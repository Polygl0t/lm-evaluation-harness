# LeoLM

German translations of the four original Open LLM Leaderboard benchmarks, released by the
LeoLM project (LAION).

NOTE: the dataset cards document no translation methodology, and the released text contains
machine-translation artifacts (e.g. `"ist der Vatikanstadt"`, `"Ich habe keine
Kommentare"`). Treat these as machine translations when comparing against other German
translations of the same benchmarks.

Homepage: https://laion.ai/blog/leo-lm/

## Citation

```
@misc{leolm2023,
    title  = {LeoLM: Igniting German-Language LLM Research},
    author = {Bj{\"o}rn Pl{\"u}ster and Christoph Schuhmann},
    year   = {2023},
    howpublished = {\url{https://laion.ai/blog/leo-lm/}}
}
```

Cite the individual benchmarks from each subfolder as well.

### Groups and Tasks

#### Groups

- `leolm`

#### Tasks

- `arc_challenge_de` ([arc_challenge/](arc_challenge/README.md)): test split, 1150 docs
- `hellaswag_leolm_de` ([hellaswag/](hellaswag/README.md)): validation split, 10042 docs
- `mmlu_de` ([mmlu/](mmlu/README.md)): validation split
- `truthfulqa_leolm_de_mc1` ([truthfulqa/](truthfulqa/README.md)): 817 docs
- `truthfulqa_leolm_de_mc2` ([truthfulqa/](truthfulqa/README.md)): 817 docs

`hellaswag_leolm_de` and `truthfulqa_leolm_de_*` carry `leolm` in the task name because
`hellaswag_de` and `truthfulqa_de_mc1` are taken by [okapi](../okapi/).
