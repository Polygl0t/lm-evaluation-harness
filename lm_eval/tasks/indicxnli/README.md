# IndicXNLI

## Paper

Title: IndicXNLI: Evaluating Multilingual Inference for Indian Languages

Abstract: https://aclanthology.org/2022.emnlp-main.755/

IndicXNLI is similar to existing XNLI dataset in shape/form, but focusses on Indic language family. IndicXNLI include NLI data for eleven major Indic languages. This repository currently implements the Hindi and Gujarati translations of the original English XNLI dataset.

Homepage: https://huggingface.co/datasets/Divyanshu/indicxnli

### Citation
```latex
@inproceedings{aggarwal-etal-2022-indicxnli,
    title = "{I}ndic{XNLI}: Evaluating Multilingual Inference for {I}ndian Languages",
    author = "Aggarwal, Divyanshu  and
      Gupta, Vivek  and
      Kunchukuttan, Anoop",
    booktitle = "Proceedings of the 2022 Conference on Empirical Methods in Natural Language Processing",
    month = dec,
    year = "2022",
    address = "Abu Dhabi, United Arab Emirates",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2022.emnlp-main.755",
    pages = "10994--11006",
    abstract = "While Indic NLP has made rapid advances recently in terms of the availability of corpora and pre-trained models, benchmark datasets on standard NLU tasks are limited. To this end, we introduce INDICXNLI, an NLI dataset for 11 Indic languages. It has been created by high-quality machine translation of the original English XNLI dataset and our analysis attests to the quality of INDICXNLI. By finetuning different pre-trained LMs on this INDICXNLI, we analyze various cross-lingual transfer techniques with respect to the impact of the choice of language models, languages, multi-linguality, mix-language input, etc. These experiments provide us with useful insights into the behaviour of pre-trained models for a diverse set of languages.",
}
```

#### Tasks

* `indicxnli`: Hindi translation of the original English XNLI dataset
* `indicxnli_gu`: Gujarati natural language inference (entailment/neutral/contradiction), scored via loglikelihood over the three label continuations, following the same format as the existing `xnli` task family. This is not part of the existing xnli group, since that group is built on `facebook/xnli`, which does not include Gujarati. This task instead uses `Divyanshu/indicxnli`, the dataset from the IndicXNLI paper, mirroring the xnli task structure for consistency.

### Checklist

For adding novel benchmarks/datasets to the library:

* [x] Is the task an existing benchmark in the literature?
  * [x] Have you referenced the original paper that introduced the task?
  * [x] If yes, does the original paper provide a reference implementation? If so, have you checked against the reference implementation and documented how to run such a test?

If other tasks on this dataset are already supported:

* [x] Is the "Main" variant of this task clearly denoted?
* [x] Have you provided a short sentence in a README on what each new variant adds / evaluates?
* [x] Have you noted which, if any, published evaluation setups are matched by this variant?
