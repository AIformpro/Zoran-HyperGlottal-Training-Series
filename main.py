#!/usr/bin/env python3
"""
Zoran - HyperGlottal Training Series launcher (stdlib only)
"""
import sys, importlib

LESSONS = {
    "1": "lessons.lesson01_intent_basics",
    "3": "lessons.lesson03_guard_deltaM",
}

def run_lesson(idx: str):
    modname = LESSONS.get(idx)
    if not modname:
        print("Lesson not found. Available:", ", ".join(sorted(LESSONS)))
        return
    mod = importlib.import_module(modname)
    if hasattr(mod, "main"):
        mod.main()
    else:
        print(f"Module {modname} has no main()")

def main():
    print("Zoran - HyperGlottal Training Series")
    print("Available lessons:", ", ".join(sorted(LESSONS)))
    if len(sys.argv) > 1:
        run_lesson(sys.argv[1])
    else:
        print("Usage: python main.py <lesson_number>")
        print("Example: python main.py 1")

if __name__ == "__main__":
    main()
