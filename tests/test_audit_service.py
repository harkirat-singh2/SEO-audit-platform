from app.database.session import SessionLocal
from app.services.audit_service import AuditService


URL = "https://quotes.toscrape.com/"
MAX_PAGES = 5


def main():
    db = SessionLocal()

    try:
        service = AuditService(db)

        results = service.run_audit(
            URL,max_pages=MAX_PAGES
        )

        print(f"Pages Audited: {len(results)}")

        if results:
            first = results[0]

            print(f"SEO Score: {first.seo.seo_score}")

            if first.recommendation:
                print(first.recommendation.meta_description)

    finally:
        db.close()


if __name__ == "__main__":
    main()