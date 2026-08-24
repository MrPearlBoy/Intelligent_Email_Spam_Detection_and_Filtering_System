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
# 📅 Day 3 – AI Integration

> Part of the [Intelligent Email Spam Detection and Filtering System](../README.md) — 3-Day Mini Project Development Documentation.
>
> **Previous:** [Day 2 – Machine Learning Model](DAY2_MACHINE_LEARNING_MODEL.md)

---

## 1. Machine Learning + AI Integration

On Day 3, the trained ML model is integrated into the desktop application.

The application loads:

```python
model = joblib.load("spam_filter_model_2.pkl")
vectorizer = joblib.load("tfidf_vectorizer_2.pkl")
```

The application then accepts new email text and performs real-time inference.

The actual application code loads both serialized artifacts before performing prediction.

---

## 2. Real-Time Prediction

When the user clicks **Predict Entry**, the system performs the following operations:

```text
Raw Email
    ↓
clean_sentence()
    ↓
TF-IDF transform
    ↓
model.predict()
    ↓
Spam / Legitimate
    ↓
model.predict_proba()
    ↓
Spam Probability
```

The application also calculates the spam probability using the model's probability output.

---

## 3. AI Threat Engine

The ML prediction is enhanced with a security-oriented threat analysis layer.

The system categorizes emails into four levels:

| Spam Probability | Threat Level            | Recommended Action |
| ---------------- | ------------------------ | ------------------- |
| ≥ 85%             | High Threat              | Move to Quarantine  |
| ≥ 60% and < 85%   | Moderate Threat           | Mark as Spam/Junk   |
| < 60% Spam        | Suspicious / Low Threat   | Verify Sender       |
| Legitimate        | Safe                      | Route to Inbox      |

These thresholds are implemented in the project's threat-analysis module.

---

## 4. Security Heuristics

In addition to the ML probability, the AI threat engine examines suspicious patterns.

### Urgency Indicators

The system checks terms such as:

```text
urgent
immediately
account locked
compromised
verify your identity
suspended
```

### Financial Indicators

It also checks for terms such as:

```text
won
lottery
prize
cash
loan
bitcoin
investment
guaranteed
```

### URL Detection

External links such as:

```text
http://...
https://...
www....
```

are detected and the user is advised to scan the URL before clicking.

These security heuristics are documented in the project implementation.

---

## 5. AI Recommendation Generation

The threat engine generates actionable recommendations.

Examples:

### High Threat

```text
Move to Quarantine immediately;
potential credential harvesting or scam.
```

### Moderate Threat

```text
Mark as Spam and move to Junk folder.
```

### Suspicious

```text
Flag with warning banner;
verify sender authenticity before opening.
```

### Safe

```text
Legitimate email; route to Inbox.
```

The system can also add additional warnings when urgency, financial lure, or external URL patterns are detected.

---

## 6. GUI Integration

The Tkinter GUI displays:

```text
Verdict:
Spam Probability:
Threat Level:
Actionable Advice:
```

The actual implementation creates an **Analysis & AI Recommendation Result** section containing the verdict, threat level, and recommendation.

### Example

```text
Verdict: Spam
Spam Probability: 94.32%

Threat Level:
High Threat (Malicious/Phishing)

Actionable Advice:
Move to Quarantine immediately;
potential credential harvesting or scam.
```

---

## 7. Result Logging

Every analysis is stored in:

```text
master_email_log.csv
```

The stored information includes:

```text
Email_Text
Prediction
Spam_Probability
Threat_Level
Recommendation
```

This provides a historical record of analyzed emails. The project presentation also specifies that the email text, prediction, probability, threat level, and recommendation are appended to the CSV log.

---

**Back to:** [Main README](../README.md)


