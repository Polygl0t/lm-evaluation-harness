# Context-Aware LAnguage Modeling Evaluation for Portuguese (CALAME-PT)

### Paper

Context-Aware LAnguage Modeling Evaluation for Portuguese (CALAME-PT)

CALAME-PT is a PT benchmark composed of small texts (_contexts_) and their respective last words. These contexts should, in theory, contain enough information so that a human or a model is capable of guessing its last word - without being too specific and/or too ambiguous. This dataset correspond to the ones mentioned and used in the [GlorIA](https://aclanthology.org/2024.propor-1.45/) paper.

Homepage: https://huggingface.co/datasets/NOVA-vision-language/calame-pt

### Citation

```bibtex
@inproceedings{lopes-etal-2024-gloria,
    title = "{G}l{\'o}r{IA}: A Generative and Open Large Language Model for {P}ortuguese",
    author = "Lopes, Ricardo  and
      Magalhaes, Joao  and
      Semedo, David",
    editor = "Gamallo, Pablo  and
      Claro, Daniela  and
      Teixeira, Ant{\'o}nio  and
      Real, Livy  and
      Garcia, Marcos  and
      Oliveira, Hugo Gon{\c{c}}alo  and
      Amaro, Raquel",
    booktitle = "Proceedings of the 16th International Conference on Computational Processing of Portuguese - Vol. 1",
    month = mar,
    year = "2024",
    address = "Santiago de Compostela, Galicia/Spain",
    publisher = "Association for Computational Lingustics",
    url = "https://aclanthology.org/2024.propor-1.45/",
    pages = "441--453"
}
```

### Groups and Tasks

- `calame_pt`

#### Tasks

- `calame_pt`: This is the CALAME-PT task introduced in the GlorIA paper.

### Checklist

- [x] Is the task an existing benchmark in the literature?
  - [x] Have you referenced the original paper that introduced the task?
  - [x] If yes, does the original paper provide a reference implementation? If so, have you checked against the reference implementation and documented how to run such a test?
        (This task is novel to the Evaluation Harness, and has been checked against v0.3.0 of the harness.)

If other tasks on this dataset are already supported:

- [x] Is the "Main" variant of this task clearly denoted?
- [x] Have you provided a short sentence in a README on what each new variant adds / evaluates?
- [x] Have you noted which, if any, published evaluation setups are matched by this variant?
