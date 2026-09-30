# MMLU (German, LeoLM)

## Paper

Measuring Massive Multitask Language Understanding
https://arxiv.org/abs/2009.03300

A multiple-choice benchmark covering 57 subjects across STEM, the humanities, the social
sciences and other areas, ranging from elementary to advanced professional difficulty.

This variant uses the German columns (`question_de`, `choices_de`) of LeoLM's translation;
see [../README.md](../README.md) on translation provenance.

Homepage: https://github.com/hendrycks/test

Dataset: https://huggingface.co/datasets/LeoLM/MMLU_de

## Citation

```
@article{hendryckstest2021,
    title={Measuring Massive Multitask Language Understanding},
    author={Dan Hendrycks and Collin Burns and Steven Basart and Andy Zou and Mantas Mazeika and Dawn Song and Jacob Steinhardt},
    journal={Proceedings of the International Conference on Learning Representations (ICLR)},
    year={2021}
}
```

### Groups and Tasks

#### Groups

- `leolm`

#### Tasks

- `mmlu_de`: single aggregate task, cloze-scored over `choices_de`.

### Notes

- **Not comparable to published MMLU scores.** The prompt is cloze-style
  (`Frage:`/`Antwort:` with the answer texts as choices), not MMLU's lettered `A./B./C./D.`
  format with a per-subject `description:`. Use [global_mmlu](../../global_mmlu/README.md)
  or [opengptx/mmlux](../../opengptx/mmlux/) for the standard setup.
- Single flat task with no `subject` column, so no per-subject or category rollups.
- **Row count depends on the installed `datasets` version.** `LeoLM/MMLU_de` ships a
  loading script plus `data/*.parquet` and `val/*.parquet`. `datasets` < 3 runs the script;
  `datasets` >= 3 refuses and falls back to the repo's `refs/convert/parquet` export, which
  holds only a 755-row `default/validation`. Check the reported `n-samples`.
- No separate few-shot split: few-shot context is drawn from the split being scored.

### Checklist

- [x] Is the task an existing benchmark in the literature?
  - [x] Have you referenced the original paper that introduced the task?
  - [x] If yes, does the original paper provide a reference implementation? If so, have you checked against the reference implementation and documented how to run such a test?
- [x] Is the "Main" variant of this task clearly denoted?
- [x] Have you provided a short sentence in a README on what each new variant adds / evaluates?
- [x] Have you noted which, if any, published evaluation setups are matched by this variant?
