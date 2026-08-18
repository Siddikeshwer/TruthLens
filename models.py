from typing import List, Literal, Union
from pydantic import BaseModel, Field


VerdictType = Literal[
    "TRUE",
    "MOSTLY_TRUE",
    "MISLEADING",
    "MOSTLY_FALSE",
    "FALSE",
    "UNVERIFIABLE",
    "OPINION"
]


class Source(BaseModel):
    title: str = ""
    url: str = ""
    source_type: str = "unknown"


class Evidence(BaseModel):
    source_title: str = ""
    source_url: str = ""
    supports_claim: bool = False
    explanation: str = ""


class VerificationResult(BaseModel):
    claim: str

    verdict: VerdictType

    confidence: float = Field(
        ge=0,
        le=100
    )

    summary: str

    reasoning: str

    evidence: List[Union[Evidence, str]] = []

    sources: List[Union[Source, str]] = []