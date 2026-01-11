from dataclasses import dataclass
from typing import List, Dict
from ida.core.argument import Argument
from .metrics import calculate_completeness_score, assess_evidence_strength

@dataclass
class ValidationResult:
    quality_score: float
    evidence_strength: str
    missing_elements: List[str]

class Validator:
    def validate(self, argument: Argument) -> ValidationResult:
        score = calculate_completeness_score(argument)
        strength = assess_evidence_strength(argument.evidence)

        missing = []
        if not argument.warrant:
            missing.append("warrant")
        if not argument.counterarguments:
            missing.append("counterarguments")
        if not argument.limitations:
            missing.append("limitations")
        if not argument.evidence:
            missing.append("evidence")

        return ValidationResult(
            quality_score=score,
            evidence_strength=strength,
            missing_elements=missing
        )
