# GSM8K-X

## Paper

Towards Cross-Lingual LLM Evaluation for European Languages
https://arxiv.org/abs/2410.08928

openGPT-X's translation of GSM8K into 20 European languages. The chain-of-thought
rationales are translated along with the questions, so the set works as a few-shot CoT
benchmark in the target language rather than an answer-only task.

The source benchmark, GSM8K, is 8.5K grade-school math word problems requiring 2–8
elementary arithmetic steps, each with a solution ending in `#### <final answer>`.

Dataset: https://huggingface.co/datasets/LumiOpen/opengpt-x_gsm8kx

Source paper (GSM8K): https://arxiv.org/abs/2110.14168

## Citation

```
@misc{thellmann2024crosslingual,
    title={Towards Cross-Lingual LLM Evaluation for European Languages},
    author={Klaudia Thellmann and Bernhard Stadler and Michael Fromm and Jasper Schulze Buschhoff and Alex Jude and Fabio Barth and Johannes Leveling and Nicolas Flores-Herr and Joachim Köhler and René Jäkel and Mehdi Ali},
    year={2024},
    eprint={2410.08928},
    archivePrefix={arXiv},
    primaryClass={cs.CL}
}

@article{cobbe2021gsm8k,
    title={Training Verifiers to Solve Math Word Problems},
    author={Cobbe, Karl and Kosaraju, Vineet and Bavarian, Mohammad and Chen, Mark and Jun, Heewoo and Kaiser, Lukasz and Plappert, Matthias and Tworek, Jerry and Hilton, Jacob and Nakano, Reiichiro and Hesse, Christopher and Schulman, John},
    journal={arXiv preprint arXiv:2110.14168},
    year={2021}
}
```

### Groups and Tasks

#### Groups

- `opengptx`

#### Tasks

- `gsm8kx_de`, `gsm8kx_fr`, `gsm8kx_es`, `gsm8kx_it`, `gsm8kx_pt_pt`, `gsm8kx_nl`,
  `gsm8kx_da`, `gsm8kx_sv`, `gsm8kx_fi`, `gsm8kx_et`, `gsm8kx_lt`, `gsm8kx_lv`,
  `gsm8kx_pl`, `gsm8kx_cs`, `gsm8kx_sk`, `gsm8kx_sl`, `gsm8kx_hu`, `gsm8kx_ro`,
  `gsm8kx_bg`, `gsm8kx_el`

Each language has 1319 test problems and a 104-problem `train` split used as the few-shot
pool. `gsm8kx_de.yaml` holds the full configuration; the other 19 are one-line `include:`
files overriding only `task` and `dataset_name`, so **any change to `gsm8kx_de.yaml`
applies to all 20 languages**.

### Notes

- Configuration mirrors the upstream [gsm8k](../../gsm8k/README.md) task: same
  `exact_match` metric, same `regexes_to_ignore`, same `strict-match` /
  `flexible-extract` filters, same 5-shot default. Only the prompt keywords are translated.
- `doc_to_target` is the full rationale, not the final number, so the few-shot examples
  demonstrate reasoning. All 1319 test and 104 train answers end in `#### <number>`.
- Commas are normalised away on both sides: the translations retain English thousands
  separators in some gold answers (14 of 1319 in German).
- `ignore_punctuation` is `false`; setting it `true` would erase decimal points and let
  `2.5` match `25`.
- `max_gen_toks: 512`. German rationales reach ~410 tokens (p95 ~210); the 256 default
  truncates the tail before it emits `#### <number>`. Other languages are unmeasured.
- `"\n\n"` is not a stop sequence — rationales are multi-line. `Frage:` terminates at the
  next example.

### Checklist

- [x] Is the task an existing benchmark in the literature?
  - [x] Have you referenced the original paper that introduced the task?
  - [x] If yes, does the original paper provide a reference implementation? If so, have you checked against the reference implementation and documented how to run such a test?
- [x] Is the "Main" variant of this task clearly denoted?
- [x] Have you provided a short sentence in a README on what each new variant adds / evaluates?
- [x] Have you noted which, if any, published evaluation setups are matched by this variant?
