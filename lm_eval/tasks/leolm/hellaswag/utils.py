import re

import datasets


def _preprocess_hellaswag(text: str) -> str:
    text = text.strip()
    text = text.replace(" [title]", ". ")
    text = re.sub(r"\[.*?\]", "", text)
    text = text.replace("  ", " ")
    return text


def process_docs_hellaswag_leolm(dataset: datasets.Dataset) -> datasets.Dataset:
    """LeoLM columns: activity_label_de / ctx_de / endings_de; label is str."""
    def _process(doc):
        return {
            "query": _preprocess_hellaswag(doc["activity_label_de"] + ": " + doc["ctx_de"]),
            "choices": [_preprocess_hellaswag(e) for e in doc["endings_de"]],
            "gold": int(doc["label"]),
        }
    return dataset.map(_process)
