from app.database.session import SessionLocal
from app.services.audit_service import AuditService


def main():
    db = SessionLocal()

    try:
        service = AuditService(db)

        results = service.run_audit(
            "https://books.toscrape.com/",
        )

        first = results[0]

        print(f"Pages Audited: {len(results)}")
        print(f"SEO Score: {first.seo.seo_score}")

        if first.recommendation:
            print(first.recommendation.meta_description)

    finally:
        db.close()


if __name__ == "__main__":
    main()