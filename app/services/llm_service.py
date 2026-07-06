from google import genai
from google.genai import types
from app.core.logger import logger
from app.core.config import settings
import time

start = time.perf_counter()

response = ...

elapsed = time.perf_counter() - start

logger.info(
    "Gemini responded in %.2f seconds",
    elapsed,
)

class LLMService:
    """
    Handles communication with Gemini.
    """

    def __init__(self):
        self.client = None

    def get_client(self):
        """
        Lazily create the Gemini client.
        """
        if self.client is None:
            self.client = genai.Client(
                api_key=settings.GEMINI_API_KEY,
            )

        return self.client

    def generate(
        self,
        prompt: str,
        response_schema: dict | None = None,
    ) -> str:
        """
        Generate content using Gemini.
        """

        client = self.get_client()

        config = None

        if response_schema is not None:
            config = types.GenerateContentConfig(
                response_mime_type="application/json",
                response_schema=response_schema,
            )

        try:
            logger.info("Sending prompt to Gemini")

            response = client.models.generate_content(
                model=settings.GEMINI_MODEL,
                contents=prompt,
                config=config,
            )

            logger.info("Received response from Gemini")

            return response.text

        except Exception:
            logger.exception("Gemini request failed")
            raise