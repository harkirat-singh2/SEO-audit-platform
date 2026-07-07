from app.services.pdf_service import PDFService


def main():

    pdf = PDFService()

    path = pdf.generate(
        "audit_report.pdf",
    )

    print(path)


if __name__ == "__main__":
    main()