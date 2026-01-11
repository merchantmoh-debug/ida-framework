from typing import List, Dict, Any
from ida.core.argument import Argument
from ida.core.evidence import Evidence

def calculate_completeness_score(argument: Argument) -> float:
    """
    Calculates a 0-100 score based on the presence of key components.
    """
    score = 0
    weights = {
        "claim": 20,
        "evidence": 30,
        "warrant": 20,
        "counterarguments": 15,
        "limitations": 15
    }

    if argument.claim:
        score += weights["claim"]

    if argument.evidence and len(argument.evidence) > 0:
        score += weights["evidence"]

    if argument.warrant:
        score += weights["warrant"]

    if argument.counterarguments and len(argument.counterarguments) > 0:
        score += weights["counterarguments"]

    if argument.limitations and len(argument.limitations) > 0:
        score += weights["limitations"]

    return float(score)

def assess_evidence_strength(evidence_list: List[Evidence]) -> str:
    if not evidence_list:
        return "weak"

    avg_confidence = sum(e.confidence for e in evidence_list) / len(evidence_list)
    has_experimental = any(e.type == "experimental" for e in evidence_list)

    if avg_confidence > 0.8 and has_experimental:
        return "strong"
    elif avg_confidence > 0.5:
        return "moderate"
    else:
        return "weak"
