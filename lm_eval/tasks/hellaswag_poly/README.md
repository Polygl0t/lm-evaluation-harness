# HellaSwag

### Paper

Title: HellaSwag: Can a Machine Really Finish Your Sentence?

Abstract: https://arxiv.org/abs/1905.07830

Recent work by Zellers et al. (2018) introduced a new task of commonsense natural language inference: given an event description such as "A woman sits at a piano," a machine must select the most likely followup: "She sets her fingers on the keys." With the introduction of BERT, near human-level performance was reached. Does this mean that machines can perform human level commonsense inference?
In this paper, we show that commonsense inference still proves difficult for even state-of-the-art models, by presenting HellaSwag, a new challenge dataset. Though its questions are trivial for humans (>95% accuracy), state-of-the-art models struggle (<48%). We achieve this via Adversarial Filtering (AF), a data collection paradigm wherein a series of discriminators iteratively select an adversarial set of machine-generated wrong answers. AF proves to be surprisingly robust. The key insight is to scale up the length and complexity of the dataset examples towards a critical 'Goldilocks' zone wherein generated text is ridiculous to humans, yet often misclassified by state-of-the-art models.
Our construction of HellaSwag, and its resulting difficulty, sheds light on the inner workings of deep pretrained models. More broadly, it suggests a new path forward for NLP research, in which benchmarks co-evolve with the evolving state-of-the-art in an adversarial way, so as to present ever-harder challenges.

Homepage: https://rowanzellers.com/hellaswag/

### Citation

```bibtex
@inproceedings{zellers2019hellaswag,
    title={HellaSwag: Can a Machine Really Finish Your Sentence?},
    author={Zellers, Rowan and Holtzman, Ari and Bisk, Yonatan and Farhadi, Ali and Choi, Yejin},
    booktitle ={Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics},
    year={2019}
}
```

### Groups and Tasks

#### Groups

- None

#### Tasks

- `hellaswag_poly_{lang}`: These are HellaSwag tasks in different languages introduced in the Polyglot evaluation harness.

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
