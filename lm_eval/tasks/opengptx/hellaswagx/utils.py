import re

import datasets


def _preprocess_hellaswag(text: str) -> str:
    text = text.strip()
    text = text.replace(" [title]", ". ")
    text = re.sub(r"\[.*?\]", "", text)
    text = text.replace("  ", " ")
    return text


def process_docs_hellaswag(dataset: datasets.Dataset) -> datasets.Dataset:
    """Standard openGPT-X columns: activity_label / ctx_a / ctx_b / endings."""
    def _process(doc):
        ctx = doc["ctx_a"] + " " + doc["ctx_b"].capitalize()
        return {
            "query": _preprocess_hellaswag(doc["activity_label"] + ": " + ctx),
            "choices": [_preprocess_hellaswag(e) for e in doc["endings"]],
            "gold": int(doc["label"]),
        }
    return dataset.map(_process)
