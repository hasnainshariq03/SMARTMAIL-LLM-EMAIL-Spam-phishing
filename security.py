def validate_email_text(text, max_chars=12000):
    if not isinstance(text, str):
        raise ValueError("Email content must be text.")
    text = text.strip()
    if not text:
        raise ValueError("Please paste an email before analyzing it.")
    if len(text) > max_chars:
        raise ValueError(f"Email is too long. Maximum length is {max_chars:,} characters.")
    return True

def redact_for_logs(text):
    """Placeholder helper: safest default is not to log email content at all."""
    return "[EMAIL CONTENT REDACTED]"
