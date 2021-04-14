# Indonesia Dataset

This repository will be used to store Indonesian Datasets. 

## Where did the dataset come from?

1. I usually scrape from internet. 
2. If the dataset is available in English, I use Google Translate to translate it.

## Table of contents
  * [Crawl](#crawl)
    * [Kaskus WebText](#kaskus-webtext)
    * [Twitter Puisi](#twitter-puisi)
    * [Wipedia Links](#wikipedia-links)
  * [Dictionary](#dictionary)
    * [Wordlist](#wordlist)
  * [Dump](#dump)
    * [Twitter](#twitter)
  * [Paraphrase](#paraphrase)
    * [PAWS](#paws)
  * [Question Answering](#question-answering)
    * [SQuAD](#squad)
    * [Mathematics Dataset](#mathematics-dataset)
  * [Speech](#speech)
    * [Bible](#bible)
  * [Summarization](#summarization)
    * [Gigaword](#gigaword)
    * [WikiHow](#wikihow)
  * [Translation](#translation)
    * [ParaCrawl](#paracrawl)

## [Crawl](crawl)

#### [Kaskus WebText](crawl/kaskus-webtext)

Scrape URLs from Kaskus (Starter only), filter to 3 or more cendol (karma). 

#### [Twitter Puisi](crawl/twitter-puisi)

This dataset contains poem from various user on Twitter. 

#### [Wikipedia Links](crawl/wikipedia-links)

Wikipedia have a lot of references & citations from internet. It should contain some high quality web content, this dataset contains content from 58k urls in Indonesian Wikipedia external links dump.

## [Dictionary](dictionary)

#### [Wordlist](dictionary/wordlist)

This dataset contains 105,226 words from Kamus Besar Bahasa Indonesia.

## [Dump](dump)

#### [Twitter](dump/twitter)

This dataset contains tweets from 2011, filtered from ArchiveTeam dump using fastText. More data will be released soon!

## [Paraphrase](paraphrase)

#### [PAWS](paraphrase/paws)

This dataset contains 108,463 human-labeled and 656k noisily labeled pairs that feature the importance of modeling structure, context, and word order information for the problem of paraphrase identification.

## [Question Answering](question-answering)

#### [SQuAD](question-answering/squad)

Stanford Question Answering Dataset (SQuAD) is a reading comprehension dataset, consisting of questions posed by crowdworkers on a set of Wikipedia articles, where the answer to every question is a segment of text, or span, from the corresponding reading passage, or the question might be unanswerable.

#### [Mathematics Dataset](question-answering/mathematics_dataset)

This dataset contains mathematical question and answer pairs, from a range of question types at roughly school-level difficulty. This is designed to test the mathematical learning and algebraic reasoning skills of learning models.

## [Speech](speech)

#### [Bible](speech/bible)

Scrape audio from [Bible.is](https://bible.is). I cannot share the data because of copyright stuff. I already provide script to replicate it.

## [Summarization](summarization)

#### [Gigaword](summarization/gigaword)

Headline-generation on a corpus of article pairs from Gigaword consisting of around 4 million articles. Use the 'org_data' provided by [https://github.com/microsoft/unilm/](https://github.com/microsoft/unilm/) which is identical to [https://github.com/harvardnlp/sent-summary](https://github.com/harvardnlp/sent-summary) but with better format.

#### [WikiHow](summarization/wikihow)

WikiHow is a new large-scale dataset using the online [WikiHow](https://id.wikihow.com/) knowledge base. Each article consists of multiple paragraphs and each paragraph starts with a sentence summarizing it. By merging the paragraphs to form the article and the paragraph outlines to form the summary.

## [Translation](translation)

#### [ParaCrawl](translation/paracrawl)

ParaCrawl v.7.1 is a parallel dataset with 41 language pairs primarily aligned with English (39 out of 41) and mined using the parallel-data-crawling tool Bitextor which includes downloading documents, preprocessing and normalization, aligning documents and segments, and filtering noisy data via Bicleaner. ParaCrawl focuses on European languages, but also includes 9 lower-resource, non-European language pairs in v7.1.

## Disclaimer

I do not own any of this dataset. Do not use for Commercial Purpose!
