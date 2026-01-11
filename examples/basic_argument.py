import sys
import os

# Ensure src is in path for example execution
sys.path.append(os.path.join(os.path.dirname(__file__), '../src'))

from ida.core.argument import Argument
from ida.core.evidence import Evidence
from ida.validation.validator import Validator

def main():
    print("--- IDA Framework Basic Example ---\n")

    # 1. Create a structured argument
    arg = Argument(
        claim="Fine-tuning LLMs on domain data improves task accuracy by 15%",
        evidence=[
            Evidence(
                type="experimental",
                description="Controlled A/B test on 10k samples",
                source="experiments/finetune_results.csv",
                confidence=0.95
            )
        ],
        warrant="Consistent improvement across 5 different domains and 3 model sizes",
        counterarguments=[
            "Improvement may be due to overfitting",
            "Sample size may be insufficient for generalization"
        ],
        limitations=[
            "Limited to English language",
            "Tested only on classification tasks"
        ]
    )
    print(f"Created Argument: '{arg.claim}'")

    # 2. Validate argument structure
    validator = Validator()
    results = validator.validate(arg)

    print(f"\nValidation Results:")
    print(f"Argument Quality Score: {results.quality_score}/100")
    print(f"Evidence Strength: {results.evidence_strength}")
    print(f"Missing Elements: {results.missing_elements}")

    assert results.quality_score == 100.0
    print("\n[SUCCESS] Example executed successfully.")

if __name__ == "__main__":
    main()
