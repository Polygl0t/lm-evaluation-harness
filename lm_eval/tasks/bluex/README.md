# BLUEX

## Paper

Title: `BLUEX: A benchmark based on Brazilian Leading Universities Entrance eXams`

Abstract: `https://arxiv.org/abs/2307.05410`

BLUEX is a multimodal dataset consisting of the two leading university entrance exams conducted in Brazil: Convest (Unicamp) and Fuvest (USP), spanning from 2018 to 2024. The benchmark comprises 724 questions that do not have accompanying images.

This task evaluates models on the multiple-choice questions from these exams. The model is given a question in Portuguese together with its answer choices and must respond with the correct alternative letter (`A`, `B`, `C`, `D` or `E`), evaluated in a 3-shot setting.

Two variants are provided:

* `bluex_cloze` scores the answer via loglikelihood comparison of each answer letter (`output_type: multiple_choice`). This requires access to the model's logits (not available for most API-only models).
* `bluex_generative` instead lets the model freely generate an answer (`output_type: generate_until`) and extracts the answer letter with a regex filter. Use this variant for models that only expose generated text, e.g. most API-only models.

Homepage: `https://github.com/portuguese-benchmark-datasets/bluex`

### Citation

```text
@misc{almeida2023bluex,
  title={BLUEX: A benchmark based on Brazilian Leading Universities Entrance eXams},
  author={Thales Sales Almeida and Thiago Laitz and Giovana K. Bonás and Rodrigo Nogueira},
  year={2023},
  eprint={2307.05410},
  archivePrefix={arXiv},
  primaryClass={cs.CL}
}
```

### Groups, Tags, and Tasks

#### Tasks

* `bluex_cloze`: Reading-comprehension / multiple-choice questions from the Convest (Unicamp) and Fuvest (USP) Brazilian university entrance exams (2018–2024), scored via loglikelihood over the answer choices.
* `bluex_generative`: Same dataset and prompt as `bluex`, but the answer is free-form generated text with the answer letter recovered via regex, for use with models where logits are unavailable.

### Checklist

For adding novel benchmarks/datasets to the library:

* [x] Is the task an existing benchmark in the literature?
  * [x] Have you referenced the original paper that introduced the task?
  * [ ] If yes, does the original paper provide a reference implementation? If so, have you checked against the reference implementation and documented how to run such a test?

If other tasks on this dataset are already supported:

* [ ] Is the "Main" variant of this task clearly denoted?
* [ ] Have you provided a short sentence in a README on what each new variant adds / evaluates?
* [ ] Have you noted which, if any, published evaluation setups are matched by this variant?

### Changelog

* `v1.0` — Initial port of the BLUEX task from the [lm-evaluation-harness-pt](https://github.com/eduagarcia/lm-evaluation-harness-pt) fork (maintained by Eduardo Garcia) to the current lm-evaluation-harness.
  * Reworked the task to use APIs available in the current upstream `lm-evaluation-harness` (the fork relied on a custom `id_sampler` fewshot sampler and custom `normalize_spaces`/`remove_accents`/`find_choices` filters that no longer exist upstream):
  * Switched `output_type` from `generate_until` (with a chain of regexes to recover the answer letter from free-form text) to `multiple_choice`. The model's choice is now scored directly via loglikelihood comparison of each answer letter (see `bluex_cloze.yaml`), which is both more robust (no dependence on the model formatting its answer as instructed) and the convention used by comparable tasks. `doc_to_choice` reads the valid letters per-question since not every exam question has 5 alternatives (some only have 4).
  * Replaced the custom `id_sampler`/`sampler_config.id_list` fewshot mechanism (not present upstream) with `fewshot_config.process_docs`, restricting the fewshot pool to 3 fixed, curated exemplars (`USP_2018_3`, `UNICAMP_2018_2`, `USP_2018_35`) spanning both universities, combined with the built-in `first_n` sampler for deterministic, reproducible fewshot selection.
  * Added `process_docs` on the test split to drop the fewshot exemplars from evaluation and to filter out 2 questions that were officially nullified and have no `answerKey`.
  * Added `bluex_generative`, a `generate_until` variant of the task for models that can't be scored via loglikelihood (e.g. most API-only models). It reuses the same dataset, prompt, and fewshot setup as `bluex`; the answer letter is recovered from the generated text with a `strict-match`/`flexible-extract` regex filter pair:
    * `strict-match` expects the letter right at the start of the completion, since the shared prompt already ends in "Resposta correta:".
    * `flexible-extract` is a fallback that scans the whole completion and takes the last `A`-`E` letter found, in case the model reasons before stating its final answer.
