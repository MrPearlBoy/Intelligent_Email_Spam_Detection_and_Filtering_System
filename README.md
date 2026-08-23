# Intelligent_Email_Spam_Detection_and_Filtering_System

#### 1. Problem Statement:
- Digital communication is heavily impacted by unsolicited, deceptive, and malicious emails.
- Users struggle to identify phishing and fraudulent scam messages before interacting with them.
- Traditional static keyword filters fail against evolving obfuscation and text manipulations.
- A real-time system is needed to analyze incoming email body text and provide immediate filtering decisions.

#### 2. Proposed Solution:
- Accept raw email body/sentence text directly from the user.
- Preprocess and tokenize text using NLP techniques (lowercasing, punctuation stripping, stop-word removal).
- Extract numerical features using TF-IDF vectorization (unigrams and bigrams).
- Classify the email as Spam or Ham using a Machine Learning classifier (Multinomial Naive Bayes / SVM / Logistic Regression).
- Calculate threat levels and generate actionable security recommendations.
- Display instant results and persist records to a master log via a clean Tkinter GUI.

#### 3. Process Flow:
<p align="center"> Start <br> &darr; <br> Enter Email Sentence / Body Text <br> &darr; <br> Validate Input <br> &darr; <br> Preprocess & TF-IDF Vectorization <br> &darr; <br> ML Model Prediction <br> &darr; <br> Determine Threat Level & Confidence <br> &darr; <br> Generate AI Recommendation <br> &darr; <br> Display Result in GUI & Save to CSV <br> &darr; <br> End</p>

#### 4. Project Mapping:
| V-Model Stage           | Intelligent Email Spam Project               |
|:------------------------|:---------------------------------------------|
| Requirement Analysis    | Identify spam detection from raw body text   |
| System Design           | Design NLP pipeline and single-window GUI    |
| Implementation          | Develop TF-IDF vectorizer + ML models        |
| Integration             | Integrate Tkinter GUI, ML, and AI heuristics | 
| Testing                 | Test text inputs, edge cases, and accuracy   |
| Validation              | Validate precision against false positives   |
| Demonstration           | Present working desktop application          |

### 5. Requirement Analysis
#### 5.1 Functional Requirements
The system should:
+ Accept single email body/sentence inputs via a multi-line text area.
+ Validate that the text input is not empty.
+ Preprocess input text and transform it into TF-IDF vectors.
+ Apply the trained ML classification model.
+ Predict whether the content is Spam or Ham.
+ Calculate spam probability confidence scores.
+ Generate actionable security advice based on threat levels.
+ Log individual results into `master_email_log.csv`.
+ Provide clear and exit options.

#### 5.2 Non Functional Requirements:
The application should be:
+ User-friendly and distraction-free
+ Fast in generating real-time predictions
+ Reliable and consistent
+ Modular and maintainable
+ Lightweight with low memory footprint

#### 5.3 Identify the Users
Primary Users may include:
  + Email Users / Consumers
  + Helpdesk Support Engineers
  + IT Administrators

#### 5.4 User Requirements
The user should be able to:
+ Paste any suspicious or regular email sentence/body text.
+ Click a single button to analyze the message.
+ View the classification verdict (Spam vs. Ham).
+ See the estimated threat severity.
+ Read concrete advice on whether to quarantine, delete, or trust the email.

#### 5.5 Identify System Inputs
+ Email Sentence / Body Text (Raw unstructured text)

#### 5.6 Identify System Outputs
###### 5.6.1 Classification Verdict
  + Spam
  + Ham (Legitimate)

###### 5.6.2 Additional Outputs
  + Spam Probability Confidence (%)
  + Threat Level (High Threat, Moderate Threat, Suspicious, Safe)
  + Actionable AI Recommendation

###### Example
__Prediction:__ Spam (94.20% Spam Probability) \
__Threat Level:__ High Threat (Malicious/Phishing) \
__Recommendation:__ Move to Quarantine immediately; urgent psychological pressure detected — do not click links or share credentials.
