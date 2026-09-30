import datasets


def process_docs_arc_leolm(dataset: datasets.Dataset) -> datasets.Dataset:
    """Drop 5-choice questions (answerKey='E') — templates only support A–D."""
    return dataset.filter(lambda x: x["answerKey"] in x["choices_de"]["label"])
