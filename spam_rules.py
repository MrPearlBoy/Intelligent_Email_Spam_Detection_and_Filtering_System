import re

def calculate_threat_level(prediction_label, spam_prob):
    """Determine threat category based on ML probability."""
    if prediction_label == "Spam":
        if spam_prob >= 0.85:
            return "High Threat (Malicious/Phishing)"
        elif spam_prob >= 0.60:
            return "Moderate Threat (Promotional Spam)"
        else:
            return "Suspicious / Low Threat"
    else:
        return "Safe (Legitimate)"


def ai_email_feedback(threat_level, email_text):
    """Generate automated security feedback and quarantine suggestions based on email text only."""
    suggestions = []
    text_lower = email_text.lower()

    # 1. Base threat advice
    if "High Threat" in threat_level:
        suggestions.append("Move to Quarantine immediately; potential credential harvesting or scam.")
    elif "Moderate Threat" in threat_level:
        suggestions.append("Mark as Spam and move to Junk folder.")
    elif "Suspicious" in threat_level:
        suggestions.append("Flag with warning banner; verify sender authenticity before opening.")
    else:
        suggestions.append("Legitimate email; route to Inbox.")

    # 2. Check for suspicious financial/urgency keywords
    urgency_keywords = ["urgent", "immediately", "account locked", "compromised", "verify your identity", "suspended"]
    if any(keyword in text_lower for keyword in urgency_keywords):
        suggestions.append("Urgent psychological pressure detected — do not click links or share credentials.")

    # 3. Check for monetary/lottery keywords
    money_keywords = ["won", "lottery", "prize", "cash", "loan", "bitcoin", "investment", "guaranteed"]
    if any(keyword in text_lower for keyword in money_keywords):
        suggestions.append("Unsolicited financial lure or giveaway detected.")

    # 4. Check for external URLs
    if re.search(r"https?://\S+|www\.\S+", email_text):
        suggestions.append("External hyperlink detected — scan URL before clicking.")

    return " | ".join(suggestions)