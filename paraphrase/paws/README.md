# Paraphrase Adversaries from Word Scrambling

[[Original Paper](https://arxiv.org/abs/1904.01130)] [[Original Dataset](https://github.com/google-research-datasets/paws)] [[Dataset Download](https://github.com/Wikidepia/indonesia_dataset/tree/master/paraphrase/paws/data)]

This dataset contains 100k human-labeled pairs that feature the importance of modeling structure, context, and word order information for the problem of paraphrase identification.

All translated pairs are sourced from examples in [PAWS-Wiki](https://github.com/google-research-datasets/paws#paws-wiki).

- [`PAWS-Wiki Labeled (Final)`](https://github.com/Wikidepia/indonesia_dataset/tree/master/paraphrase/PAWS/data/final): containing pairs that are generated from both word swapping and back translation methods. All pairs have human judgements on both paraphrasing and fluency and they are split into Train/Dev/Test sections.

- [`PAWS-Wiki Labeled (Swap-only)`](https://github.com/Wikidepia/indonesia_dataset/tree/master/paraphrase/PAWS/data/swap): containing pairs that have no back translation counterparts and therefore they are not included in the first set. Nevertheless, they are high-quality pairs with human judgements on both paraphrasing and fluency, and they can be included as an auxiliary training set.

Translated to Indonesia using Google Translate API. Translate script is included.

## Citation

```bibtex
@misc{zhang2019paws,
      title={PAWS: Paraphrase Adversaries from Word Scrambling}, 
      author={Yuan Zhang and Jason Baldridge and Luheng He},
      year={2019},
      eprint={1904.01130},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```
