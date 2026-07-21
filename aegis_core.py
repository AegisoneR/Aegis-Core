import re
from typing import Any, Dict, List


EMAIL_PATTERN = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")
PHONE_PATTERN = re.compile(r"^\+?[0-9\s()-]{7,20}$")


def process_user_input(data: Dict[str, Any]) -> Dict[str, Any]:
    """Validate reservation and account input and return a structured response."""
    name = str(data.get("name", "")).strip()
    email = str(data.get("email", "")).strip()
    phone = str(data.get("phone", "")).strip()
    country = str(data.get("country", "")).strip()
    vehicle = str(data.get("vehicle", "")).strip()
    usage = str(data.get("usage", "")).strip()
    timeline = str(data.get("timeline", "")).strip()
    consent = bool(data.get("consent", False))
    password = str(data.get("password", "")).strip()

    errors: List[str] = []
    reservation_mode = any(key in data for key in ("name", "phone", "country", "vehicle"))

    if reservation_mode:
        if len(name) < 2:
            errors.append("name: must include at least 2 characters")

        if not EMAIL_PATTERN.match(email):
            errors.append("email: invalid email address")

        if not PHONE_PATTERN.match(phone):
            errors.append("phone: invalid phone number")

        if not country:
            errors.append("country: country is required")

        if not vehicle:
            errors.append("vehicle: please select an Aegis model")
    else:
        if not EMAIL_PATTERN.match(email):
            errors.append("email: invalid email address")

        if password and len(password) < 8:
            errors.append("password: must be at least 8 characters")

    return {
        "success": not errors,
        "errors": errors,
        "validated_data": {
            "name": name,
            "email": email,
            "phone": phone,
            "country": country,
            "vehicle": vehicle,
            "usage": usage,
            "timeline": timeline,
            "consent": consent,
            "password": password,
        },
    }
