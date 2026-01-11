from typing import List
from ida.core.argument import Argument

def generate_checklist(argument: Argument) -> List[str]:
    checklist = []

    # 1. Evidence Verification
    if argument.evidence:
        for idx, ev in enumerate(argument.evidence):
            checklist.append(f"[ ] Verify source availability for Evidence #{idx+1}: {ev.source or 'No source listed'}")
            checklist.append(f"[ ] Audit data processing steps for Evidence #{idx+1}")
    else:
        checklist.append("[!] No evidence provided to verify")

    # 2. Argumentation Logic
    checklist.append(f"[ ] Verify warrant logic: {argument.warrant[:50]}..." if argument.warrant else "[!] Missing Warrant")

    # 3. Limitations
    if argument.limitations:
        checklist.append("[ ] Confirm all listed limitations are addressed in discussion")
    else:
        checklist.append("[!] No limitations disclosed")

    return checklist
