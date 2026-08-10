# MILU: A Multi-task Indic Language Understanding Benchmark

## Paper

Title: MILU: A Multi-task Indic Language Understanding Benchmark

Abstract: https://arxiv.org/abs/2411.02538

MILU (Multi-task Indic Language Understanding Benchmark) is a comprehensive evaluation dataset designed to assess the performance of Large Language Models (LLMs) across 11 Indic languages. It spans 8 domains and 41 subjects, reflecting both general and culturally specific knowledge from India.

### Citation

```latex
@article{verma2024milu,
  title   = {MILU: A Multi-task Indic Language Understanding Benchmark},
  author  = {Sshubam Verma and Mohammed Safi Ur Rahman Khan and Vishwajeet Kumar and Rudra Murthy and Jaydeep Sen},
  year    = {2024},
  journal = {arXiv preprint arXiv: 2411.02538}
}
```

#### Tasks

* milu_hi:  Assess the performance of Large Language Models (LLMs) across  8 domains and 41 subjects, reflecting both general and culturally specific knowledge from India.
Note: 
- Although MILU covers 11 Indic languages, this implementation is only for Hindi.
- The original implementation of this task in the lm-evaluation-harness can be found [here](https://github.com/AI4Bharat/MILU)
- The reason for including this task here is to provide a single, standardized place where we can evaluate multiple Hindi tasks.



### Checklist

For adding novel benchmarks/datasets to the library:

* [x] Is the task an existing benchmark in the literature?
  * [x] Have you referenced the original paper that introduced the task?
  * [x] If yes, does the original paper provide a reference implementation? If so, have you checked against the reference implementation and documented how to run such a test?

If other tasks on this dataset are already supported:

* [x] Is the "Main" variant of this task clearly denoted?
* [x] Have you provided a short sentence in a README on what each new variant adds / evaluates?
* [x] Have you noted which, if any, published evaluation setups are matched by this variant?


