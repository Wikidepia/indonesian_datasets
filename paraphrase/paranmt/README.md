# ParaNMT

[[Original Dataset](http://www.cs.cmu.edu/~jwieting/)] [[Dataset Download](https://depia.wiki/files/paranmt-5m.jsonl.zst)]

We describe PARANMT-50M, a dataset of more than 50 million English-English sentential paraphrase pairs. We generated the pairs automatically by using neural machine translation to translate the non-English side of a large parallel corpus, following Wieting et al. (2017). Our hope is that ParaNMT-50M can be a valuable resource for paraphrase generation and can provide a rich source of semantic knowledge to improve downstream natural language understanding tasks. To show its utility, we use ParaNMT-50M to train paraphrastic sentence embeddings that outperform all supervised systems on every SemEval semantic textual similarity competition, in addition to showing how it can be used for paraphrase generation.

## Citations

```bibtex
@inproceedings{wieting-gimpel-2018-paranmt,
    title = "{P}ara{NMT}-50{M}: Pushing the Limits of Paraphrastic Sentence Embeddings with Millions of Machine Translations",
    author = "Wieting, John  and
      Gimpel, Kevin",
    booktitle = "Proceedings of the 56th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)",
    month = jul,
    year = "2018",
    address = "Melbourne, Australia",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/P18-1042",
    doi = "10.18653/v1/P18-1042",
    pages = "451--462",
    abstract = "We describe ParaNMT-50M, a dataset of more than 50 million English-English sentential paraphrase pairs. We generated the pairs automatically by using neural machine translation to translate the non-English side of a large parallel corpus, following Wieting et al. (2017). Our hope is that ParaNMT-50M can be a valuable resource for paraphrase generation and can provide a rich source of semantic knowledge to improve downstream natural language understanding tasks. To show its utility, we use ParaNMT-50M to train paraphrastic sentence embeddings that outperform all supervised systems on every SemEval semantic textual similarity competition, in addition to showing how it can be used for paraphrase generation.",
}
```
