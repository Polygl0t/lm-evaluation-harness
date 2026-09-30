# ARC Challenge (German, LeoLM)

## Paper

Think you have Solved Question Answering? Try ARC, the AI2 Reasoning Challenge
https://arxiv.org/abs/1803.05457

A set of grade-school science questions. The Challenge set contains only questions
answered incorrectly by both a retrieval-based and a word co-occurrence algorithm.

This variant uses the German columns (`question_de`, `choices_de`) of LeoLM's translation;
see [../README.md](../README.md) on translation provenance.

Homepage: https://allenai.org/data/arc

Dataset: https://huggingface.co/datasets/LeoLM/ArcChallenge_de

## Citation

```
@article{Clark2018ThinkYH,
    title={Think you have Solved Question Answering? Try ARC, the AI2 Reasoning Challenge},
    author={Peter Clark and Isaac Cowhey and Oren Etzioni and Tushar Khot and Ashish Sabharwal and Carissa Schoenick and Oyvind Tafjord},
    journal={arXiv:1803.05457v1},
    year={2018}
}
```

### Groups and Tasks

#### Groups

- `leolm`

#### Tasks

- `arc_challenge_de`: cloze-scored over `choices_de`, same prompt format as the upstream
  `arc_challenge` task with `Frage:`/`Antwort:` in place of `Question:`/`Answer:`.

### Notes

- The dataset has no train split: few-shot context comes from `validation` (299 docs),
  `test` (1172 docs) is scored.
- `utils.process_docs_arc_leolm` drops docs whose `answerKey` is absent from
  `choices_de.label` — 22 of 1172 test and 5 of 299 validation docs — so absolute numbers
  are not comparable to variants that keep them.

### Checklist

- [x] Is the task an existing benchmark in the literature?
  - [x] Have you referenced the original paper that introduced the task?
  - [x] If yes, does the original paper provide a reference implementation? If so, have you checked against the reference implementation and documented how to run such a test?
- [x] Is the "Main" variant of this task clearly denoted?
- [x] Have you provided a short sentence in a README on what each new variant adds / evaluates?
- [x] Have you noted which, if any, published evaluation setups are matched by this variant?
