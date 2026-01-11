from dataclasses import dataclass, field
from typing import Optional, List, Any

@dataclass
class Evidence:
    """
    Represents a piece of evidence supporting a claim.
    """
    description: str
    type: str = "general"
    source: Optional[str] = None
    confidence: float = 1.0
    sample_size: Optional[int] = None
    metadata: dict = field(default_factory=dict)

    def __post_init__(self):
        if not (0.0 <= self.confidence <= 1.0):
            raise ValueError("Confidence must be between 0.0 and 1.0")

@dataclass
class EvidenceChain:
    """
    A collection of evidence linked to support a specific point.
    """
    items: List[Evidence] = field(default_factory=list)

    def add_evidence(self, evidence: Evidence) -> None:
        self.items.append(evidence)

    def __iter__(self):
        return iter(self.items)

    def __len__(self):
        return len(self.items)
