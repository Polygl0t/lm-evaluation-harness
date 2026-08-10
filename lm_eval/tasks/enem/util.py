# Fixed few-shot exemplars, from
# https://github.com/piresramon/gpt-4-enem/blob/main/lm_eval/tasks/enem.py
# Kept out of the eval split so they are never scored as test questions.
FEWSHOT_IDS = ["2022_21", "2022_88", "2022_143"]


def generate_options(choices):
    options = ""
    for text, label in zip(choices['text'], choices['label']):
        options += f"{label}. {text}\n"
    return options.strip()

def doc_to_text(doc):
    return f"Pergunta:\n{doc['question']}\nAlternativas:\n{generate_options(doc['choices'])}\nResposta correta:"


def doc_to_choice(doc):
    return doc["choices"]["label"]


def process_fewshot_docs(dataset):
    docs_by_id = {doc["id"]: doc for doc in dataset}
    return [docs_by_id[doc_id] for doc_id in FEWSHOT_IDS]


def process_test_docs(dataset):
    return dataset.filter(
        lambda doc: doc["answerKey"] is not None and doc["id"] not in FEWSHOT_IDS
    )
