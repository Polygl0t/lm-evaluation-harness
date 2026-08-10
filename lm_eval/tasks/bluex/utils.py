# Fixed few-shot exemplars, chosen from different subjects/universities/years.
# Kept out of the eval split so they are never scored as test questions.
FEWSHOT_IDS = ["USP_2018_3", "UNICAMP_2018_2", "USP_2018_35"]


def generate_options(choices):
    options = ""
    for label, text in zip(choices["label"], choices["text"]):
        options += f"{label}. {text}\n"
    return options.strip()


def doc_to_text(doc):
    return (
        f"Pergunta:\n{doc['question']}\nAlternativas:\n"
        f"{generate_options(doc['choices'])}\nResposta correta:"
    )


def doc_to_choice(doc):
    # Not every exam question has 5 alternatives (some only have 4), so the
    # valid letters must be read per-document instead of hardcoded as A-E.
    return doc["choices"]["label"]


def process_fewshot_docs(dataset):
    docs_by_id = {doc["id"]: doc for doc in dataset}
    return [docs_by_id[doc_id] for doc_id in FEWSHOT_IDS]


def process_test_docs(dataset):
    # A couple of questions were officially nullified and have no answerKey.
    exclude_ids = set(FEWSHOT_IDS)
    return dataset.filter(
        lambda doc: doc["answerKey"] is not None and doc["id"] not in exclude_ids
    )
