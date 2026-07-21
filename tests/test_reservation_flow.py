import os

from aegis_core import process_user_input
from reservation_store import ReservationStore


def test_accepts_complete_reservation_details():
    result = process_user_input({
        "name": "Ada Lovelace",
        "email": "ada@example.com",
        "phone": "+1 555 123 4567",
        "country": "United States",
        "vehicle": "Aegis One",
    })

    assert result["success"] is True
    assert result["errors"] == []
    assert result["validated_data"]["name"] == "Ada Lovelace"


def test_rejects_invalid_phone_and_missing_country():
    result = process_user_input({
        "name": "A",
        "email": "not-an-email",
        "phone": "abc",
        "country": "",
        "vehicle": "",
    })

    assert result["success"] is False
    assert any("name" in error for error in result["errors"])
    assert any("email" in error for error in result["errors"])
    assert any("phone" in error for error in result["errors"])
    assert any("country" in error for error in result["errors"])
    assert any("vehicle" in error for error in result["errors"])


def test_allows_reservation_without_optional_fields():
    result = process_user_input({
        "name": "Ada Lovelace",
        "email": "ada@example.com",
        "phone": "+1 555 123 4567",
        "country": "United States",
        "vehicle": "Aegis One",
    })

    assert result["success"] is True
    assert result["errors"] == []


def test_store_persists_reservation(tmp_path):
    db_path = tmp_path / "reservations.sqlite"
    store = ReservationStore(str(db_path))

    reservation_id = store.save({
        "name": "Grace Hopper",
        "email": "grace@example.com",
        "phone": "+44 7700 900123",
        "country": "United Kingdom",
        "vehicle": "Aegis R",
    })

    reservations = store.list_reservations()

    assert reservation_id is not None
    assert len(reservations) == 1
    assert reservations[0]["name"] == "Grace Hopper"
    assert reservations[0]["country"] == "United Kingdom"
