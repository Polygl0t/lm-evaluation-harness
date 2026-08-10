# Cloze-style Multiple Choice QA

## Paper

Title: IndicNLPSuite: Monolingual Corpora, Evaluation Benchmarks and Pre-trained Multilingual Language Models for Indian Languages

Abstract: https://aclanthology.org/2020.findings-emnlp.445.pdf

Cloze-style Multiple Choice QA (CSQA): is a question answering task for Hindi language in which an entity in a sentence is masked and the model must select the correct entity from four candidates, emphasizing commonsense and relational reasoning. This dataset is available in other Indian languages as well, but this implementation is only for Hindi.


### Citation

```latex
@inproceedings{kakwani-etal-2020-indicnlpsuite,
    title = "{I}ndic{NLPS}uite: Monolingual Corpora, Evaluation Benchmarks and Pre-trained Multilingual Language Models for {I}ndian Languages",
    author = "Kakwani, Divyanshu  and
      Kunchukuttan, Anoop  and
      Golla, Satish  and
      N.C., Gokul  and
      Bhattacharyya, Avik  and
      Khapra, Mitesh M.  and
      Kumar, Pratyush",
    booktitle = "Findings of the Association for Computational Linguistics: EMNLP 2020",
    month = nov,
    year = "2020",
    address = "Online",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2020.findings-emnlp.445",
    doi = "10.18653/v1/2020.findings-emnlp.445",
    pages = "4948--4961",
}
```

#### Tasks

* `csqa_hi`: Given a text with an entity randomly masked, the task is to predict that masked entity from a list of 4 candidate entities (3 incorrect, 1 correct). 


### Checklist

For adding novel benchmarks/datasets to the library:

* [x] Is the task an existing benchmark in the literature?
  * [x] Have you referenced the original paper that introduced the task?
  * [x] If yes, does the original paper provide a reference implementation? If so, have you checked against the reference implementation and documented how to run such a test?

If other tasks on this dataset are already supported:

* [x] Is the "Main" variant of this task clearly denoted?
* [x] Have you provided a short sentence in a README on what each new variant adds / evaluates?
* [x] Have you noted which, if any, published evaluation setups are matched by this variant?


