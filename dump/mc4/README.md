# "Clean" mC4

[[Original Dataset](https://github.com/allenai/allennlp/discussions/5265)]] [[Dataset Download (Soon)](https://depia.wiki/files/mc4)]

Indonesian mC4 with filtering from spam, NSFW, and Gambling. Big thanks to AllenAI for releasing Multilingual C4 🙏.

## Filtering Steps

1. Remove text from CCAligned domain (Why? CCAligned sometimes contains machine translated website.)
2. Find porn-y and gambling words, if it exceeds certain threshold it wont be included.
3. Train fasttext clasifier from (NSFW & Gambling) and (Indonesian CC-NEWS) text and classify text with it.

## Citations

```bibtex
@article{Raffel2020ExploringTL,
  title={Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer},
  author={Colin Raffel and Noam M. Shazeer and Adam Roberts and Katherine Lee and Sharan Narang and Michael Matena and Yanqi Zhou and W. Li and Peter J. Liu},
  journal={ArXiv},
  year={2020},
  volume={abs/1910.10683}
}
```
