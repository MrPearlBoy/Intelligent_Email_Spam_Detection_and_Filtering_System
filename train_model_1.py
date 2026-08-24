import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report
import joblib
from preprocess_utils import clean_sentence

# 1. Load sentence dataset
data = pd.read_csv("emails.csv")

# 2. Clean sentences
data["Clean_Sentence"] = data["text"].apply(clean_sentence)
X = data["Clean_Sentence"]
y = data["spam"]

# 3. Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42, stratify=y)

# 4. Sentence Vectorization (Unigrams + Bigrams)
vectorizer = TfidfVectorizer(stop_words='english', ngram_range=(1, 2), max_features=5000)
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

# 5. Train Model
model = MultinomialNB(alpha=0.5)
model.fit(X_train_vec, y_train)

# 6. Evaluate
y_pred = model.predict(X_test_vec)
print(f"Naive Bayes Accuracy: {accuracy_score(y_test, y_pred) * 100:.2f}%\n")
print(classification_report(y_test, y_pred))

# 7. Save Artifacts
#joblib.dump(model, "spam_filter_model.pkl")
#joblib.dump(vectorizer, "tfidf_vectorizer.pkl")
#print("Saved Naive Bayes model and vectorizer successfully.")