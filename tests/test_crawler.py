from app.crawler.crawler import WebsiteCrawler


def main():
    crawler = WebsiteCrawler(
    base_url="https://books.toscrape.com/",
    max_pages=10,
)

    pages = crawler.crawl()

    print(f"\nPages Crawled: {len(pages)}")

    for page in pages:
        print("-" * 50)
        print(f"URL: {page.url}")
        print(f"Status: {page.status_code}")
        print(f"Links Found: {len(page.links)}")


if __name__ == "__main__":
    main()