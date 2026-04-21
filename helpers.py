from uuid import uuid4

from data import ApplicationConstants


def build_user_credentials():
    return {
        "email": f"autotest_{uuid4().hex}@test.ru",
        "password": ApplicationConstants.DEFAULT_PASSWORD,
    }


def build_listing_payload():
    suffix = uuid4().hex[:8]
    return {
        "title": f"Autotest listing {suffix}",
        "description": "Описание товара для автотеста",
        "price": "12345",
        "category": "Книги",
        "city": "Казань",
        "condition": "Б/У",
    }
