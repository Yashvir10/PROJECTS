# simple_nlp — Basic NLP Preprocessing Demo

A beginner-friendly notebook demonstrating the core building blocks of a text preprocessing pipeline using NLTK and scikit-learn.

## Overview

This notebook walks through the fundamental steps of preparing raw text for NLP tasks, using a single example sentence and a small two-document corpus:

1. **Text cleaning** — lowercasing, removing non-alphabetic characters, and collapsing extra whitespace.
2. **Tokenization** — splitting cleaned text into individual word tokens.
3. **Stopword removal** — filtering out common English stopwords (e.g., "the", "are", "over").
4. **Stemming** — reducing words to their root form using the Porter Stemmer.
5. **Lemmatization** — reducing words to their dictionary base form using WordNet's lemmatizer (verb mode).
6. **Vectorization** — converting a small text corpus into a bag-of-words matrix with `CountVectorizer`.

## Requirements

```
nltk
scikit-learn
```

Install with:
```bash
pip install nltk scikit-learn
```

You'll also need the following NLTK resources downloaded (not included in this notebook — download separately if needed):
```python
import nltk
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')
nltk.download('wordnet')
```

## How to Run

1. Open `simple_nlp.ipynb` in Jupyter Notebook / JupyterLab / VS Code.
2. Run all cells in order (top to bottom).
3. Observe the printed output at each stage: cleaned text → tokens → filtered tokens → stemmed tokens → lemmatized tokens → vocabulary and vectors.

## Example Walkthrough

**Input:**
```
"The quick brown foxes are jumping over the lazy dogs! Running fast, they laughed."
```

**After cleaning:**
```
the quick brown foxes are jumping over the lazy dogs running fast they laughed
```

**After stopword removal:**
```
['quick', 'brown', 'foxes', 'jumping', 'lazy', 'dogs', 'running', 'fast', 'laughed']
```

**After stemming (Porter Stemmer):**
```
['quick', 'brown', 'fox', 'jump', 'lazi', 'dog', 'run', 'fast', 'laugh']
```
*(Note "lazi" — a known quirk of stemming, which can produce non-dictionary forms.)*

**After lemmatization (verb-based):**
```
['quick', 'brown', 'fox', 'jump', 'lazy', 'dog', 'run', 'fast', 'laugh']
```
*(Lemmatization keeps valid dictionary words, unlike stemming.)*

**Bag-of-words vectorization on a separate corpus:**
```
Corpus: ["the quick brown fox", "the lazy dog sleeps"]
Vocabulary: ['brown', 'dog', 'fox', 'lazy', 'quick', 'sleeps', 'the']
Vectors:
[[1 0 1 0 1 0 1]
 [0 1 0 1 0 1 1]]
```

## Purpose

This notebook is intended as a teaching/reference example illustrating the difference between stemming and lemmatization, and how raw text becomes numeric features suitable for machine learning models.

## Possible Extensions

- Apply stemming/lemmatization directly to the `corpus` before vectorizing.
- Compare `CountVectorizer` output with `TfidfVectorizer` for weighted term importance.
- Combine with a classifier (see `ML_P1.ipynb`) to build a full text classification pipeline.
