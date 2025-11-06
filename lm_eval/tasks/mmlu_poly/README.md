# MMLU

### Paper

Title: Measuring Massive Multitask Language Understanding

Abstract: https://arxiv.org/abs/2009.03300

The test covers 57 tasks including elementary mathematics, US history, computer science, law, and more.

Homepage: https://github.com/hendrycks/test

### Citation

```bibtex
@article{hendryckstest2021,
  title={Measuring Massive Multitask Language Understanding},
  author={Dan Hendrycks and Collin Burns and Steven Basart and Andy Zou and Mantas Mazeika and Dawn Song and Jacob Steinhardt},
  journal={Proceedings of the International Conference on Learning Representations (ICLR)},
  year={2021}
}

@article{hendrycks2021ethics,
  title={Aligning AI With Shared Human Values},
  author={Dan Hendrycks and Collin Burns and Steven Basart and Andrew Critch and Jerry Li and Dawn Song and Jacob Steinhardt},
  journal={Proceedings of the International Conference on Learning Representations (ICLR)},
  year={2021}
}
```

### Groups and Tasks

#### Groups

- `mmlu_poly`: Evaluates all `mmlu_poly_{lang}` tasks

#### Tasks

- `mmlu_poly_{lang}`: These are MMLU tasks in different languages introduced in the Polyglot evaluation harness.

<details>
<summary><b>All languages supported</b></summary>

```text
* ar (Arabic)
* bn (Bengali)
* ca (Catalan)
* da (Danish)
* de (German)
* es (Spanish)
* eu (Basque)
* fr (French)
* gu (Gujarati)
* hi (Hindi)
* hr (Croatian)
* hu (Hungarian)
* hy (Armenian)
* id (Indonesian)
* it (Italian)
* kn (Kannada)
* ml (Malayalam)
* mr (Marathi)
* ne (Nepali)
* nl (Dutch)
* pt (Portuguese)
* ro (Romanian)
* ru (Russian)
* sk (Slovak)
* sr (Serbian)
* sv (Swedish)
* ta (Tamil)
* te (Telugu)
* uk (Ukrainian)
* vi (Vietnamese)
* zh (Chinese)
```

</details>

### Checklist

For adding novel benchmarks/datasets to the library:

- [x] Is the task an existing benchmark in the literature?
  - [x] Have you referenced the original paper that introduced the task?
  - [x] If yes, does the original paper provide a reference implementation? If so, have you checked against the reference implementation and documented how to run such a test?

If other tasks on this dataset are already supported:

- [x] Is the "Main" variant of this task clearly denoted?
- [x] Have you provided a short sentence in a README on what each new variant adds / evaluates?
- [x] Have you noted which, if any, published evaluation setups are matched by this variant?
