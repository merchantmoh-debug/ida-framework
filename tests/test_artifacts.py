import os
import pytest
from ida.core.argument import Argument
from ida.core.evidence import Evidence
from ida.reproducibility.artifacts import ResearchArtifact

def test_markdown_generation(tmp_path):
    arg = Argument(
        claim="Test Claim",
        evidence=[Evidence("Data", source="file.csv")],
        warrant="Logic"
    )
    artifact = ResearchArtifact(argument=arg)

    output_file = tmp_path / "test_artifact.md"
    artifact.export_markdown(str(output_file))

    assert output_file.exists()
    content = output_file.read_text()
    assert "Test Claim" in content
    assert "file.csv" in content
    assert "Reproducibility Checklist" in content

def test_checklist_generation_logic(tmp_path):
    arg = Argument(claim="Empty")
    artifact = ResearchArtifact(argument=arg)
    output_file = tmp_path / "empty.md"
    artifact.export_markdown(str(output_file))
    content = output_file.read_text()
    assert "[!] No evidence provided" in content
