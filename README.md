# Indonesia Dataset

This repository will be used to store Indonesia Dataset. Mostly from translating other dataset.

## Table of contents
  * [Crawl](#crawl)
    * [Neliti](#neliti)
    * [Twitter](#twitter)
    * [Twitter Puisi](#twitter-puisi)
  * [Dictionary](#dictionary)
    * [Wordlist](#wordlist)
  * [Paraphrase](#paraphrase)
    * [PAWS](#paws)
  * [Question Answering](#question-answering)
    * [SQuAD](#SQuAD)
    * [Mathematics Dataset](#mathematics_dataset)

## [Crawl](crawl)

#### [Neliti](crawl/neliti)

This dataset is my attempt to replicate [The Pile arXiv](https://arxiv.org/abs/2101.00027). This dataset only contain 1/4 of the entire Neliti.com. More data will be released soon!

#### [Twitter](crawl/twitter)

This dataset is crawled from Twitter. Contains the first 100 tweets from random 10k users and filtered using fastText.

#### [Twitter Puisi](crawl/twitter-puisi)

This dataset contains poem from various user on Twitter. 

## [Dictionary](dictionary)

#### [Wordlist](dictionary/wordlist)

This dataset contains 105,226 words from Kamus Besar Bahasa Indonesia.

## [Paraphrase](paraphrase)

#### [PAWS](paraphrase/PAWS)

This dataset contains 108,463 human-labeled and 656k noisily labeled pairs that feature the importance of modeling structure, context, and word order information for the problem of paraphrase identification.

[Original Dataset](https://github.com/google-research-datasets/paws)

## [Question Answering](question-answering)

#### [SQuAD](question-answering/SQuAD)

Stanford Question Answering Dataset (SQuAD) is a reading comprehension dataset, consisting of questions posed by crowdworkers on a set of Wikipedia articles, where the answer to every question is a segment of text, or span, from the corresponding reading passage, or the question might be unanswerable.

[Original Dataset](https://rajpurkar.github.io/SQuAD-explorer/)

#### [Mathematics Dataset](question-answering/mathematics_dataset)

This dataset contains mathematical question and answer pairs, from a range of question types at roughly school-level difficulty. This is designed to test the mathematical learning and algebraic reasoning skills of learning models.

[Original Dataset](https://github.com/deepmind/mathematics_dataset)
