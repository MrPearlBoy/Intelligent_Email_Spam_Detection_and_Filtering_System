import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
import joblib
from preprocess_utils import clean_sentence

data = pd.read_csv("emails.csv")
data["Clean_Sentence"] = data["text"].apply(clean_sentence)

X_train, X_test, y_train, y_test = train_test_split(
    data["Clean_Sentence"], data["spam"], test_size=0.35, random_state=42, stratify=data["spam"]
)

vectorizer = TfidfVectorizer(stop_words='english', ngram_range=(1, 2), max_features=5000)
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

model = LogisticRegression(C=2.0, max_iter=1000, random_state=42)
model.fit(X_train_vec, y_train)

y_pred = model.predict(X_test_vec)
print(f"Logistic Regression Accuracy: {accuracy_score(y_test, y_pred) * 100:.2f}%\n")
print(classification_report(y_test, y_pred))
#
joblib.dump(model, "spam_filter_model_2.pkl")
joblib.dump(vectorizer, "tfidf_vectorizer_2.pkl")