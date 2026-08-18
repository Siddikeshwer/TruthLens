import json

from models import VerificationResult


class Verifier:

    def __init__(self, agent):
        self.agent = agent

    def verify_claim(self, claim: str):

        response = self.agent.verify(claim)

        text = response.choices[0].message.content

        result_data = json.loads(text)

        result = VerificationResult(
            **result_data
        )

        return {
            "result": result,
            "citations": []
        }