#!/usr/bin/env python3
"""
Lesson 03 - DeltaM11.3 guard demo (stdlib only)
Simulates a stability score; if below threshold, rollback to safe snapshot.
"""
import random, json

THRESHOLD = 0.78
SAFE_SNAPSHOT = {"output": "Stable baseline response.", "stability": 0.95}

def generate_output():
    stability = round(random.uniform(0.5, 0.98), 3)
    return {"output": "New response candidate", "stability": stability}

def guard_eval(candidate, threshold=THRESHOLD):
    if candidate["stability"] < threshold:
        return {"rolled_back": True, "final": SAFE_SNAPSHOT, "candidate": candidate}
    return {"rolled_back": False, "final": candidate, "candidate": candidate}

def main():
    cand = generate_output()
    result = guard_eval(cand)
    print("Candidate:", json.dumps(cand, indent=2))
    print("Guard result:", json.dumps(result, indent=2))

if __name__ == "__main__":
    main()
