import json

from app.schemas import (
    RecommendationResult,
    SEOResult,
)
from app.services.llm_service import LLMService
from app.core.schemas import RECOMMENDATION_SCHEMA
from app.core.logger import logger

class RecommendationService:
    """
    Generates AI-powered SEO recommendations.
    """
    def __init__(self):
        self.llm = LLMService()

    def build_prompt(
        self,
        result: SEOResult,
    ) -> str:
        """
        Build a structured prompt for Gemini.
        """
        passed = "\n".join(
            f"- {check}" for check in result.passed_checks
        )
        failed = "\n".join(
            f"- {check}" for check in result.failed_checks
        )

        metrics = f"""
        Title Length: {result.title_length}
        Meta Description Length: {result.meta_description_length}
        Word Count: {result.word_count}
        H1 Count: {result.h1_count}
        H2 Count: {result.h2_count}
        Total Images: {result.total_images}
        Images Without Alt: {result.images_without_alt}
        Internal Links: {result.internal_links}
        External Links: {result.external_links}
        Canonical: {result.has_canonical}
        Language: {result.language}
        """

        return f"""
        Role
        ----
        You are an experienced SEO consultant.

        Task
        ----
        Analyze the SEO audit below and provide actionable recommendations.

        Website
        -------
        {result.url}

        SEO Score
        ---------
        {result.seo_score}/100

        Metrics
        -------
        {metrics}

        Passed Checks
        -------------
        {passed}

        Failed Checks
        -------------
        {failed}

        Output Requirements
        -------------------
        Return ONLY a valid JSON object. Do NOT include:
        - Markdown
        - Triple backticks
        - Explanations
        - Notes

        Every value must be a string. 
        
        CRITICAL RULE FOR RECOMENDATIONS:
        Generate recommendations ONLY for failed checks. Do not invent improvements, tips, or preventative advice for any passed checks. For every JSON field below that corresponds to a passed check or has no issues, you must return exactly: "No changes required."

        JSON Schema
        -----------
        {{
          "meta_title": "",
          "meta_description": "",
          "heading_structure": "",
          "image_alt_text_recommendation": "",
          "link_recommendation": "",
          "page_speed_suggestion": "",
          "mobile_optimization_suggestion": "",
          "crawl_delay_suggestion": ""
        }}
        """

    def clean_json_response(
        self,
        response: str,
    ) -> str:
        """
        Remove markdown code fences from Gemini responses.
        """
        response = response.strip()
        if response.startswith("```json"):
            response = response.replace("```json", "", 1)
        if response.startswith("```"):
            response = response.replace("```", "", 1)
        if response.endswith("```"):
            response = response[:-3]
        return response.strip()

    def parse_response(
    self,
    response: str,
) -> RecommendationResult:
        """
        Parse Gemini JSON into RecommendationResult.
        """

        cleaned = self.clean_json_response(
        response,
    )

        try:
            data = json.loads(cleaned)

        except json.JSONDecodeError:
            logger.exception(
                "Failed to parse Gemini JSON"
            )
            raise

        return RecommendationResult(**data)

    def generate(
        self,
        result: SEOResult,
    ) -> RecommendationResult:
        """
        Generate AI-powered SEO recommendations.
        """

        prompt = self.build_prompt(result)

        response = self.llm.generate(prompt ,RECOMMENDATION_SCHEMA)

        return self.parse_response(response)