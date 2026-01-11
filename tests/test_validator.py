import pytest
from ida.core.argument import Argument
from ida.core.evidence import Evidence
from ida.validation.validator import Validator

def test_validator_perfect_score():
    arg = Argument(
        claim="Claim",
        evidence=[Evidence("Ev", type="experimental", confidence=0.9)],
        warrant="Warrant",
        counterarguments=["Counter"],
        limitations=["Limit"]
    )
    validator = Validator()
    result = validator.validate(arg)

    assert result.quality_score == 100.0
    assert result.evidence_strength == "strong"
    assert len(result.missing_elements) == 0

def test_validator_incomplete():
    arg = Argument(claim="Empty Claim")
    validator = Validator()
    result = validator.validate(arg)

    assert result.quality_score == 20.0 # Only claim present
    assert "evidence" in result.missing_elements
    assert result.evidence_strength == "weak"

def test_evidence_strength_logic():
    # Moderate case
    arg = Argument(
        claim="Claim",
        evidence=[Evidence("Ev", confidence=0.6, type="anecdotal")]
    )
    validator = Validator()
    result = validator.validate(arg)
    assert result.evidence_strength == "moderate"
