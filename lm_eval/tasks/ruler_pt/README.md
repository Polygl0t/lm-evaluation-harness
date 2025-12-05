# Task-name

### Paper

**This is a PORTUGUESE implementation of the RULER benchmark. For the original English version, please refer to [lm_eval/tasks/ruler/README.md](../ruler/README.md). The haystack is downloaded from the [OneRuler](https://github.com/mungg/OneRuler) repository, which contains long Portuguese texts. The QA tasks are not available in this version (yet).**

Title: `RULER: What’s the Real Context Size of Your Long-Context Language Models?`

Abstract: `https://arxiv.org/abs/2404.06654`

`RULER expands upon the vanilla NIAH test to encompass variations with diverse types and quantities of needles. Moreover, RULER introduces new task categories multi-hop tracing and aggregation to test behaviors beyond searching from context. We evaluate 17 long-context LMs with 13 representative tasks in RULER.`

Homepage: `https://github.com/NVIDIA/RULER`

> [!NOTE]
> When using Ruler tasks, please note:
>
> 1. A tokenizer is required for data processing. The system will use the `tokenizer` from model_args, or fall back to the tokenizer associated with the `pretrained` model name.
> 2. The default maximum sequence length is 4096. For calculating metrics of different max seq lengths, specify additional lengths using the metadata parameter:
>    `--metadata='{"max_seq_lengths":[4096,8192,16384,32768,65536,131072]}'`. The metadata parameter can also be passed to the TaskManager (metadata: dict).
> 3. To prevent truncation of longer sequences, we recommend setting the max_length parameter in model_args:
>    `--model_args=pretrained=...,max_length=32768`

### Citation

```
@article{hsieh2024ruler,
  title={RULER: What's the Real Context Size of Your Long-Context Language Models?},
  author={Cheng-Ping Hsieh and Simeng Sun and Samuel Kriman and Shantanu Acharya and Dima Rekesh and Fei Jia and Yang Zhang and Boris Ginsburg},
  year={2024},
  journal={arXiv preprint arXiv:2404.06654},
}
@article{kim2025one,
  title={One ruler to measure them all: Benchmarking multilingual long-context language models},
  author={Kim, Yekyung and Russell, Jenna and Karpinska, Marzena and Iyyer, Mohit},
  journal={arXiv preprint arXiv:2503.01996},
  year={2025}
}
```

### Groups, Tags, and Tasks

#### Groups

- `ruler_pt`: `11 tasks from the original RULER benchmark`

#### Tags

`longcxt`: `Long-context tasks`

#### Tasks

- `niah_pt_single_1`: `NIAH single needle; key=word,value=number,haystack=repeat ∼passkey retrieval`
- `niah_pt_single_2`: `NIAH single needle; key=word,value=number,haystack=essay ∼vanilla NIAH`
- `niah_pt_single_3`: `NIAH single needle; key=word,value=uuid,haystack=essay`
- `niah_pt_multikey_1`: `NIAH multi-key, ∼line retrieval`
- `niah_pt_multikey_2`: `NIAH multi-key, ∼KV retrieval`
- `niah_pt_multikey_3`: `NIAH multi-key, `
- `niah_pt_multiquery`: `NIA multi-query`
- `niah_pt_multivalue`: `NIAH multi-value`
- `ruler_pt_vt`: `Variation tracing`
- `ruler_pt_cwe`: `Common word extraction`
- `ruler_pt_fwe`: `Frequent word extraction`

### Checklist

For adding novel benchmarks/datasets to the library:

- [x] Is the task an existing benchmark in the literature?
  - [x] Have you referenced the original paper that introduced the task?
  - [x] If yes, does the original paper provide a reference implementation? If so, have you checked against the reference implementation and documented how to run such a test?

If other tasks on this dataset are already supported:

- [x] Is the "Main" variant of this task clearly denoted?
- [x] Have you provided a short sentence in a README on what each new variant adds / evaluates?
- [x] Have you noted which, if any, published evaluation setups are matched by this variant?

### Changelog
