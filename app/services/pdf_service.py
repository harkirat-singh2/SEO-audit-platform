from pathlib import Path

from reportlab.platypus import SimpleDocTemplate

from app.reports.pdf_builder import build_story


class PDFService:

    def generate(
        self,
        result,
        filename: str,
    ) -> str:

        output = Path(filename)

        document = SimpleDocTemplate(
            str(output),
        )

        story = build_story(result)

        document.build(story)

        return str(output)