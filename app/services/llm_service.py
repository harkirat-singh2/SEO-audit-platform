import time
from openai import OpenAI
from app.core.config import settings
from app.core.logger import logger

class LLMService:
    """
    Handles communication with OpenRouter using the OpenAI SDK client.
    """
    def __init__(self):
        self.client = OpenAI(
        api_key=settings.OPENROUTER_API_KEY,
        base_url="https://openrouter.ai/api/v1",
)

    def generate(
        self,
        prompt: str,
        response_schema: dict | None = None,
    ) -> str:
        """
        Generate content using OpenRouter.
        """
        try:
            logger.info("Sending prompt to OpenRouter")
            start = time.perf_counter()

            response = self.client.chat.completions.create(
                model=settings.OPENROUTER_MODEL,
                messages=[
                    {
                        "role": "system",
                        "content": (
                            "You are an expert SEO consultant. "
                            "Always return valid JSON only."
                        ),
                    },
                    {
                        "role": "user",
                        "content": prompt,
                    },
                ],
                temperature=0.2,
            )

            elapsed = time.perf_counter() - start
            logger.info("OpenRouter responded in %.2f seconds", elapsed)
            
            # Fixed: Correctly indexing the first choice from the response array
            return response.choices[0].message.content

        except Exception:
            logger.exception("OpenRouter request failed")
            raise
