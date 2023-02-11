# Javanese Text

[[Dataset Download](https://storage.depia.wiki/jv-text/)]

Extracting Javanese text from available data. The data used comes from:

- CC100
- [data.statmt.org](http://data.statmt.org/ngrams/raw/)
- Wikipedia

## Process

1. Detect language with CLD3
2. Score sentence with KenLM with Javanese Wikipedia
3. Dedupe with simple awk

## Citations

```bibtex
@inproceedings{wenzek2020ccnet,
  title={CCNet: Extracting High Quality Monolingual Datasets from Web Crawl Data},
  author={Wenzek, Guillaume and Lachaux, Marie-Anne and Conneau, Alexis and Chaudhary, Vishrav and Guzm{\'a}n, Francisco and Joulin, Armand and Grave, {\'E}douard},
  booktitle={Proceedings of The 12th Language Resources and Evaluation Conference},
  pages={4003--4012},
  year={2020}
}
```