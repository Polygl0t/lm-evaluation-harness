# HumanEval Multilingual

## Paper

Evaluating Large Language Models Trained on Code
https://arxiv.org/abs/2107.03374

HumanEval is a set of 164 hand-written Python programming problems. Each gives a function
signature and a docstring; the model completes the body and the completion is executed
against the problem's unit tests.

This is ellamind's release with the docstrings translated. Function signatures, identifiers
and tests stay in English/Python, so the task isolates the model's ability to follow a
non-English specification.

Dataset: https://huggingface.co/datasets/ellamind/humaneval-multilingual

## Citation

```
@misc{chen2021evaluating,
    title={Evaluating Large Language Models Trained on Code},
    author={Mark Chen and Jerry Tworek and Heewoo Jun and Qiming Yuan and Henrique Ponde de Oliveira Pinto and Jared Kaplan and Harri Edwards and Yuri Burda and Nicholas Joseph and Greg Brockman and Alex Ray and Raul Puri and Gretchen Krueger and Michael Petrov and Heidy Khlaaf and Girish Sastry and Pamela Mishkin and Brooke Chan and Scott Gray and Nick Ryder and Mikhail Pavlov and Alethea Power and Lukasz Kaiser and Mohammad Bavarian and Clemens Winter and Philippe Tillet and Felipe Petroski Such and Dave Cummings and Matthias Plappert and Fotios Chantzis and Elizabeth Barnes and Ariel Herbert-Voss and William Hebgen Guss and Alex Nichol and Alex Paino and Nikolas Tezak and Jie Tang and Igor Babuschkin and Suchir Balaji and Shantanu Jain and William Saunders and Christopher Hesse and Andrew N. Carr and Jan Leike and Josh Achiam and Vedant Misra and Evan Morikawa and Alec Radford and Matthew Knight and Miles Brundage and Mira Murati and Katie Mayer and Peter Welinder and Bob McGrew and Dario Amodei and Sam McCandlish and Ilya Sutskever and Wojciech Zaremba},
    year={2021},
    eprint={2107.03374},
    archivePrefix={arXiv},
    primaryClass={cs.LG}
}
```

### Groups and Tasks

#### Groups

- `ellamind`

#### Tasks

- `humaneval_multilingual_de`: German docstrings, 142 docs.
- `humaneval_multilingual_fra`: French docstrings, 142 docs.

## Usage

These tasks execute model-generated code and are marked `unsafe_code: true`. They require
both `--confirm_run_unsafe_code` and `HF_ALLOW_CODE_EVAL=1`:

```bash
HF_ALLOW_CODE_EVAL=1 lm_eval --model hf --model_args pretrained=<model> \
    --tasks humaneval_multilingual_de --confirm_run_unsafe_code
```

### Notes

- Configuration matches the upstream [humaneval](../humaneval/README.md) task: same `until`
  stop sequences, `max_gen_toks`, `pass_at_k` metric with `k: [1]`, the same
  `build_predictions` filter, and the default `target_delimiter`, so prompts are
  byte-identical to upstream and scores can be read against the English baseline.
- 142 of the original 164 problems survive translation, so absolute numbers are not
  comparable to 164-problem HumanEval results.
- The dataset also carries `canonical_solution`, `translation_confidence` and
  `required_adaptation` columns, for filtering to problems marked as direct translations.

### Checklist

- [x] Is the task an existing benchmark in the literature?
  - [x] Have you referenced the original paper that introduced the task?
  - [x] If yes, does the original paper provide a reference implementation? If so, have you checked against the reference implementation and documented how to run such a test?
- [x] Is the "Main" variant of this task clearly denoted?
- [x] Have you provided a short sentence in a README on what each new variant adds / evaluates?
- [x] Have you noted which, if any, published evaluation setups are matched by this variant?
