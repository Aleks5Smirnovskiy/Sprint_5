from uuid import uuid4

from data import ListingData, UserData


def build_user_credentials():
    return {
        "email": f"autotest_{uuid4().hex}@test.ru",
        "password": UserData.DEFAULT_PASSWORD,
    }


def build_listing_payload():
    suffix = uuid4().hex[:8]
    return {
        "title": f"Autotest listing {suffix}",
        "description": ListingData.DEFAULT_DESCRIPTION,
        "price": ListingData.DEFAULT_PRICE,
        "category": ListingData.DEFAULT_CATEGORY,
        "city": ListingData.DEFAULT_CITY,
        "condition": ListingData.DEFAULT_CONDITION,
    }
