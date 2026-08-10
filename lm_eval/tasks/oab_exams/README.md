# OAB Exams

## Paper

Title: `Passing the Brazilian OAB Exam: Data Preparation and Some Experiments`

Abstract: `https://arxiv.org/abs/1712.05128`

OAB Exams is a dataset of more than 2,000 questions from the Brazilian Bar Association's (Ordem dos Advogados do Brasil) exams, from 2010 to 2018.

This task evaluates models on the multiple-choice questions from these exams. The model is given a question in Portuguese together with its answer choices and must respond with the correct alternative letter (`A`, `B`, `C` or `D`), evaluated in a 3-shot setting.

Two variants are provided:

* `oab_exams_cloze` scores the answer via loglikelihood comparison of each answer letter (`output_type: multiple_choice`). This requires access to the model's logits (not available for most API-only models).
* `oab_exams_generative` instead lets the model freely generate an answer (`output_type: generate_until`) and extracts the answer letter with a regex filter. Use this variant for models that only expose generated text, e.g. most API-only models.

Data sources: [[1]](https://huggingface.co/datasets/eduagarcia/oab_exams) [[2]](https://github.com/legal-nlp/oab-exams)

Homepage: `https://github.com/legal-nlp/oab-exams`

### Citation

```text
@inproceedings{d2017passing,
  title={Passing the Brazilian OAB Exam: Data Preparation and Some Experiments},
  author={Delfino, Pedro and Cuconato, Bruno and Haeusler, Edward Hermann and Rademaker, Alexandre},
  booktitle={Legal Knowledge and Information Systems: JURIX 2017: The Thirtieth Annual Conference},
  volume={302},
  pages={89},
  year={2017},
  organization={IOS Press}
}
```

### Groups, Tags, and Tasks

#### Tasks

* `oab_exams_cloze`: Multiple-choice questions from the Brazilian OAB entrance exams (2010–2018), scored via loglikelihood over the answer choices.
* `oab_exams_generative`: Same dataset and prompt as `oab_exams_cloze`, but the answer is free-form generated text with the answer letter recovered via regex, for use with models where logits are unavailable.

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

* `v1.0` — Initial port of the OAB Exams task from the [lm-evaluation-harness-pt](https://github.com/eduagarcia/lm-evaluation-harness-pt) fork (maintained by Eduardo Garcia) to the current lm-evaluation-harness.
  * Reworked the task to use APIs available in the current upstream `lm-evaluation-harness` (the fork relied on a custom `id_sampler` fewshot sampler and custom `normalize_spaces`/`remove_accents`/`find_choices` filters, plus a `group_by` filter option, none of which exist upstream):
  * Added `oab_exams_cloze`, an `output_type: multiple_choice` variant. The model's choice is scored directly via loglikelihood comparison of each answer letter, which is both more robust (no dependence on the model formatting its answer as instructed) and the convention used by comparable tasks. `doc_to_choice` reads the valid letters per-question instead of hardcoding `["A", "B", "C", "D"]`.
  * Replaced the custom `id_sampler`/`sampler_config.id_list` fewshot mechanism (not present upstream) with `fewshot_config.process_docs`, restricting the fewshot pool to the same 15 curated exemplars used by the fork (one per exam-question type, from the 2010 exam), combined with the built-in `default` (random, seeded) sampler to draw `num_fewshot: 3` of them per document.
  * Added `process_docs` on the test split to drop the fewshot exemplar pool from evaluation, and to defensively filter out any question missing an `answerKey`.
  * Fixed the `acc` metric's `aggregation` field, which was set to `acc` in the fork (not a valid aggregation function upstream); it is now `mean`, as used by every other `acc` metric in this repo.
  * Added `oab_exams_generative`, a `generate_until` variant of the task for models that can't be scored via loglikelihood (e.g. most API-only models). It reuses the same dataset, prompt, and fewshot setup as `oab_exams_cloze`; the answer letter is recovered from the generated text with a `strict-match`/`flexible-extract` regex filter pair (replacing the fork's `normalize_spaces`/`remove_accents`/`find_choices` chain):
    * `strict-match` expects the letter right at the start of the completion, since the shared prompt already ends in "Resposta correta:".
    * `flexible-extract` is a fallback that scans the whole completion and takes the last `A`-`D` letter found, in case the model reasons before stating its final answer.

