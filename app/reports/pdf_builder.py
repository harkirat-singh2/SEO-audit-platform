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
        ["Canonical", str(result.seo.has_canonical)],
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
    for check in result.seo.passed_checks:
        story.append(
            Paragraph(
                "✔ " + check,
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
    for check in result.seo.failed_checks:
        story.append(
            Paragraph(
                "✘ " + check,
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
        
        recommendations = [
            result.recommendation.meta_title,
            result.recommendation.meta_description,
            result.recommendation.heading_structure,
            result.recommendation.image_alt_text_recommendation,
            result.recommendation.link_recommendation,
            result.recommendation.page_speed_suggestion,
            result.recommendation.mobile_optimization_suggestion,
            result.recommendation.crawl_delay_suggestion,
        ]
        
        recommendations = [
            r for r in recommendations if r and r.strip() != "No changes required."
        ]
        
        if recommendations:
            for recommendation in recommendations:
                story.append(
                    Paragraph(
                        "• " + recommendation,
                        NORMAL_STYLE,
                    )
                )
        else:
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
