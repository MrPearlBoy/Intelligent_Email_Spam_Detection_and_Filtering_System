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
# 📅 Day 2 – Machine Learning Model

> Part of the [Intelligent Email Spam Detection and Filtering System](../README.md) — 3-Day Mini Project Development Documentation.
>
> **Previous:** [Day 1 – Problem Definition & System Design](DAY1_PROBLEM_DEFINITION_AND_SYSTEM_DESIGN.md)

---

## 1. Dataset Preparation

The project uses `emails.csv` containing labeled email text for training.

The dataset is processed using:

```python
data = pd.read_csv("emails.csv")
data["Clean_Sentence"] = data["text"].apply(clean_sentence)
```

The training data is divided into training and testing sets using:

```python
train_test_split(
    test_size=0.35,
    random_state=42,
    stratify=data["spam"]
)
```

The project therefore uses **65% training data and 35% testing data**.

---

## 2. NLP Preprocessing

The `clean_sentence()` function prepares raw email text before feature extraction.

The preprocessing includes:

* Lowercase conversion
* URL normalization
* Currency normalization
* Number normalization
* Removal of non-alphabetic characters
* Whitespace normalization

For example:

```text
https://example.com
        ↓
urltoken
```

```text
$500
        ↓
moneytoken
```

```text
12345
        ↓
numtoken
```

These preprocessing operations are implemented in `preprocess_utils.py`.

---

## 3. TF-IDF Feature Extraction

Machine learning algorithms cannot directly process raw sentences, so the cleaned email text is converted into numerical features.

The project uses:

```python
TfidfVectorizer(
    stop_words='english',
    ngram_range=(1, 2),
    max_features=5000
)
```

### Configuration

| Parameter          | Value              |
| ------------------ | ------------------ |
| Feature extraction | TF-IDF             |
| Stop words         | English            |
| N-grams            | Unigrams + Bigrams |
| Maximum features   | 5000               |

Unigrams capture individual terms, while bigrams capture contextual phrases such as **"claim prize"** and **"account locked"**.

---

## 4. Machine Learning Algorithm

### Logistic Regression

The project uses **Logistic Regression** as the final classification model.

```python
model = LogisticRegression(
    C=2.0,
    max_iter=1000,
    random_state=42
)

model.fit(X_train_vec, y_train)
```

The model performs binary classification:

```text
Email
  ↓
TF-IDF Features
  ↓
Logistic Regression
  ↓
Spam / Legitimate
```

The training configuration and model artifact generation are documented in the project materials.

---

## 5. Model Evaluation

The trained model is evaluated using:

```python
accuracy_score()
classification_report()
```

The evaluation provides:

* Accuracy
* Precision
* Recall
* F1-score
* Classification report

The trained model and TF-IDF vectorizer are then serialized using Joblib:

```text
spam_filter_model_2.pkl
tfidf_vectorizer_2.pkl
```

These files allow the application to perform prediction without retraining the model every time.

---

## 6. Day 2 Deliverables

* Dataset preparation
* Text preprocessing
* TF-IDF feature extraction
* Train/test split
* Logistic Regression training
* Model evaluation
* Model serialization
* Vectorizer serialization

### Day 2 Output

```text
emails.csv
     ↓
Preprocessing
     ↓
TF-IDF
     ↓
Logistic Regression
     ↓
spam_filter_model_2.pkl

TF-IDF Vectorizer
     ↓
tfidf_vectorizer_2.pkl
```

---


