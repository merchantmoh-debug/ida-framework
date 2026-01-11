from dataclasses import dataclass, field
from typing import List, Optional

@dataclass
class Claim:
    """
    A specific assertion that requires evidence.
    """
    statement: str
    confidence: float = 1.0
