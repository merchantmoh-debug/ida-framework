from dataclasses import dataclass, field
from typing import List

@dataclass
class Hypothesis:
    """
    A proposed explanation made on the basis of limited evidence as a starting point for further investigation.
    """
    statement: str
    assumptions: List[str] = field(default_factory=list)
    testable_predictions: List[str] = field(default_factory=list)
