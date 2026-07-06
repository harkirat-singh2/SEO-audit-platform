from app.schemas import seo_result
from app.schemas import seo_result
from app.crawler.crawler import WebsiteCrawler
from app.services.seo_analyzer import SEOAnalyzer


def main():
    crawler = WebsiteCrawler(
        base_url="https://books.toscrape.com/",
        max_pages=1,
    )

    pages = crawler.crawl()

    analyzer = SEOAnalyzer()

    for page in pages:
        result = analyzer.analyze(page)

        print("\n" + "=" * 60)
        print("SEO ANALYSIS")
        print("=" * 60)

        print(f"URL: {result.url}")
        print(f"Title: {result.title}")
        print(f"Title Length: {result.title_length}")

        print(f"\nMeta Description:")
        print(result.meta_description)
        print(f"Length: {result.meta_description_length}")

        print(f"\nWord Count: {result.word_count}")

        print(f"\nH1 Count: {result.h1_count}")
        print(f"H2 Count: {result.h2_count}")
        print(f"Total Headings: {result.total_headings}")

        print(f"\nTotal Images: {result.total_images}")
        print(f"Images Without Alt: {result.images_without_alt}")

        print(f"\nInternal Links: {result.internal_links}")
        print(f"External Links: {result.external_links}")

        print(f"\nCanonical: {result.has_canonical}")
        print(f"Canonical URL: {result.canonical_url}")

        print(f"\nLanguage: {result.language}")
        print(f"Robots: {result.robots_meta}")

        print(f"\nSEO Score: {result.seo_score}/100")

        print("\nPassed Checks")
        print("-" * 40)

        for check in result.passed_checks:
            print(f"✅ {check}")

        print("\nFailed Checks")
        print("-" * 40)

        for check in result.failed_checks:
            print(f"❌ {check}")


if __name__ == "__main__":
    main()