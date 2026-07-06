from collections import deque

import requests

from app.core.logger import logger
from app.crawler.parser import (
    create_soup,
    extract_links,
)
from app.crawler.url_utils import (
    is_same_domain,
    is_valid_url,
    normalize_url,
)
from app.schemas import PageData

class WebsiteCrawler:
    """
    Crawls a website using the Breadth-First Search (BFS) algorithm.
    """

    def __init__(
        self,
        base_url: str,
        max_pages: int = 100,
        timeout: int = 10,
    ):
        self.base_url = base_url
        self.max_pages = max_pages
        self.timeout = timeout

        # URLs that have already been crawled
        self.visited: set[str] = set()

        # URLs that have already been discovered
        self.discovered: set[str] = {base_url}

        # BFS Queue
        self.queue: deque[str] = deque([base_url])

        # Reusable HTTP session
        self.session = requests.Session()
        self.session.headers.update(
            {
                "User-Agent": (
                    "SEOAuditBot/1.0 "
                    "(Educational Project)"
                )
            }
        )

        logger.info(
            "Crawler initialized for %s",
            self.base_url,
        )

    def fetch_page(
        self,
        url: str,
    ) -> tuple[str, int] | None:
        """
        Download a webpage.

        Returns:
            (html, status_code) on success.
            None on failure.
        """
        try:
            logger.info("Fetching page: %s", url)

            response = self.session.get(
                url,
                timeout=self.timeout,
            )

            response.raise_for_status()

            logger.info(
                "Successfully fetched: %s",
                url,
            )

            return (
                response.text,
                response.status_code,
            )

        except requests.RequestException as exc:
            logger.error(
                "Failed to fetch %s: %s",
                url,
                exc,
            )
            return None

    def process_page(
        self,
        url: str,
    ) -> PageData | None:
        """
        Download, parse and process a webpage.
        """
        result = self.fetch_page(url)

        if result is None:
            logger.warning(
                "Skipping page because download failed: %s",
                url,
            )
            return None

        html, status_code = result

        soup = create_soup(html)

        raw_links = extract_links(soup)

        logger.info(
            "Found %d raw links on %s",
            len(raw_links),
            url,
        )

        cleaned_links: set[str] = set()

        for link in raw_links:

            if not link:
                continue

            normalized_url = normalize_url(
                url,
                link,
            )

            if not is_valid_url(normalized_url):
                continue

            if not is_same_domain(
                self.base_url,
                normalized_url,
            ):
                continue

            cleaned_links.add(normalized_url)

        logger.info(
            "Retained %d internal links on %s",
            len(cleaned_links),
            url,
        )

        return PageData(
            url=url,
            html=html,
            soup=soup,
            links=list(cleaned_links),
            status_code=status_code,
        )

    def enqueue_links(
        self,
        links: list[str],
    ) -> None:
        """
        Add newly discovered URLs to the crawl queue.
        """
        added = 0

        for link in links:

            if link in self.discovered:
                continue

            self.discovered.add(link)
            self.queue.append(link)
            added += 1

        logger.debug(
            "Added %d new URLs to queue",
            added,
        )

    def crawl(
        self,
    ) -> list[PageData]:
        """
        Crawl the website using Breadth-First Search (BFS).
        """
        crawled_pages: list[PageData] = []

        try:

            while (
                self.queue
                and len(self.visited) < self.max_pages
            ):

                current_url = self.queue.popleft()

                if current_url in self.visited:
                    continue

                self.visited.add(current_url)

                logger.info(
                    "Crawling (%d/%d): %s",
                    len(self.visited),
                    self.max_pages,
                    current_url,
                )

                page = self.process_page(current_url)

                if page is None:
                    continue

                crawled_pages.append(page)

                self.enqueue_links(page.links)

            logger.info(
                "Crawl completed. Successfully crawled %d pages.",
                len(crawled_pages),
            )

            return crawled_pages

        finally:
            self.session.close()
            logger.info("HTTP session closed.")