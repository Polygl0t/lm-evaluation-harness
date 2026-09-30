# GermanQuAD

## Paper

GermanQuAD and GermanDPR: Improving Non-English Question Answering and Passage Retrieval
https://arxiv.org/abs/2104.12741

A human-labelled extractive question answering dataset of 13,722 questions in German,
created by deepset and inspired by SQuAD. Unlike the machine-translated German QA sets it
is natively authored over German Wikipedia passages, and its test set is three-way
annotated.

Homepage: https://www.deepset.ai/germanquad

Dataset: https://huggingface.co/datasets/deepset/germanquad

## Citation

```
@misc{möller2021germanquad,
    title={GermanQuAD and GermanDPR: Improving Non-English Question Answering and Passage Retrieval},
    author={Timo Möller and Julian Risch and Malte Pietsch},
    year={2021},
    eprint={2104.12741},
    archivePrefix={arXiv},
    primaryClass={cs.CL}
}
```

### Groups and Tasks

#### Groups

- `german_native`

#### Tasks

- `germanquad`: extractive QA, 3-shot, scored with SQuAD exact-match and token F1.

### Notes

- Prompt format and metrics follow the [xquad](../xquad/README.md) tasks, using
  `xquad_de`'s German wording (`Kontext:` / `Frage:` / `Antwort:`).
- `dataset_kwargs.revision` is pinned to `refs/convert/parquet`: the repo contains only a
  loading script, which `datasets` >= 3 refuses to run.
- `utils.process_results_germanquad` uses `squad_metrics.compute_exact` / `compute_f1`
  (same normalisation as xquad/mlqa's `process_results_qa`) rather than the generic
  `exact_match` metric, which never strips whitespace and so scored 0 for every
  `generate_until` completion.
- The test split has up to three reference answers per question; scoring takes the best
  match. The train split, used for few-shot context, has one.
- `test` (2204 docs) is scored; few-shot context comes from `train` (11518 docs).

### Checklist

- [x] Is the task an existing benchmark in the literature?
  - [x] Have you referenced the original paper that introduced the task?
  - [x] If yes, does the original paper provide a reference implementation? If so, have you checked against the reference implementation and documented how to run such a test?
- [x] Is the "Main" variant of this task clearly denoted?
- [x] Have you provided a short sentence in a README on what each new variant adds / evaluates?
- [x] Have you noted which, if any, published evaluation setups are matched by this variant?
