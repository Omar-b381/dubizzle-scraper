import re

def clean_text(text):
    """Clean text by removing extra whitespace and standardizing."""
    return re.sub(r'\s+', ' ', text).strip() if text else None