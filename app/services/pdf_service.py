from pathlib import Path

from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import (
    Paragraph,
    SimpleDocTemplate,
)


class PDFService:
    """
    Generates SEO Audit PDF reports.
    """

    def generate(
        self,
        filename: str,
    ) -> str:
        """
        Create a simple PDF.
        """

        output = Path(filename)

        document = SimpleDocTemplate(
            str(output),
        )

        styles = getSampleStyleSheet()

        story = []

        story.append(
            Paragraph(
                "AI SEO Audit Report",
                styles["Title"],
            )
        )

        story.append(
            Paragraph(
                "Generated Successfully!",
                styles["Normal"],
            )
        )

        document.build(story)

        return str(output)