# ParaCrawl

[[Dataset Download](https://huggingface.co/datasets/Wikidepia/IndoParaCrawl)] [[Original Paper](https://www.aclweb.org/anthology/W19-6721/)]

ParaCrawl v.7.1 is a parallel dataset with 41 language pairs primarily aligned with English (39 out of 41) and mined using the parallel-data-crawling tool Bitextor which includes downloading documents, preprocessing and normalization, aligning documents and segments, and filtering noisy data via Bicleaner. ParaCrawl focuses on European languages, but also includes 9 lower-resource, non-European language pairs in v7.1.

## Download

To download IndoParaCrawl you will need `git lfs`.

```bash
git lfs install
git clone https://huggingface.co/datasets/Wikidepia/IndoParaCrawl
```

## Citation

```bibtex
@inproceedings{espla-etal-2019-paracrawl,
    title = "{P}ara{C}rawl: Web-scale parallel corpora for the languages of the {EU}",
    author = "Espl{\`a}, Miquel  and
      Forcada, Mikel  and
      Ram{\'\i}rez-S{\'a}nchez, Gema  and
      Hoang, Hieu",
    booktitle = "Proceedings of Machine Translation Summit XVII Volume 2: Translator, Project and User Tracks",
    month = aug,
    year = "2019",
    address = "Dublin, Ireland",
    publisher = "European Association for Machine Translation",
    url = "https://www.aclweb.org/anthology/W19-6721",
    pages = "118--119",
}
```
