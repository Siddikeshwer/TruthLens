from groq import Groq

from config import GROQ_API_KEY, MODEL_NAME
from prompts import SYSTEM_PROMPT


class TruthLensAgent:

    def __init__(self):
        self.client = Groq(
            api_key=GROQ_API_KEY
        )

    def verify(self, claim: str):

        prompt = f"""
{SYSTEM_PROMPT}

Your task is to verify this claim:

"{claim}"

Give a careful evidence-based assessment.

Return ONLY valid JSON:

{{
    "claim": "the claim",
    "verdict": "TRUE",
    "confidence": 95,
    "summary": "short summary",
    "reasoning": "detailed reasoning",
    "evidence": [],
    "sources": []
}}
"""

        response = self.client.chat.completions.create(
            model=MODEL_NAME,
            messages=[
                {
                    "role": "system",
                    "content": SYSTEM_PROMPT
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.1,
            response_format={
                "type": "json_object"
            }
        )

        return response