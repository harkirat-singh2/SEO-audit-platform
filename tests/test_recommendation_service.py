from app.crawler.crawler import WebsiteCrawler
from app.services.seo_analyzer import SEOAnalyzer
from app.services.recommendation_service import RecommendationService


def main():
    crawler = WebsiteCrawler(
        base_url="https://books.toscrape.com/",
        max_pages=1,
    )

    page = crawler.crawl()[0]

    analyzer = SEOAnalyzer()
    seo_result = analyzer.analyze(page)

    recommendation_service = RecommendationService()

    recommendation = recommendation_service.generate(
        seo_result,
    )

    print("\n" + "=" * 60)
    print("AI SEO RECOMMENDATIONS")
    print("=" * 60)

    print(f"Meta Title:\n{recommendation.meta_title}\n")

    print(f"Meta Description:\n{recommendation.meta_description}\n")

    print(f"Heading Structure:\n{recommendation.heading_structure}\n")

    print(
        "Image Alt Recommendation:\n"
        f"{recommendation.image_alt_text_recommendation}\n"
    )

    print(
        "Link Recommendation:\n"
        f"{recommendation.link_recommendation}\n"
    )

    print(
        "Page Speed:\n"
        f"{recommendation.page_speed_suggestion}\n"
    )

    print(
        "Mobile Optimization:\n"
        f"{recommendation.mobile_optimization_suggestion}\n"
    )

    print(
        "Crawl Delay:\n"
        f"{recommendation.crawl_delay_suggestion}\n"
    )


if __name__ == "__main__":
    main()
    