from dataclasses import dataclass, field
from typing import List, Optional, Union
from ida.core.evidence import Evidence
from ida.core.claim import Claim
# Local import to avoid circular dependency if validation imports Argument
# But here we need to import checklist logic.
# However, checklists.py imports Argument (type hint).
# To avoid circular import at module level, we import inside the method.

@dataclass
class Counterargument:
    statement: str
    strength: str = "moderate"  # weak, moderate, strong

@dataclass
class Rebuttal:
    counterargument: Counterargument
    response: str
    evidence: Optional[Evidence] = None

@dataclass
class Argument:
    """
    The core structure representing a reasoned argument.
    """
    claim: str
    evidence: List[Evidence] = field(default_factory=list)
    warrant: str = ""
    counterarguments: List[Union[str, Counterargument]] = field(default_factory=list)
    rebuttals: List[Rebuttal] = field(default_factory=list)
    limitations: List[str] = field(default_factory=list)

    def generate_reproducibility_checklist(self) -> List[str]:
        from ida.reproducibility.checklists import generate_checklist
        return generate_checklist(self)
