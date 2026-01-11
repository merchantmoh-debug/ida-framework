import os
from dataclasses import dataclass
from typing import List, Optional
from ida.core.argument import Argument
from ida.core.hypothesis import Hypothesis
from ida.reproducibility.checklists import generate_checklist

@dataclass
class ResearchArtifact:
    hypothesis: Optional[Hypothesis] = None
    argument: Optional[Argument] = None

    def export_markdown(self, filepath: str) -> None:
        content = ["# Research Artifact\n"]

        if self.hypothesis:
            content.append("## Hypothesis")
            content.append(f"**Statement:** {self.hypothesis.statement}\n")
            if self.hypothesis.assumptions:
                content.append("### Assumptions")
                for a in self.hypothesis.assumptions:
                    content.append(f"- {a}")
            content.append("")

        if self.argument:
            content.append("## Core Argument")
            content.append(f"**Claim:** {self.argument.claim}\n")

            content.append("### Evidence Chain")
            for idx, ev in enumerate(self.argument.evidence):
                content.append(f"#### Evidence {idx+1}")
                content.append(f"- **Description:** {ev.description}")
                content.append(f"- **Type:** {ev.type}")
                content.append(f"- **Confidence:** {ev.confidence}")
                if ev.source:
                    content.append(f"- **Source:** {ev.source}")
                content.append("")

            content.append("### Warrant")
            content.append(f"{self.argument.warrant}\n")

            if self.argument.counterarguments:
                content.append("### Counterarguments")
                for ca in self.argument.counterarguments:
                    if hasattr(ca, 'statement'):
                        content.append(f"- {ca.statement} (Strength: {ca.strength})")
                    else:
                        content.append(f"- {ca}")

            content.append("\n### Reproducibility Checklist")
            checklist = generate_checklist(self.argument)
            for item in checklist:
                content.append(f"- {item}")

        with open(filepath, 'w') as f:
            f.write('\n'.join(content))

    def generate_reproducibility_package(self, directory: str) -> None:
        # Placeholder for directory creation and copying assets
        if not os.path.exists(directory):
            os.makedirs(directory)
        self.export_markdown(os.path.join(directory, "README.md"))
