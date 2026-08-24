# 📅 Day 1 – Problem Definition & System Designing

> Part of the [Intelligent Email Spam Detection and Filtering System](../README.md) — 3-Day Mini Project Development Documentation.

---

## 1. Problem Definition

### Problem

Email users receive a large number of unsolicited promotional, spam, phishing, and potentially malicious messages.

These emails may contain:

* Phishing attempts
* Credential harvesting
* Financial scams
* Fake offers
* Promotional spam
* Suspicious links
* Urgency-based social engineering

Traditional static keyword and rule-based filters may not handle changing or obfuscated text effectively.

### Objective

The objective of the project is to develop an intelligent desktop application that:

1. Accepts raw email body text.
2. Cleans and preprocesses the text.
3. Converts text into numerical features.
4. Uses a trained ML model to classify the email.
5. Calculates spam probability.
6. Determines the threat level.
7. Generates security recommendations.
8. Displays the result through a graphical interface.
9. Stores analysis results for future reference.

---

## 2. Proposed Solution

The proposed system consists of five major stages:

### Input Layer

The user enters or pastes the email body into the Tkinter interface.

### NLP Layer

The email text is cleaned and normalized before machine learning processing.

### Machine Learning Layer

The processed text is converted into TF-IDF features and classified using the trained Logistic Regression model.

### AI Threat Engine

The spam probability and suspicious text patterns are analyzed to determine the threat level and generate security advice.

### Persistence Layer

The prediction, probability, threat level, and recommendation are stored in `master_email_log.csv`.

This architecture is also reflected in the project's presentation, where the solution is divided into Input, NLP, Machine Learning, Threat Engine, and Persistence components.

---

## 3. System Architecture

```text
┌──────────────────────┐
│      User Input      │
│     Email Body       │
└──────────┬───────────┘
           ↓
┌──────────────────────┐
│   NLP Preprocessing  │
│  clean_sentence()    │
└──────────┬───────────┘
           ↓
┌──────────────────────┐
│    TF-IDF Vectorizer │
│    Unigrams+Bigrams  │
└──────────┬───────────┘
           ↓
┌──────────────────────┐
│   ML Classification  │
│  Logistic Regression │
└──────────┬───────────┘
           ↓
┌──────────────────────┐
│   Spam Probability   │
└──────────┬───────────┘
           ↓
┌──────────────────────┐
│    AI Threat Engine  │
│ Threat + Heuristics  │
└──────────┬───────────┘
           ↓
┌──────────────────────┐
│ Security Recommendation│
└──────────┬───────────┘
           ↓
┌──────────────────────┐
│     Tkinter GUI      │
└──────────┬───────────┘
           ↓
┌──────────────────────┐
│ master_email_log.csv │
└──────────────────────┘
```

The implemented GUI contains a multi-line email input area and **Predict Entry, Clear, and Exit** actions.

---

## 4. Day 1 Deliverables

* Problem statement
* Project objective
* Functional requirements
* Non-functional requirements
* System architecture
* Data-flow/process flow
* GUI design
* Module identification

### Main modules identified

```text
main.py
preprocess_utils.py
train_model.py
spam_rules.py
spam_filter_model_2.pkl
tfidf_vectorizer_2.pkl
master_email_log.csv
```

---

**Next:** [Day 2 – Machine Learning Model →](DAY2_MACHINE_LEARNING_MODEL.md)