import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LogisticRegression
from sklearn.svm import LinearSVC
from sklearn.calibration import CalibratedClassifierCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import joblib
from preprocess_utils import clean_sentence

# 1. Load and clean sentence data
data = pd.read_csv("emails.csv")
data["Clean_Sentence"] = data["text"].apply(clean_sentence)

X = data["Clean_Sentence"]
y = data["spam"]

# 2. Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42, stratify=y)

# 3. Vectorize sentence phrases
vectorizer = TfidfVectorizer(stop_words='english', ngram_range=(1, 2), max_features=5000)
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

# 4. Models to evaluate
models = {
    "Multinomial Naive Bayes": MultinomialNB(alpha=0.5),
    "Logistic Regression": LogisticRegression(C=2.0, max_iter=1000, random_state=42),
    "Support Vector Machine": CalibratedClassifierCV(LinearSVC(random_state=42, dual='auto')),
    "Random Forest": RandomForestClassifier(n_estimators=150, max_depth=25, random_state=42),
    "Decision Tree": DecisionTreeClassifier(max_depth=20, random_state=42)
}

# 5. Evaluate all models
records = []
best_acc = -1.0
best_model = None
best_model_name = ""

for name, clf in models.items():
    clf.fit(X_train_vec, y_train)
    preds = clf.predict(X_test_vec)

    acc = accuracy_score(y_test, preds)
    prec = precision_score(y_test, preds, pos_label=1, zero_division=0)
    rec = recall_score(y_test, preds, pos_label=1, zero_division=0)
    f1 = f1_score(y_test, preds, pos_label=1, zero_division=0)

    records.append({
        "Algorithm": name,
        "Accuracy (%)": round(acc * 100, 2),
        "Precision (%)": round(prec * 100, 2),
        "Recall (%)": round(rec * 100, 2),
        "F1-Score (%)": round(f1 * 100, 2)
    })

    if acc > best_acc:
        best_acc = acc
        best_model = clf
        best_model_name = name

# 6. Display comparison table
summary_df = pd.DataFrame(records).sort_values(by="Accuracy (%)", ascending=False)
print("\n" + "=" * 68)
print("           SENTENCE SPAM CLASSIFICATION BENCHMARK")
print("=" * 68)
print(summary_df.to_string(index=False))
print("=" * 68)

# 7. Save top-performing model
#joblib.dump(best_model, "spam_filter_model.pkl")
#joblib.dump(vectorizer, "tfidf_vectorizer.pkl")
#print(f"\n[+] Highest performing model: {best_model_name} ({best_acc * 100:.2f}%)")
#print("[+] Serialized 'spam_filter_model.pkl' & 'tfidf_vectorizer.pkl' for single-sentence UI inference.")