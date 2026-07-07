from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.styles import (
    ParagraphStyle,
    getSampleStyleSheet,
)


styles = getSampleStyleSheet()

TITLE_STYLE = ParagraphStyle(
    "Title",
    parent=styles["Title"],
    alignment=TA_CENTER,
    textColor=colors.darkblue,
    spaceAfter=20,
)

SECTION_STYLE = ParagraphStyle(
    "Section",
    parent=styles["Heading2"],
    textColor=colors.white,
    backColor=colors.darkblue,
    alignment=TA_CENTER,
    spaceBefore=10,
    spaceAfter=10,
)

NORMAL_STYLE = styles["BodyText"]