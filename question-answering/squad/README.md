# Stanford Question Answering Dataset

[[Original Paper](https://arxiv.org/abs/1806.03822)] [[Original Dataset](https://rajpurkar.github.io/SQuAD-explorer/)] [[Dataset Download](https://github.com/Wikidepia/indonesia_dataset/tree/master/question-answering/squad/data)]

Stanford Question Answering Dataset (SQuAD) is a reading comprehension dataset, consisting of questions posed by crowdworkers on a set of Wikipedia articles, where the answer to every question is a segment of text, or span, from the corresponding reading passage, or the question might be unanswerable.

**NEW** : Properly aligned SQuAD now added! Thanks to [TranslateAlignRetrieve](https://github.com/ccasimiro88/TranslateAlignRetrieve).

This dataset translated from English to Indonesia with Google Translate, and only aligned by searching from beginning of the context.

If you need to use `run_qa.py` from Huggingace, you need to run `process_hf.py` script to match Huggingface script.

## Citations

```bibtex
@misc{rajpurkar2018know,
      title={Know What You Don't Know: Unanswerable Questions for SQuAD}, 
      author={Pranav Rajpurkar and Robin Jia and Percy Liang},
      year={2018},
      eprint={1806.03822},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```

```bibtex
@misc{carrino2019automatic,
      title={Automatic Spanish Translation of the SQuAD Dataset for Multilingual Question Answering}, 
      author={Casimiro Pio Carrino and Marta R. Costa-jussà and José A. R. Fonollosa},
      year={2019},
      eprint={1912.05200},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```
