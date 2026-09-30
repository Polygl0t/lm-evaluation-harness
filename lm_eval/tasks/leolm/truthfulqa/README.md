# TruthfulQA (German, LeoLM)

## Paper

TruthfulQA: Measuring How Models Mimic Human Falsehoods
https://arxiv.org/abs/2109.07958

Measures whether a language model is truthful in generating answers to questions crafted so
that some humans would answer falsely due to a misconception.

This variant uses the German columns (`question_de`, `mc1_targets_de`, `mc2_targets_de`) of
LeoLM's translation; see [../README.md](../README.md) on translation provenance.

Homepage: https://github.com/sylinrl/TruthfulQA

Dataset: https://huggingface.co/datasets/LeoLM/TruthfulQA_de

## Citation

```
@inproceedings{lin-etal-2022-truthfulqa,
    title = "{T}ruthful{QA}: Measuring How Models Mimic Human Falsehoods",
    author = "Lin, Stephanie and Hilton, Jacob and Evans, Owain",
    booktitle = "Proceedings of the 60th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)",
    month = may,
    year = "2022",
    address = "Dublin, Ireland",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2022.acl-long.229",
    doi = "10.18653/v1/2022.acl-long.229",
    pages = "3214--3252",
}
```

### Groups and Tasks

#### Groups

- `leolm`

#### Tasks

- `truthfulqa_leolm_de_mc1`: multiple choice, one correct answer, scored as accuracy.
- `truthfulqa_leolm_de_mc2`: multiple choice, several answers may be true, scored as the
  normalised probability mass on all true answers.

Both share one `process_docs` and the same prompt. Named `_leolm_` because
`truthfulqa_de_mc1` is taken by
[okapi/truthfulqa_multilingual](../../okapi/truthfulqa_multilingual/README.md).

### Notes

- Matches the upstream `truthfulqa_mc1` / `truthfulqa_mc2` setup: the same 6-shot QA primer
  is prepended to every question, translated to German.
- Validation-only dataset (817 docs), so `num_fewshot` is pinned to 0.
- mc1 gold is resolved as `mc1_targets_de["labels"].index(1)`, which is 0 for all 817 docs,
  i.e. equivalent to the upstream `doc_to_target: 0`.
- mc2 items have 4–9 choices with 1–6 true. A model with no preference scores ≈0.448 here
  (the mean of `n_true / n_choices`), against ≈0.40 for the English original — treat ~0.45
  as the no-signal baseline.
- No `_gen` variant: `LeoLM/TruthfulQA_de` has no `correct_answers` / `incorrect_answers`
  columns, which upstream `truthfulqa_gen` requires from the `generation` config.

### Checklist

- [x] Is the task an existing benchmark in the literature?
  - [x] Have you referenced the original paper that introduced the task?
  - [x] If yes, does the original paper provide a reference implementation? If so, have you checked against the reference implementation and documented how to run such a test?
- [x] Is the "Main" variant of this task clearly denoted?
- [x] Have you provided a short sentence in a README on what each new variant adds / evaluates?
- [x] Have you noted which, if any, published evaluation setups are matched by this variant?
