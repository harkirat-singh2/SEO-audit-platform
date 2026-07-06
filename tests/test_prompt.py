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

    prompt = recommendation_service.build_prompt(
        seo_result,
    )

    print(prompt)


if __name__ == "__main__":
    main()