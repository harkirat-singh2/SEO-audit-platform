from app.database.session import SessionLocal
from app.services.audit_service import AuditService
from app.services.pdf_service import PDFService


def main():
    db = SessionLocal()

    try:
        audit_service = AuditService(db)

        audit = audit_service.run_audit(
            "https://quotes.toscrape.com/",
            max_pages=1,
        )

        pdf = PDFService()

        pdf.generate(
            audit["results"][0],
            "audit_report.pdf",
        )

        print("PDF generated successfully!")

    finally:
        db.close()


if __name__ == "__main__":
    main()