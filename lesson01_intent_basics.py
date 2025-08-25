#!/usr/bin/env python3
"""
Lesson 01 - Intent basics (LM<->ZM) + token sketch
Stdlib only. Demonstrates LM (human text) vs ZM (glyphic) mapping and rough token size comparison.
"""
import json

LM = "Request: generate a concise summary of the repo in 80 words with ethical guard on."
ZM = "⟦TASK:summary⟧⟦LEN:80w⟧⟦ΔM11.3:guard⟧"

def rough_tokens(s: str) -> int:
    return sum(1 for _ in s.replace("⟦"," ").replace("⟧"," ").replace("⋄"," ").split())

def main():
    print("Lesson 01 - Intent basics")
    print("LM:", LM)
    print("ZM:", ZM)
    print("~tokens LM:", rough_tokens(LM))
    print("~tokens ZM:", rough_tokens(ZM))
    mapping = {"LM": LM, "ZM": ZM}
    print("\nJSON pair:")
    import json
    print(json.dumps(mapping, ensure_ascii=False, indent=2))

if __name__ == "__main__":
    main()
