# German Language Proficiency

## Paper

No accompanying paper; an original release by ellamind.

Tests German grammar, orthography and usage through minimal pairs: each item gives a
context and endings that differ only in the phenomenon under test, and the model picks the
well-formed one. Items cover 22 phenomena spanning targeted error types (adjective endings,
article case and gender, `das`/`dass`, `seit`/`seid`, `ß`/`ss`, n-declension, Konjunktiv,
verb conjugation, subordinate-clause and V2 word order, capitalization, punctuation,
pronoun case, perfect auxiliary, `als`/`wie`, register) and broader fluency judgements
(collocation, connectives, discourse, naturalness, prose quality).

Dataset: https://huggingface.co/datasets/ellamind/german-language-proficiency

## Citation

```
@misc{ellamind_german_language_proficiency,
    title  = {German Language Proficiency},
    author = {ellamind},
    year   = {2026},
    howpublished = {\url{https://huggingface.co/datasets/ellamind/german-language-proficiency}}
}
```

### Groups and Tasks

#### Groups

- `ellamind`

#### Tasks

- `german_language_proficiency`: aggregate over all 22 phenomena (the `all` config, 7283
  docs), scored as multiple choice over `endings`.

### Notes

- The dataset's `all` config is the default, so no `dataset_name` is needed.
- No held-out split: the dataset ships only `train`, used as both the evaluation set and
  the few-shot pool. `num_fewshot` is pinned to 0; do not raise it without also setting a
  disjoint `fewshot_split`.
- Per-phenomenon configs (`dass_das_error`, `word_order_v2_error`, …) exist on the Hub but
  are not registered as tasks. The `error_type` / `error_category` columns allow slicing
  the aggregate run.

### Checklist

- [x] Is the task an existing benchmark in the literature?
  - [ ] Have you referenced the original paper that introduced the task? (none exists)
  - [ ] If yes, does the original paper provide a reference implementation? If so, have you checked against the reference implementation and documented how to run such a test?
- [x] Is the "Main" variant of this task clearly denoted?
- [x] Have you provided a short sentence in a README on what each new variant adds / evaluates?
- [x] Have you noted which, if any, published evaluation setups are matched by this variant?
