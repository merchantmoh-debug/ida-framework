import pytest
from ida.core.evidence import Evidence, EvidenceChain
from ida.core.claim import Claim
from ida.core.hypothesis import Hypothesis
from ida.core.argument import Argument, Counterargument, Rebuttal

def test_evidence_initialization():
    ev = Evidence(description="Test data", confidence=0.9)
    assert ev.confidence == 0.9
    assert ev.type == "general"

def test_evidence_invalid_confidence():
    with pytest.raises(ValueError):
        Evidence(description="Bad data", confidence=1.5)

def test_evidence_chain():
    chain = EvidenceChain()
    ev1 = Evidence(description="A")
    ev2 = Evidence(description="B")
    chain.add_evidence(ev1)
    chain.add_evidence(ev2)
    assert len(chain) == 2
    assert chain.items[0] == ev1

def test_hypothesis_creation():
    hyp = Hypothesis(
        statement="Sky is blue",
        assumptions=["Sun exists"],
        testable_predictions=["Spectroscopy"]
    )
    assert "Sun exists" in hyp.assumptions

def test_argument_structure():
    arg = Argument(
        claim="LLMs are useful",
        evidence=[Evidence(description="Usage stats")],
        warrant="High adoption implies utility",
        limitations=["Bias"]
    )
    assert arg.claim == "LLMs are useful"
    assert len(arg.evidence) == 1
    assert arg.limitations[0] == "Bias"

def test_checklist_integration():
    arg = Argument(
        claim="Claim",
        warrant="Warrant"
    )
    # Should produce checklist with warnings about missing evidence
    checklist = arg.generate_reproducibility_checklist()
    assert any("[!] No evidence provided" in item for item in checklist)
    assert any("Warrant" in item for item in checklist)
