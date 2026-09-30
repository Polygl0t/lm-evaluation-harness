# HellaSwag (German, LeoLM)

## Paper

HellaSwag: Can a Machine Really Finish Your Sentence?
https://arxiv.org/abs/1905.07830

A commonsense natural language inference benchmark built with adversarial filtering. Given
a context, the model picks the most plausible continuation from four candidates.

This variant uses the German columns (`activity_label_de`, `ctx_de`, `endings_de`) of
LeoLM's translation; see [../README.md](../README.md) on translation provenance.

Homepage: https://rowanzellers.com/hellaswag/

Dataset: https://huggingface.co/datasets/LeoLM/HellaSwag_de

## Citation

```
@inproceedings{zellers2019hellaswag,
    title={HellaSwag: Can a Machine Really Finish Your Sentence?},
    author={Zellers, Rowan and Holtzman, Ari and Bisk, Yonatan and Farhadi, Ali and Choi, Yejin},
    booktitle={Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics},
    year={2019}
}
```

### Groups and Tasks

#### Groups

- `leolm`

#### Tasks

- `hellaswag_leolm_de`: named `_leolm_` because `hellaswag_de` is taken by
  [okapi/hellaswag_multilingual](../../okapi/hellaswag_multilingual/README.md).

### Notes

- Preprocessing matches the upstream `hellaswag` task (strip, `[title]` → `. `, drop
  remaining bracketed artifacts, collapse double spaces). Context comes from the translated
  `ctx_de` column rather than being rebuilt from `ctx_a` + `ctx_b`.
- `validation` (10042 docs) is scored; few-shot context comes from `train` (1000 docs).

### Checklist

- [x] Is the task an existing benchmark in the literature?
  - [x] Have you referenced the original paper that introduced the task?
  - [x] If yes, does the original paper provide a reference implementation? If so, have you checked against the reference implementation and documented how to run such a test?
- [x] Is the "Main" variant of this task clearly denoted?
- [x] Have you provided a short sentence in a README on what each new variant adds / evaluates?
- [x] Have you noted which, if any, published evaluation setups are matched by this variant?
