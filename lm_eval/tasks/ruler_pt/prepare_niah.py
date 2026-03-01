# Copyright (c) 2024, NVIDIA CORPORATION.  All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License


import os
import random
import re
import uuid
from functools import lru_cache, cache
from typing import List, Union, Literal
import requests

import numpy as np
from packaging.version import parse as parse_version
from importlib.metadata import version
from lm_eval.tasks.ruler_pt.common_utils import SUBSTANTIVOS, ADJETIVOS, VERBOS

from tqdm import tqdm

try:
    import nltk
    from nltk import sent_tokenize
except ImportError:
    raise ImportError(
        'Please install the `nltk` package to run this script. You can install it with `pip install lm_eval["ruler"]` or `pip install nltk`.'
    )


NUM_SAMPLES = 500
REMOVE_NEWLINE_TAB = ""
STOP_WORDS = ""
RANDOM_SEED = 42
# Define Needle/Haystack Format
NEDDLE = "Um {type_needle_v} especial para {key} é: {value}."

# Portuguese translations for needle types (singular, plural, grammatical gender)
TYPE_NEEDLE_PT = {
    "numbers": {"singular": "número",      "plural": "números",      "gender": "m"},
    "words":   {"singular": "palavra",      "plural": "palavras",     "gender": "f"},
    "uuids":   {"singular": "código UUID",  "plural": "códigos UUID", "gender": "m"},
}

nouns = SUBSTANTIVOS
adjs = ADJETIVOS
verbs = VERBOS
words = [f"{adj}-{noun}" for adj in adjs for noun in nouns]
WORDS = sorted(list(set(words)))

# Positions
DEPTHS = list(np.round(np.linspace(0, 100, num=40, endpoint=True)).astype(int))

NLTK_MIN_VERSION = "3.9.1"
RANK = os.environ.get("LOCAL_RANK", "0")


@lru_cache(maxsize=1024)
def cached_sent_tokenize(text: str) -> List[str]:
    return sent_tokenize(text, language='portuguese')


def download_nltk_resources():
    """Download 'punkt' if not already installed"""
    assert (nltk_version := parse_version(version("nltk"))) >= parse_version(
        NLTK_MIN_VERSION
    ), (
        f"`nltk` version {nltk_version} is not >= {NLTK_MIN_VERSION}. Please update `nltk` before proceeding--older versions are vulnerable to a remote code execution vulnerability."
    )

    try:
        nltk.data.find("tokenizers/punkt_tab")
    except LookupError:
        if RANK == "0":
            nltk.download("punkt_tab")
            print("Downloaded punkt_tab on rank 0")


download_nltk_resources()


def generate_random_number(num_digits=7) -> str:
    lower_bound = 10 ** (num_digits - 1)
    upper_bound = 10**num_digits - 1
    return str(random.randint(lower_bound, upper_bound))


def generate_random_word() -> str:
    word = random.choice(WORDS)
    return word


def generate_random_uuid() -> str:
    return str(uuid.UUID(int=random.getrandbits(128), version=4))


def generate_random(type_needle: str) -> str:
    if type_needle == "numbers":
        return generate_random_number()
    elif type_needle == "words":
        return generate_random_word()
    elif type_needle == "uuids":
        return generate_random_uuid()
    else:
        raise NotImplementedError(f"{type_needle} is not implemented.")


def generate_input_output(
    num_haystack: int,
    haystack: Union[list[str], str],
    *,
    type_haystack: str,
    num_needle_k: int,
    type_needle_k: str,
    num_needle_v: int,
    type_needle_v: str,
    template: str,
    num_needle_q: int = 1,
    random_seed: int = RANDOM_SEED,
) -> tuple[str, list[str], str]:
    pt_info        = TYPE_NEEDLE_PT.get(type_needle_v, {"singular": type_needle_v, "plural": type_needle_v, "gender": "m"})
    pt_singular    = pt_info["singular"]
    pt_plural      = pt_info["plural"]
    pt_gender      = pt_info["gender"]
    needle_article = "Uma" if pt_gender == "f" else "Um"
    NEEDLE = f"{needle_article} {{type_needle_v}} especial para {{key}} é: {{value}}."
    keys, values, needles = [], [], []
    for _ in range(num_needle_k):
        keys.append(generate_random(type_needle_k))
        value = []
        for _ in range(num_needle_v):
            value.append(generate_random(type_needle_v))
            needles.append(
                NEEDLE.format(
                    type_needle_v=pt_singular,
                    key=keys[-1],
                    value=value[-1],
                )
            )
        values.append(value)

    random.Random(random_seed).shuffle(needles)

    # Context
    if type_haystack == "essay":
        assert isinstance(haystack, list)
        text = " ".join(haystack[:num_haystack])
        document_sents = cached_sent_tokenize(text.strip())
        insertion_positions = (
            [0]
            + sorted(
                [
                    int(len(document_sents) * (depth / 100))
                    for depth in random.sample(DEPTHS, len(needles))
                ]
            )
            + [len(document_sents)]
        )
        document_sents_list = []
        for i in range(1, len(insertion_positions)):
            last_pos = insertion_positions[i - 1]
            next_pos = insertion_positions[i]
            document_sents_list.append(" ".join(document_sents[last_pos:next_pos]))
            if i - 1 < len(needles):
                document_sents_list.append(needles[i - 1])
        context = " ".join(document_sents_list)

    else:
        if type_haystack == "repeat":
            sentences = [haystack] * num_haystack
        elif type_haystack == "needle":
            sentences = [
                haystack.format(
                    article=needle_article,
                    type_needle_v=pt_singular,
                    key=generate_random(type_needle_k),
                    value=generate_random(type_needle_v),
                )
                for _ in range(num_haystack)
            ]

        indexes = sorted(random.sample(range(num_haystack), len(needles)), reverse=True)
        for index, element in zip(indexes, needles):
            sentences.insert(index, element)
        context = "\n".join(sentences)

    ## Query and Answer
    indices = random.sample(range(num_needle_k), num_needle_q)
    queries = [keys[i] for i in indices]
    answers = [a for i in indices for a in values[i]]
    query = (
        ", ".join(queries[:-1]) + " e " + queries[-1]
        if len(queries) > 1
        else queries[0]
    )

    template = template
    type_needle_v = type_needle_v
    if num_needle_q * num_needle_v == 1:
        # Singular form – gender-aware replacements
        art_indef_s = "Uma" if pt_gender == "f" else "Um"
        pro_obj_s   = "a"   if pt_gender == "f" else "o"
        pro_s       = "ela" if pt_gender == "f" else "ele"
        hidden_s    = "está escondida"  if pt_gender == "f" else "está escondido"
        mentioned_s = "mencionada"      if pt_gender == "f" else "mencionado"
        art_def_s   = "a"              if pt_gender == "f" else "o"
        template = template.replace(
            "Alguns {type_needle_v} especiais estão escondidos",
            f"{art_indef_s} {{type_needle_v}} especial {hidden_s}",
        )
        template = template.replace("Memorize-os", f"Memorize-{pro_obj_s}")
        template = template.replace("sobre eles", f"sobre {pro_s}")
        template = template.replace(
            "Quais são todos os {type_needle_v} especiais",
            f"Qual é {art_def_s} {{type_needle_v}} especial",
        )
        template = template.replace("mencionados", mentioned_s)
        type_needle_v_pt = pt_singular
    else:
        # Plural form – gender agreement for feminine types
        if pt_gender == "f":
            template = template.replace("Alguns {type_needle_v}", "Algumas {type_needle_v}")
            template = template.replace("estão escondidos", "estão escondidas")
            template = template.replace("Memorize-os", "Memorize-as")
            template = template.replace("sobre eles", "sobre elas")
            template = template.replace("todos os {type_needle_v}", "todas as {type_needle_v}")
            template = template.replace("mencionados", "mencionadas")
        type_needle_v_pt = pt_plural

    input_text = template.format(
        type_needle_v=type_needle_v_pt,
        context=context,
        query=query,
    )

    return input_text, answers, query


def generate_samples(
    haystack,
    TOKENIZER=None,
    *,
    max_seq_length: int,
    type_haystack: str,
    type_needle_k: str,
    type_needle_v: str,
    template: str,
    num_samples: int = 500,
    tokens_to_generate: int = 128,
    num_needle_v: int = 1,
    num_needle_k: int = 1,
    num_needle_q=1,
    incremental: int = 500,
    remove_newline_tab: bool = False,
    random_seed: int = 42,
) -> list[dict]:
    assert TOKENIZER is not None, "TOKENIZER is not defined."
    num_needle_k = max(num_needle_k, num_needle_q)
    pt_info = TYPE_NEEDLE_PT.get(type_needle_v, {"singular": type_needle_v, "plural": type_needle_v, "gender": "m"})
    write_jsons = []
    tokens_to_generate = tokens_to_generate

    if type_haystack == "essay":
        incremental = 500
    elif type_haystack == "repeat":
        incremental = 25
    elif type_haystack == "needle":
        incremental = 25

    if type_haystack != "essay" and max_seq_length < 4096:
        incremental = 5

    num_haystack = incremental

    total_tokens = 0  # Track the total tokens generated for the first example
    while total_tokens + tokens_to_generate < max_seq_length:
        input_text, answer, query = generate_input_output(
            num_haystack,
            haystack,
            type_haystack=type_haystack,
            num_needle_k=num_needle_k,
            type_needle_k=type_needle_k,
            num_needle_v=num_needle_v,
            type_needle_v=type_needle_v,
            template=template,
            num_needle_q=num_needle_q,
            random_seed=random_seed,
        )
        # Calculate the number of tokens in the example
        total_tokens = len(TOKENIZER(input_text + " ".join(answer)).input_ids)
        if total_tokens + tokens_to_generate > max_seq_length:
            num_haystack -= incremental
            break

        if type_haystack == "essay" and num_haystack > len(haystack):
            num_haystack = len(haystack)
            break

        num_haystack += incremental

    # print("Num haystack:", num_haystack)

    # Generate samples
    for index in tqdm(
        range(num_samples),
        desc=f"Generating synthetic samples: {type_haystack} | {max_seq_length}",
    ):
        used_haystack = num_haystack
        while True:
            try:
                input_text, answer, query = generate_input_output(
                    used_haystack,
                    haystack,
                    type_haystack=type_haystack,
                    num_needle_k=num_needle_k,
                    type_needle_k=type_needle_k,
                    num_needle_v=num_needle_v,
                    type_needle_v=type_needle_v,
                    template=template,
                    num_needle_q=num_needle_q,
                    random_seed=random_seed,
                )
                length = len(TOKENIZER(input_text).input_ids) + tokens_to_generate
                assert length <= max_seq_length, f"{length} exceeds max_seq_length."
                break
                # ruff: noqa
            except:
                if used_haystack > incremental:
                    used_haystack -= incremental

        if remove_newline_tab:
            input_text = " ".join(
                input_text.replace("\n", " ").replace("\t", " ").strip().split()
            )

        formatted_output = {
            "index": index,
            "input": input_text,
            "outputs": answer,
            "length": length,
            "max_length": max_seq_length,
            "gen_prefix": (
                f"{'A' if pt_info['gender'] == 'f' else 'O'} {pt_info['singular']} especial para {query} "
                f"{'mencionada' if pt_info['gender'] == 'f' else 'mencionado'} no texto fornecido é"
                if num_needle_q * num_needle_v == 1 else
                f"{'As' if pt_info['gender'] == 'f' else 'Os'} {pt_info['plural']} especiais para {query} "
                f"{'mencionadas' if pt_info['gender'] == 'f' else 'mencionados'} no texto fornecido são"
            ),
        }
        if formatted_output["outputs"][0] not in formatted_output["input"]:
            assert False, (
                f"Needle not in input: {formatted_output}. Something went wrong."
            )
        write_jsons.append(formatted_output)
    return write_jsons

@cache
def get_haystack(
    type_haystack: Literal["essay", "repeat", "needle"],
) -> Union[list[str], str]:
    
    NEEDLE = "{article} {type_needle_v} especial para {key} é: {value}."
    if type_haystack == "essay":
        #HAYSTACK_URL = "https://raw.githubusercontent.com/mungg/OneRuler/refs/heads/main/OneRuler/data/books/pt/the_book_of_disquietude_pt.txt"
        HAYSTACK_URL = "https://raw.githubusercontent.com/Nkluge-correa/long-pt-docs/refs/heads/main/docs/000021.txt"

        response = requests.get(HAYSTACK_URL)
        response.raise_for_status()
        essay = response.text
        haystack = re.sub(r"\s+", " ", essay).split(" ")
    elif type_haystack == "repeat":
        haystack = "A grama é verde. O céu é azul. O sol é amarelo. Lá vamos nós. De ida e volta."
    elif type_haystack == "needle":
        haystack = NEEDLE
    else:
        raise NotImplementedError(f"{type_haystack} is not implemented.")
    return haystack
