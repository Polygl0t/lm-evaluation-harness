# openGPT-X

Translations of standard English benchmarks into 20 European languages, released by the
openGPT-X project and conventionally named with an `-X` suffix (HellaSwag-X, MMLU-X,
GSM8K-X).

NOTE: all tasks load from the `LumiOpen/opengpt-x_*` mirrors rather than openGPT-X's own
repos, because the latter ship loading scripts that `datasets` >= 3 refuses to run. The
mirrors are script-free copies of the same translations. If a number looks wrong, the raw
JSONL under `openGPT-X/<benchmark>` is the reference.

## Paper

Towards Cross-Lingual LLM Evaluation for European Languages
https://arxiv.org/abs/2410.08928

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
```

Cite the source benchmark from each subfolder as well.

### Groups and Tasks

#### Groups

- `opengptx`
- `mmlux_de`: the 57 German MMLU-X subjects

#### Tasks

- [gsm8kx/](gsm8kx/README.md): `gsm8kx_de` and 19 other languages. German: 1319 test,
  104 train.
- [hellaswagx/](hellaswagx/): `hellaswagx_de` and 19 other languages. German: 9979
  validation, 99 train.
- [mmlux/](mmlux/): `mmlux_de_<subject>` for 57 subjects, German only.

### Notes

- `gsm8kx` is configured as few-shot chain-of-thought. One base config is shared across all
  20 languages, so editing `gsm8kx_de.yaml` changes every language.
- `mmlux` is cloze-scored rather than using MMLU's lettered format, so it is not comparable
  to published MMLU scores. It has a held-out `dev` split for few-shot.
- `hellaswagx` few-shot settings and split choices have not been checked against the
  upstream English task; its German `train` split is only 99 docs.
- ARC-X is not included: LumiOpen publishes no `opengpt-x_arcx` mirror, and
  `openGPT-X/arcx` has a loading script and no per-language `configs:`. Use
  [arc_mt](../arc_mt/) or [leolm/arc_challenge](../leolm/arc_challenge/README.md) for
  German ARC.
- TruthfulQA-X and GoldenSwag-X have script-free mirrors but no tasks here yet.
