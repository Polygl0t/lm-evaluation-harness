# One curated fewshot exemplar per exam-question type (max 15), sampled from
# 2010's first exam. Kept out of the eval split so they are never scored as
# test questions; `num_fewshot: 3` are drawn from this pool at random per doc
# (see fewshot_config.sampler: default in the task yamls).
FEWSHOT_IDS = [
    "2010-01_1", "2010-01_11", "2010-01_13", "2010-01_23", "2010-01_26",
    "2010-01_28", "2010-01_38", "2010-01_48", "2010-01_58", "2010-01_68",
    "2010-01_76", "2010-01_83", "2010-01_85", "2010-01_91", "2010-01_99",
]


def generate_options(choices):
    options = ""
    for text, label in zip(choices['text'], choices['label']):
        options += f"{label}. {text}\n"
    return options.strip()

def doc_to_text(doc):
    return f"Questão:\n{doc['question']}\nAlternativas:\n{generate_options(doc['choices'])}\nResposta correta:"


def doc_to_choice(doc):
    # OAB questions always have 4 alternatives, but reading the labels from
    # the doc itself (instead of hardcoding ["A", "B", "C", "D"]) is safer.
    return doc["choices"]["label"]


def process_fewshot_docs(dataset):
    return dataset.filter(lambda doc: doc["id"] in FEWSHOT_IDS)


def process_test_docs(dataset):
    return dataset.filter(
        lambda doc: doc["answerKey"] is not None and doc["id"] not in FEWSHOT_IDS
    )
