# PAWS : Paraphrase Adversaries from Word Scrambling

This dataset contains 108,463 human-labeled and 656k noisily labeled pairs that feature the importance of modeling structure, context, and word order information for the problem of paraphrase identification.

All translated pairs are sourced from examples in [PAWS-Wiki](https://github.com/google-research-datasets/paws#paws-wiki).

- [`PAWS-Wiki Labeled (Final)`](https://github.com/Wikidepia/indonesia_dataset/tree/master/paraphrase/PAWS/data/final): containing pairs that are generated from both word swapping and back translation methods. All pairs have human judgements on both paraphrasing and fluency and they are split into Train/Dev/Test sections.

- [`PAWS-Wiki Labeled (Swap-only)`](https://github.com/Wikidepia/indonesia_dataset/tree/master/paraphrase/PAWS/data/swap): containing pairs that have no back translation counterparts and therefore they are not included in the first set. Nevertheless, they are high-quality pairs with human judgements on both paraphrasing and fluency, and they can be included as an auxiliary training set.

Translated to Indonesia using Google Translate API. Translate script is included.

[Original Dataset](https://github.com/google-research-datasets/paws)
