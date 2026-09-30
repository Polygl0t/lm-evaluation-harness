# WinoGrande Multilingual

## Paper

WinoGrande: An Adversarial Winograd Schema Challenge at Scale
https://arxiv.org/abs/1907.10641

A fill-in-the-blank coreference task with binary options, inspired by the Winograd Schema
Challenge but scaled up and adversarially filtered to reduce dataset-specific bias.

NOTE: this evaluation uses partial evaluation as described by Trinh & Le in Simple Method
for Commonsense Reasoning (2018). See: https://arxiv.org/abs/1806.02847

This is ellamind's multilingual release. Items are synthesised from WinoGrande seeds and
rewritten into natural target-language scenarios rather than translated literally, so the
`_`-blank structure is preserved while names and context are localised.

Dataset: https://huggingface.co/datasets/ellamind/winogrande-multilingual

## Citation

```
@article{sakaguchi2019winogrande,
    title={WinoGrande: An Adversarial Winograd Schema Challenge at Scale},
    author={Sakaguchi, Keisuke and Bras, Ronan Le and Bhagavatula, Chandra and Choi, Yejin},
    journal={arXiv preprint arXiv:1907.10641},
    year={2019}
}
```

### Groups and Tasks

#### Groups

- `ellamind`

#### Tasks

- `winogrande_multilingual_de`: German (`deu` config), 1267 docs.
- `winogrande_multilingual_fra`: French (`fra` config), 100 docs.

### Notes

- Scoring follows the upstream [winogrande](../winogrande/README.md) task: the sentence
  prefix up to the blank is combined with each option, and the shared suffix after the
  blank is scored as the continuation.
- `utils.doc_to_text_winogrande` uses `int(str(doc["answer"])) - 1` rather than upstream's
  `{"1": 0, "2": 1}` lookup; `answer` is the string `"1"`/`"2"` in this release, and the
  arithmetic form also tolerates an int-typed column.
- Validation-only dataset, so few-shot examples come from the split being scored. Prefer
  0-shot, or set `fewshot_split` explicitly.
- Because the items are synthesised rather than translated, they appear easier than the
  English original: 7–9B base models score ~0.84–0.90 here against ~0.73–0.77 on English
  WinoGrande. Do not read these as comparable to WinoGrande numbers.
- The French config has only 100 docs; confidence intervals will be wide.

### Checklist

- [x] Is the task an existing benchmark in the literature?
  - [x] Have you referenced the original paper that introduced the task?
  - [x] If yes, does the original paper provide a reference implementation? If so, have you checked against the reference implementation and documented how to run such a test?
- [x] Is the "Main" variant of this task clearly denoted?
- [x] Have you provided a short sentence in a README on what each new variant adds / evaluates?
- [x] Have you noted which, if any, published evaluation setups are matched by this variant?
