# Reddit TLDR

[[Original Paper](https://www.aclweb.org/anthology/W17-4508/)] [[Dataset Download](https://depia.wiki/files/reddit-tldr.jsonl.zst)]

The Webis TLDR Corpus (2017) consists of approximately 4 Million content-summary pairs extracted for Abstractive Summarization, from the Reddit dataset for the years 2006-2016. This corpus is first of its kind from the social media domain in English and has been created to compensate the lack of variety in the datasets used for abstractive summarization research using deep learning models.

## Caution

Translation might seem a bit bad because of Google Translate character limit. So I need to split paragraph to sentences and merge them together.

## Citation

```bibtex
@inproceedings{volske-etal-2017-tl,
    title = "{TL};{DR}: Mining {R}eddit to Learn Automatic Summarization",
    author = {V{\"o}lske, Michael  and
      Potthast, Martin  and
      Syed, Shahbaz  and
      Stein, Benno},
    booktitle = "Proceedings of the Workshop on New Frontiers in Summarization",
    month = sep,
    year = "2017",
    address = "Copenhagen, Denmark",
    publisher = "Association for Computational Linguistics",
    url = "https://www.aclweb.org/anthology/W17-4508",
    doi = "10.18653/v1/W17-4508",
    pages = "59--63",
    abstract = "Recent advances in automatic text summarization have used deep neural networks to generate high-quality abstractive summaries, but the performance of these models strongly depends on large amounts of suitable training data. We propose a new method for mining social media for author-provided summaries, taking advantage of the common practice of appending a {``}TL;DR{''} to long posts. A case study using a large Reddit crawl yields the Webis-TLDR-17 dataset, complementing existing corpora primarily from the news genre. Our technique is likely applicable to other social media sites and general web crawls.",
}
```
