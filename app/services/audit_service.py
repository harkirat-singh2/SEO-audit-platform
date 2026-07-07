from sqlalchemy.orm import Session 
from app.core.config import settings 
from app.core.logger import logger 
from app.crawler.crawler import WebsiteCrawler 
from app.services.seo_analyzer import SEOAnalyzer 
from app.services.recommendation_service import RecommendationService 
from app.schemas import AuditResult 
from datetime import datetime 
from app.models.audit import Audit 
from app.models.page import Page 
from app.models.seo_analysis import SEOAnalysis 
from app.models.recommendation import Recommendation

class AuditService: 
    """ Coordinates the complete SEO audit workflow. """ 
    
    def __init__(self, db: Session): 
        self.db = db 
        self.analyzer = SEOAnalyzer() 
        self.recommendation_service = RecommendationService() 

    def run_audit(self, url: str, max_pages: int = 100): 
        """ Crawl a website, analyze each page, and generate AI recommendations. """ 
        try: 
            logger.info("Starting audit for %s", url) 
            audit = Audit( 
                website_url=url, 
                status="RUNNING", 
                started_at=datetime.utcnow(), 
            ) 
            self.db.add(audit) 
            self.db.flush() 
            logger.info("Created audit with ID %d", audit.id) 

            crawler = WebsiteCrawler( 
                base_url=url, 
                max_pages=max_pages, 
            ) 
            pages = crawler.crawl() 
            logger.info("Crawled %d pages", len(pages)) 
            
            results = [] 
            for index, page in enumerate(pages): 
                page_model = Page( 
                    audit_id=audit.id, 
                    url=page.url, 
                    http_status=200, 
                ) 
                self.db.add(page_model) 
                self.db.flush() 
                logger.info("Saved page '%s' with ID %d", page.url, page_model.id) 

                logger.info("Analyzing page: %s", page.url) 
                seo_result = self.analyzer.analyze(page) 
                
                analysis = SEOAnalysis(
    page_id=page_model.id,

    title=seo_result.title,
    title_length=seo_result.title_length,

    meta_description=seo_result.meta_description,
    meta_description_length=seo_result.meta_description_length,

    word_count=seo_result.word_count,

    h1_count=seo_result.h1_count,
    h2_count=seo_result.h2_count,
    total_headings=seo_result.total_headings,

    total_images=seo_result.total_images,
    images_without_alt=seo_result.images_without_alt,

    internal_links=seo_result.internal_links,
    external_links=seo_result.external_links,

    has_canonical=seo_result.has_canonical,
    canonical_url=seo_result.canonical_url,

    robots_meta=(
        str(seo_result.robots_meta)
        if seo_result.robots_meta
        else None
    ),

    language=seo_result.language,

    seo_score=seo_result.seo_score,
)

                self.db.add(analysis)
                self.db.flush()

                logger.info(
                    "Saved SEO analysis for page ID %d",
                    page_model.id,
)

                recommendation = None 
                if index < settings.MAX_AI_RECOMMENDATIONS: 
                    logger.info("Generating AI recommendations") 
                    recommendation = self.recommendation_service.generate(seo_result) 
                else: 
                    logger.info("Skipping AI recommendation for %s (limit reached)", page.url) 
                    
                if recommendation is not None:

                    recommendation_model = Recommendation(
                        page_id=page_model.id,

                        meta_title=recommendation.meta_title,

                        meta_description=recommendation.meta_description,

        heading_structure=recommendation.heading_structure,

        image_alt_text_recommendation=(
            recommendation.image_alt_text_recommendation
        ),

        link_recommendation=(
            recommendation.link_recommendation
        ),

        page_speed_suggestion=(
            recommendation.page_speed_suggestion
        ),

        mobile_optimization_suggestion=(
            recommendation.mobile_optimization_suggestion
        ),

        crawl_delay_suggestion=(
            recommendation.crawl_delay_suggestion
        ),
    )

                    self.db.add(recommendation_model)

                    self.db.flush()

                    logger.info(
                        "Saved AI recommendations for page ID %d",
                        page_model.id,
                    )    

                results.append( 
                    AuditResult( 
                        page=page, 
                        seo=seo_result, 
                        recommendation=recommendation, 
                    ) 
                ) 

            # Fix 2: Update Audit Status before completion log 
            audit.status = "COMPLETED" 
            audit.completed_at = datetime.utcnow() 
            logger.info("Audit completed successfully") 

            # Fix 3: Flush before committing and returning 
            self.db.flush() 
            # Fix 1: Commit everything within the success block 
            self.db.commit() 
            return results 

        except Exception as e: 
            # Fix 1: Rollback transaction on failure 
            logger.error("Audit failed for %s. Rolling back. Error: %s", url, str(e)) 
            self.db.rollback() 
            raise
