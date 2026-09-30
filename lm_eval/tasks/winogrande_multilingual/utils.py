from __future__ import annotations


def doc_to_text_winogrande(doc) -> int:
    """WinoGrande cloze format: return label index (0 or 1) as the 'text'."""
    return int(str(doc["answer"])) - 1


def doc_to_target_winogrande(doc) -> str:
    """Return the part of the sentence after the blank (shared suffix)."""
    idx = doc["sentence"].index("_") + 1
    return doc["sentence"][idx:].strip()


def doc_to_choice_winogrande(doc) -> list[str]:
    """Return full sentences with each option substituted for the blank."""
    idx = doc["sentence"].index("_")
    prefix = doc["sentence"][:idx]
    return [prefix + doc["option1"], prefix + doc["option2"]]
