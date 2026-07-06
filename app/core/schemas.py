RECOMMENDATION_SCHEMA = {
        "type": "OBJECT",
        "properties": {
            "meta_title": {"type": "STRING"},
            "meta_description": {"type": "STRING"},
            "heading_structure": {"type": "STRING"},
            "image_alt_text_recommendation": {"type": "STRING"},
            "link_recommendation": {"type": "STRING"},
            "page_speed_suggestion": {"type": "STRING"},
            "mobile_optimization_suggestion": {"type": "STRING"},
            "crawl_delay_suggestion": {"type": "STRING"},
        },
        "required": [
            "meta_title",
            "meta_description",
            "heading_structure",
            "image_alt_text_recommendation",
            "link_recommendation",
            "page_speed_suggestion",
            "mobile_optimization_suggestion",
            "crawl_delay_suggestion",
        ],
    }