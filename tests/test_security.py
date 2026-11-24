import pytest
from security import validate_email_text, redact_for_logs

def test_valid_text():
    assert validate_email_text("Hello, this is an email.") is True

def test_empty_text_rejected():
    with pytest.raises(ValueError):
        validate_email_text("   ")

def test_non_string_rejected():
    with pytest.raises(ValueError):
        validate_email_text(None)

def test_long_text_rejected():
    with pytest.raises(ValueError):
        validate_email_text("x" * 11, max_chars=10)

def test_redaction_helper():
    assert redact_for_logs("private message") == "[EMAIL CONTENT REDACTED]"
