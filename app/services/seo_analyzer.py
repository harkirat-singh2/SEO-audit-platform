from app.crawler.url_utils import is_valid_url
from app.schemas import (
    PageData,
    SEOResult,
)
from app.crawler.parser import (
    count_words,
    extract_canonical,
    extract_headings,
    extract_images,
    extract_images_without_alt,
    extract_language,
    extract_links,
    extract_meta_description,
    extract_robots_meta,
    extract_title,
)
from app.crawler.url_utils import (
    is_same_domain,
    normalize_url,
)
from app.core.seo_config import SEO_WEIGHTS, SEO_LIMITS


class SEOAnalyzer:
    """
    Performs SEO analysis on a webpage.
    """

    def analyze_title(
        self,
        page: PageData,
    ) -> tuple[str | None, int]:
        """
        Analyze the page title.
        """
        title = extract_title(page.soup)

        if title is None:
            return None, 0

        return title, len(title)

    def analyze_meta_description(
        self,
        page: PageData,
    ) -> tuple[str | None, int]:
        """
        Analyze the meta description.
        """
        description = extract_meta_description(page.soup)

        if description is None:
            return None, 0

        return description, len(description)

    def analyze_headings(
        self,
        page: PageData,
    ) -> tuple[int, int, int]:
        """
        Analyze page headings.
        """
        headings = extract_headings(page.soup)

        h1_count = len(headings["h1"])
        h2_count = len(headings["h2"])

        total = sum(
            len(values)
            for values in headings.values()
        )

        return (
            h1_count,
            h2_count,
            total,
        )

    def analyze_images(
        self,
        page: PageData,
    ) -> tuple[int, int]:
        """
        Analyze images.
        """
        images = extract_images(page.soup)
        missing_alt = extract_images_without_alt(page.soup)

        return (
            len(images),
            len(missing_alt),
        )

    def analyze_links(
        self,
        page: PageData,
    ) -> tuple[int, int]:
        """
        Count internal and external links.
        """
        internal = len(page.links)

        external_links: set[str] = set()

        for link in extract_links(page.soup):

            normalized = normalize_url(page.url, link)

            if not is_valid_url(normalized):
                continue

        if not is_same_domain(page.url, normalized):
            external_links.add(normalized)

        return internal, len(external_links)

    def analyze_content(
        self,
        page: PageData,
    ) -> int:
        """
        Analyze textual content.
        """
        return count_words(page.soup)

    def analyze_technical(
        self,
        page: PageData,
    ) -> tuple[str | None, dict[str, bool] | None, str | None]:
        """
        Analyze technical SEO signals.
        """
        canonical = extract_canonical(page.soup)
        robots = extract_robots_meta(page.soup)
        language = extract_language(page.soup)

        return (
            canonical,
            robots,
            language,
        )

    def analyze_canonical(
        self,
        page: PageData,
    ) -> tuple[bool, str | None]:
        """
        Analyze the canonical tag.
        """
        canonical = extract_canonical(page.soup)

        return (
            canonical is not None,
            canonical,
        )

    def analyze_robots(
        self,
        page: PageData,
    ) -> dict[str, bool] | None:
        """
        Analyze robots meta tag.
        """
        return extract_robots_meta(page.soup)

    def analyze_language(
        self,
        page: PageData,
    ) -> str | None:
        """
        Analyze document language.
        """
        return extract_language(page.soup)

    def evaluate_checks(
        self,
        result: SEOResult,
    ) -> tuple[list[str], list[str]]:
        """
        Evaluate all SEO checks and return passed and failed checks using dynamic limits.
        """
        passed = []
        failed = []

        title_min = SEO_LIMITS.get("title_min", 30)
        title_max = SEO_LIMITS.get("title_max", 60)
        meta_min = SEO_LIMITS.get("meta_min", 120)
        meta_max = SEO_LIMITS.get("meta_max", 160)
        min_words = SEO_LIMITS.get("min_word_count", 300)

        # Title
        if result.title:
            passed.append("Title exists")
        else:
            failed.append("Title is missing")

        if title_min <= result.title_length <= title_max:
            passed.append("Title length is optimal")
        else:
            failed.append(f"Title length should be between {title_min} and {title_max} characters")

        # Meta Description
        if result.meta_description:
            passed.append("Meta description exists")
        else:
            failed.append("Meta description is missing")

        if meta_min <= result.meta_description_length <= meta_max:
            passed.append("Meta description length is optimal")
        else:
            failed.append(f"Meta description should be between {meta_min} and {meta_max} characters")

        # Headings
        if result.h1_count == 1:
            passed.append("Exactly one H1 heading")
        else:
            failed.append("Page should contain exactly one H1 heading")

        # Content
        if result.word_count >= min_words:
            passed.append("Content length is sufficient")
        else:
            failed.append(f"Content should contain at least {min_words} words")

        # Canonical
        if result.has_canonical:
            passed.append("Canonical tag exists")
        else:
            failed.append("Canonical tag is missing")

        # Images
        if result.images_without_alt == 0:
            passed.append("All images have alt text")
        else:
            failed.append(
                f"{result.images_without_alt} image(s) are missing alt text"
            )

        # Language
        if result.language:
            passed.append("Language is specified")
        else:
            failed.append("Language attribute is missing")

        # Robots
        if (
            result.robots_meta
            and result.robots_meta.get("index", False)
        ):
            passed.append("Search engines can index the page")
        else:
            failed.append("Page is blocked from indexing")

        return passed, failed

    def calculate_score(
        self,
        result: SEOResult,
    ) -> int:
        """
        Calculate an SEO score out of 100 based on config limits and weights.
        """
        score = 0

        # Title exists
        if result.title:
            score += SEO_WEIGHTS.get("title_exists", 0)

        # Title length
        if (
            SEO_LIMITS.get("title_min", 0)
            <= result.title_length
            <= SEO_LIMITS.get("title_max", 0)
        ):
            score += SEO_WEIGHTS.get("title_length", 0)

        # Meta description
        if result.meta_description:
            score += SEO_WEIGHTS.get("meta_exists", 0)

        # Meta description length
        if (
            SEO_LIMITS.get("meta_min", 0)
            <= result.meta_description_length
            <= SEO_LIMITS.get("meta_max", 0)
        ):
            score += SEO_WEIGHTS.get("meta_length", 0)

        # H1
        if result.h1_count == 1:
            score += SEO_WEIGHTS.get("h1", 0)

        # Content
        if result.word_count >= SEO_LIMITS.get("min_word_count", 0):
            score += SEO_WEIGHTS.get("word_count", 0)

        # Canonical
        if result.has_canonical:
            score += SEO_WEIGHTS.get("canonical", 0)

        # Images
        if (
            result.total_images == 0
            or result.images_without_alt == 0
        ):
            score += SEO_WEIGHTS.get("images", 0)

        # Language
        if result.language:
            score += SEO_WEIGHTS.get("language", 0)

        # Robots
        if (
            result.robots_meta
            and result.robots_meta.get("index", False)
        ):
            score += SEO_WEIGHTS.get("robots", 0)

        return score

    def analyze(
        self,
        page: PageData,
    ) -> SEOResult:
        """
        Perform a complete SEO analysis.
        """
        title, title_length = self.analyze_title(page)

        (
            meta_description,
            meta_description_length,
        ) = self.analyze_meta_description(page)

        (
            h1_count,
            h2_count,
            total_headings,
        ) = self.analyze_headings(page)

        (
            total_images,
            images_without_alt,
        ) = self.analyze_images(page)

        word_count = self.analyze_content(page)
        internal_links, external_links = self.analyze_links(page)
        has_canonical, canonical_url = self.analyze_canonical(page)
        robots_meta = self.analyze_robots(page)
        language = self.analyze_language(page)

        # 1. Initialize the SEOResult container first
        result = SEOResult(
            url=page.url,
            title=title,
            title_length=title_length,
            meta_description=meta_description,
            meta_description_length=meta_description_length,
            word_count=word_count,
            h1_count=h1_count,
            h2_count=h2_count,
            total_headings=total_headings,
            total_images=total_images,
            images_without_alt=images_without_alt,
            internal_links=internal_links,
            external_links=external_links,
            has_canonical=has_canonical,
            canonical_url=canonical_url,
            robots_meta=robots_meta,
            language=language,
            seo_score=0,
            passed_checks=[],  # Assumed default fields or placeholder lists
            failed_checks=[],
        )

        # 2. Evaluate checks using the initialized result instance
        passed, failed = self.evaluate_checks(result)

        # 3. Assign evaluated data to target properties
        result.passed_checks = passed
        result.failed_checks = failed

        # 4. Generate and store final metric score
        result.seo_score = self.calculate_score(result)

        return result
