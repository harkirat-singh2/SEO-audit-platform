from datetime import datetime
from reportlab.lib import colors
from reportlab.platypus import (
    Paragraph,
    Spacer,
    Table,
    TableStyle,
)
from app.reports.pdf_styles import (
    TITLE_STYLE,
    SECTION_STYLE,
    NORMAL_STYLE,
)

def get_score_color(score: int):
    """
    Return a color based on the SEO score.
    """
    if score >= 80:
        return colors.green
    if score >= 50:
        return colors.orange
    return colors.red

def build_story(result):
    story = []

    # ----------------------------
    # Title
    # ----------------------------
    story.append(
        Paragraph(
            "AI SEO AUDIT REPORT",
            TITLE_STYLE,
        )
    )
    story.append(Spacer(1, 20))

    # ----------------------------
    # Website
    # ----------------------------
    story.append(
        Paragraph(
            "<b>Website:</b> " + result.page.url,
            NORMAL_STYLE,
        )
    )
    story.append(
        Paragraph(
            f"<b>Generated:</b> {datetime.now():%d %B %Y %H:%M}",
            NORMAL_STYLE,
        )
    )
    story.append(Spacer(1, 20))

    # ----------------------------
    # SEO Score
    # ----------------------------
    story.append(
        Paragraph(
            "SEO SCORE",
            SECTION_STYLE,
        )
    )
    score = result.seo.seo_score
    color = get_score_color(score)
    story.append(
        Paragraph(
            f'<font color="{color.hexval()}"><b>{score}/100</b></font>',
            NORMAL_STYLE,
        )
    )
    story.append(Spacer(1, 20))

    # ----------------------------
    # SEO Metrics
    # ----------------------------
    story.append(
        Paragraph(
            "SEO METRICS",
            SECTION_STYLE,
        )
    )
    
    table_data = [
        ["Metric", "Value"],
        ["Title Length", result.seo.title_length],
        ["Meta Description Length", result.seo.meta_description_length],
        ["Word Count", result.seo.word_count],
        ["H1 Count", result.seo.h1_count],
        ["H2 Count", result.seo.h2_count],
        ["Images", result.seo.total_images],
        ["Internal Links", result.seo.internal_links],
        ["External Links", result.seo.external_links],
        ["Language", result.seo.language],
        ["Canonical", "Yes" if result.seo.has_canonical else "No"],
    ]
    
    table = Table(
        table_data,
        colWidths=[220, 120],
    )
    table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), colors.darkblue),
                ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
                ("GRID", (0, 0), (-1, -1), 1, colors.grey),
                ("BACKGROUND", (0, 1), (-1, -1), colors.whitesmoke),
                ("BOTTOMPADDING", (0, 0), (-1, 0), 8),
                ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
                ("ALIGN", (1, 1), (1, -1), "CENTER"),
            ]
        )
    )
    story.append(table)
    story.append(Spacer(1, 20))

    # ----------------------------
    # Passed Checks
    # ----------------------------
    story.append(
        Paragraph(
            "PASSED CHECKS",
            SECTION_STYLE,
        )
    )

    passed_checks = []

    if result.seo.title:
        passed_checks.append("Title exists")

    if result.seo.h1_count == 1:
        passed_checks.append("Exactly one H1 heading")

    if result.seo.images_without_alt == 0:
        passed_checks.append("All images have alt text")

    if result.seo.language:
        passed_checks.append("Language is specified")

    if result.seo.has_canonical:
        passed_checks.append("Canonical tag exists")

    if passed_checks:
        for check in passed_checks:
            story.append(
                Paragraph(
                    "✔ " + check,
                    NORMAL_STYLE,
                )
            )
    else:
        story.append(
            Paragraph(
                "No passed checks.",
                NORMAL_STYLE,
            )
        )

    story.append(Spacer(1, 20))

    # ----------------------------
    # Failed Checks
    # ----------------------------
    story.append(
        Paragraph(
            "FAILED CHECKS",
            SECTION_STYLE,
        )
    )

    failed_checks = []

    if not result.seo.title:
        failed_checks.append("Title is missing")
    elif not (30 <= result.seo.title_length <= 60):
        failed_checks.append("Title length should be between 30 and 60 characters")

    if not result.seo.meta_description:
        failed_checks.append("Meta description is missing")
    elif not (120 <= result.seo.meta_description_length <= 160):
        failed_checks.append("Meta description should be between 120 and 160 characters")

    if result.seo.word_count < 300:
        failed_checks.append("Content should contain at least 300 words")

    if not result.seo.has_canonical:
        failed_checks.append("Canonical tag is missing")

    if failed_checks:
        for check in failed_checks:
            story.append(
                Paragraph(
                    "✘ " + check,
                    NORMAL_STYLE,
                )
            )
    else:
        story.append(
            Paragraph(
                "No failed checks.",
                NORMAL_STYLE,
            )
        )

    story.append(Spacer(1, 20))

    # ----------------------------
    # AI Recommendations
    # ----------------------------
    if result.recommendation:
        story.append(
            Paragraph(
                "AI RECOMMENDATIONS",
                SECTION_STYLE,
            )
        )
        
        recommendations = {
            "Meta Title": result.recommendation.meta_title,
            "Meta Description": result.recommendation.meta_description,
            "Heading Structure": result.recommendation.heading_structure,
            "Image Alt Text": result.recommendation.image_alt_text_recommendation,
            "Link Recommendation": result.recommendation.link_recommendation,
            "Page Speed": result.recommendation.page_speed_suggestion,
            "Mobile Optimization": result.recommendation.mobile_optimization_suggestion,
            "Crawl Delay": result.recommendation.crawl_delay_suggestion,
        }

        has_recommendation = False

        for title, text in recommendations.items():
            if (
                text
                and text.strip().lower() not in (
                    "no changes required",
                    "no changes required.",
                )
            ):
                has_recommendation = True
                story.append(
                    Paragraph(
                        f"<b>{title}:</b> {text}",
                        NORMAL_STYLE,
                    )
                )

        if not has_recommendation:
            story.append(
                Paragraph(
                    "No additional recommendations.",
                    NORMAL_STYLE,
                )
            )
            
    story.append(Spacer(1, 30))
    story.append(
        Paragraph(
            "<b>Generated by AI SEO Audit Platform</b>",
            NORMAL_STYLE,
        )
    )
    
    return story
