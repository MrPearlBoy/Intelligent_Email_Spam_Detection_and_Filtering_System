import re

def clean_sentence(text):
    """Clean raw sentence text for NLP vectorization."""
    if not isinstance(text, str):
        return ""
    # Convert to lowercase
    text = text.lower()
    # Normalize URLs
    text = re.sub(r'https?://\S+|www\.\S+', ' urltoken ', text)
    # Normalize Currency / Numbers
    text = re.sub(r'[$£€¥]\d+', ' moneytoken ', text)
    text = re.sub(r'\b\d+\b', ' numtoken ', text)
    # Remove non-alphabet characters (keep spaces)
    text = re.sub(r'[^a-z\s]', ' ', text)
    # Remove excessive whitespace
    text = re.sub(r'\s+', ' ', text).strip()
    return text