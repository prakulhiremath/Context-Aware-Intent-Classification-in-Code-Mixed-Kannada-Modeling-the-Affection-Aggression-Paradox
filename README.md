# Context-Aware Intent Classification in Code-Mixed Kannada

### Modeling the Affection–Aggression Paradox

---

## Overview

This project focuses on understanding **intent in code-mixed Kannada conversations**, where the same expressions may indicate either hostility or social closeness depending on context.

Existing hate speech and toxicity models often rely on surface-level signals and fail in such settings. This work introduces a **context-aware, role-based framework** to better capture real conversational intent.

---

## Problem Statement

In regions like Belagavi–Dharwad, colloquial speech often includes words that appear aggressive but are used among friends in an affectionate or neutral manner.

Example:

* “lo maga yen drama madtidya”
  → Could be friendly teasing or actual aggression

Standard NLP models:

* Misclassify such cases as toxic
* Ignore speaker relationship and conversational context

---

## Objectives

* Build a **high-quality annotated dataset** of code-mixed Kannada text
* Introduce a **new intent category: Affectionate Aggression**
* Develop **role-aware and context-aware classification models**
* Evaluate how current models fail and propose improvements

---

## Key Contributions

* Novel **label taxonomy** capturing pragmatic intent
* Introduction of **Affectionate Aggression** as a distinct class
* **Role-based annotation framework**
* Dataset focused on **underrepresented regional language use**
* Baseline models for multi-class intent classification

---

## Label Schema

### Intent Labels

* `HATE_SPEAKER` — explicit hostile or abusive intent
* `TARGET_GROUP` — identifies the target of hate
* `DEFENDER` — supports or defends a target
* `COUNTER_SPEECH` — actively opposes hate
* `AMPLIFIER` — reinforces or spreads harmful content
* `NEUTRAL` — no clear emotional or harmful intent
* `AFFECTIONATE_AGGRESSION` — aggressive wording used in a friendly/social context

---

## Data Format

Each entry is stored in JSONL format:

```json
{
  "text": "lo maga yen drama madtidya",
  "label": "AFFECTIONATE_AGGRESSION",
  "role": "NEUTRAL",
  "context": null,
  "language_mix": "code-mixed"
}
```

---

## Repository Structure

```
repo/
│── data/
│   ├── raw/
│   ├── processed/
│   └── annotations/
│
│── src/
│   ├── data/
│   ├── models/
│   ├── training/
│   └── evaluation/
│
│── notebooks/
│── configs/
│── results/
│── docs/
│
│── README.md
│── requirements.txt
│── .gitignore
```

---

## Methodology

### 1. Data Collection

* Collect conversational text from regional sources
* Focus on Kannada-English code-mixed usage

### 2. Annotation

* Manual labeling with clear guidelines
* Multi-label structure: intent + role + context

### 3. Modeling

* Baseline: transformer-based classification
* Multi-class intent prediction

### 4. Evaluation

* Accuracy, F1-score (macro + weighted)
* Error analysis on misclassified cases

---

## Why This Matters

* Improves fairness in NLP systems
* Reduces false positives in moderation tools
* Captures **real conversational nuance**
* Supports research in multilingual and low-resource settings

---

## Challenges

* Ambiguity in intent interpretation
* Annotator disagreement
* Code-mixing complexity
* Limited existing datasets

---

## Roadmap

### Phase 1

* [ ] Collect 200–500 samples
* [ ] Define annotation guidelines
* [ ] Initial labeling

### Phase 2

* [ ] Expand dataset (1000+)
* [ ] Validate annotation consistency

### Phase 3

* [ ] Train baseline models
* [ ] Perform error analysis

### Phase 4

* [ ] Improve context modeling
* [ ] Prepare for publication

---

## Installation

```bash
pip install -r requirements.txt
```

---

## Usage (Planned)

```bash
python train.py
python evaluate.py
```

---

## Future Work

* Incorporate **conversation-level context modeling**
* Extend to other Indian languages
* Explore graph-based or dialogue-aware models

---

## License

To be decided

---

## Acknowledgment

This work is motivated by real conversational patterns in regional Indian language communities and aims to bridge the gap between linguistic nuance and machine understanding.

---
