from datetime import date
import re


def validate_email(email: str) -> bool:
    """Check if an email address is valid."""
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return bool(re.match(pattern, email))


def validate_date(value: str) -> bool:
    """Check if a date string is in YYYY-MM-DD format."""
    pattern = r'^\d{4}-\d{2}-\d{2}$'
    return bool(re.match(pattern, value))


def validate_not_empty(value: str, field_name: str) -> str:
    """Strip whitespace and raise an error if the value is empty."""
    value = value.strip()
    if not value:
        raise ValueError(f"{field_name} cannot be empty.")
    return value
