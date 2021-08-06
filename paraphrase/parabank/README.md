# ParaBank

[[Original Dataset](https://nlp.jhu.edu/parabank/)] [[Dataset Download (v2.0)](https://depia.wiki/files/parabank-v2.0.jsonl.zst)]

The ParaBank project consists of a series of efforts exploring the potential for guided backtranslation for the purpose of paraphrasing with constraints. This work is spiritually connected to prior efforts at JHU in paraphrasing, in particular projects surrounding the ParaPhrase DataBase (PPDB).

## Citations

```bibtex
@inproceedings{hu-etal-2019-large,
    title = "Large-Scale, Diverse, Paraphrastic Bitexts via Sampling and Clustering",
    author = "Hu, J. Edward  and
      Singh, Abhinav  and
      Holzenberger, Nils  and
      Post, Matt  and
      Van Durme, Benjamin",
    booktitle = "Proceedings of the 23rd Conference on Computational Natural Language Learning (CoNLL)",
    month = nov,
    year = "2019",
    address = "Hong Kong, China",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/K19-1005",
    doi = "10.18653/v1/K19-1005",
    pages = "44--54",
    abstract = "Producing diverse paraphrases of a sentence is a challenging task. Natural paraphrase corpora are scarce and limited, while existing large-scale resources are automatically generated via back-translation and rely on beam search, which tends to lack diversity. We describe ParaBank 2, a new resource that contains multiple diverse sentential paraphrases, produced from a bilingual corpus using negative constraints, inference sampling, and clustering.We show that ParaBank 2 significantly surpasses prior work in both lexical and syntactic diversity while being meaning-preserving, as measured by human judgments and standardized metrics. Further, we illustrate how such paraphrastic resources may be used to refine contextualized encoders, leading to improvements in downstream tasks.",
}
```
