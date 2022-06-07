# Stanford Question Answering Dataset

[[Original Paper](https://arxiv.org/abs/1806.03822)] [[Original Dataset](https://rajpurkar.github.io/SQuAD-explorer/)] [[Dataset Download](https://cloud.depia.wiki/squad/)]

Stanford Question Answering Dataset (SQuAD) is a reading comprehension dataset, consisting of questions posed by crowdworkers on a set of Wikipedia articles, where the answer to every question is a segment of text, or span, from the corresponding reading passage, or the question might be unanswerable.

If you need to use `run_qa.py` from Hugging Face, you need to run `convert_huggingface.py` script to match Hugging Face training script.

## Folder description
- `/` aligned similar to [Swedish SQuAD](https://towardsdatascience.com/swedish-question-answering-with-bert-c856ccdcc337) and translated using Google Translated
- `/tar/` aligned using TranslateAlignRetrieve and translated using MarianMT

You can try both version, and find which one is the better one.

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
