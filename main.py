import tkinter as tk
from tkinter import messagebox, scrolledtext
import joblib
import pandas as pd
import os

from preprocess_utils import clean_sentence
from spam_rules import calculate_threat_level, ai_email_feedback

# --- Global Settings ---
MODEL_PATH = "spam_filter_model_2.pkl"
VECTORIZER_PATH = "tfidf_vectorizer_2.pkl"
MASTER_CSV_FILE = "master_email_log.csv"

# --- Load Model & Vectorizer ---
try:
    model = joblib.load(MODEL_PATH)
    vectorizer = joblib.load(VECTORIZER_PATH)
except Exception as e:
    model = None
    vectorizer = None
    print(f"Warning: Model or Vectorizer could not be loaded: {e}")

# --- Initialize Window ---
root = tk.Tk()
root.geometry("900x700")
root.title("Intelligent Email Spam Detection and Filtering System")
root.resizable(True, True)


# --- Helper Functions ---

def append_to_master_csv(df_to_add):
    """Safely append single sentence prediction to the log CSV."""
    if not os.path.exists(MASTER_CSV_FILE):
        df_to_add.to_csv(MASTER_CSV_FILE, mode='w', header=True, index=False)
    else:
        df_to_add.to_csv(MASTER_CSV_FILE, mode='a', header=False, index=False)


# --- Button Actions ---

def predict_sentence_spam():
    """Preprocess single email sentence/body, predict via ML model, and display results."""
    if model is None or vectorizer is None:
        messagebox.showerror(
            "Model Error", 
            "Trained model ('spam_filter_model.pkl') or Vectorizer ('tfidf_vectorizer.pkl') not found.\n"
            "Please run a training script first."
        )
        return

    raw_text = BodyText.get("1.0", tk.END).strip()

    if not raw_text:
        messagebox.showwarning("Missing Input", "Please enter or paste the email sentence/body to analyze.")
        return

    try:
        # 1. Clean and vectorize sentence
        cleaned_text = clean_sentence(raw_text)
        text_vector = vectorizer.transform([cleaned_text])

        # 2. ML Prediction & Probability
        prediction = model.predict(text_vector)[0]
        
        # Check if probability output is supported
        if hasattr(model, "predict_proba"):
            probabilities = model.predict_proba(text_vector)[0]
            classes = list(model.classes_)
            spam_prob = probabilities[classes.index("Spam")] if "Spam" in classes else 0.0
        else:
            spam_prob = 1.0 if prediction == "Spam" else 0.0

        # 3. Threat Assessment & AI Recommendation
        threat_level = calculate_threat_level(prediction, spam_prob)
        recommendation = ai_email_feedback(threat_level, raw_text)

        # 4. Update UI
        pred_color = "#D32F2F" if prediction == "Spam" else "#2E7D32"
        pred_label_value.config(
            text=f"Verdict: {prediction} ({spam_prob * 100:.2f}% Spam Probability)", 
            fg=pred_color
        )
        threat_label_value.config(text=f"Threat Level: {threat_level}")
        recommendation_value.config(text=f"Actionable Advice: {recommendation}")

        # 5. Log Entry to CSV
        record = {
            "Email_Text": raw_text,
            "Prediction": prediction,
            "Spam_Probability": f"{spam_prob * 100:.2f}%",
            "Threat_Level": threat_level,
            "Recommendation": recommendation
        }
        append_to_master_csv(pd.DataFrame([record]))

        # 6. Inform user
        if "High Threat" in threat_level:
            messagebox.showwarning(
                "High Threat Detected", 
                f"Warning: High-threat spam content detected!\nResult saved to '{MASTER_CSV_FILE}'."
            )
        else:
            messagebox.showinfo("Analysis Complete", f"Result saved to '{MASTER_CSV_FILE}'.")

    except Exception as err:
        messagebox.showerror("Inference Error", f"Failed to classify input:\n{err}")


def clear_fields():
    """Reset text entry and results."""
    BodyText.delete("1.0", tk.END)
    pred_label_value.config(text="Verdict: None", fg="black")
    threat_label_value.config(text="Threat Level: None")
    recommendation_value.config(text="Actionable Advice: None")
    BodyText.focus()


def exit_application():
    """Confirm before closing the application."""
    if messagebox.askyesno("Exit Application", "Are you sure you want to exit?"):
        root.destroy()


# --- UI Layout ---

main_frame = tk.Frame(root)
main_frame.pack(fill="both", expand=True, padx=30, pady=20)

heading = tk.Label(
    main_frame, 
    text="Intelligent Email Spam Detection and Filtering System", 
    font=("Times New Roman", 18, "bold")
)
heading.pack(pady=(0, 15))

# Input Frame
input_frame = tk.LabelFrame(
    main_frame, 
    text="Email Sentence / Body Input", 
    font=("Times New Roman", 13, "bold"), 
    padx=15, 
    pady=15
)
input_frame.pack(fill="both", expand=True, pady=5)

BodyText = scrolledtext.ScrolledText(input_frame, font=("Times New Roman", 11), wrap=tk.WORD, height=8)
BodyText.pack(fill="both", expand=True)

# Button Frame
button_frame = tk.Frame(main_frame)
button_frame.pack(pady=15)

predict_btn = tk.Button(
    button_frame, 
    text="Predict Entry", 
    command=predict_sentence_spam, 
    font=("Times New Roman", 11, "bold"), 
    width=14, 
    fg="blue"
)
predict_btn.pack(side="left", padx=8)

clear_btn = tk.Button(
    button_frame, 
    text="Clear", 
    command=clear_fields, 
    font=("Times New Roman", 11, "bold"), 
    width=10, 
    fg="green"
)
clear_btn.pack(side="left", padx=8)

exit_btn = tk.Button(
    button_frame, 
    text="Exit", 
    command=exit_application, 
    font=("Times New Roman", 11, "bold"), 
    width=10, 
    fg="red"
)
exit_btn.pack(side="left", padx=8)

# Result Frame
result_frame = tk.LabelFrame(
    main_frame, 
    text="Analysis & AI Recommendation Result", 
    font=("Times New Roman", 13, "bold"), 
    padx=20, 
    pady=15
)
result_frame.pack(fill="x", pady=10)

pred_label_value = tk.Label(result_frame, text="Verdict: None", font=("Times New Roman", 12, "bold"), anchor="w")
pred_label_value.pack(anchor="w", pady=3)

threat_label_value = tk.Label(result_frame, text="Threat Level: None", font=("Times New Roman", 11), anchor="w")
threat_label_value.pack(anchor="w", pady=3)

recommendation_value = tk.Label(
    result_frame, 
    text="Actionable Advice: None", 
    font=("Times New Roman", 11), 
    anchor="w", 
    wraplength=800, 
    justify="left"
)
recommendation_value.pack(anchor="w", pady=3)

root.mainloop()