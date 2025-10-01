import pytest
from fastapi.testclient import TestClient
from opengov_earlyukrainian.api.main import app

client = TestClient(app)


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"
    assert "version" in data


def test_decline_endpoint():
    response = client.post("/decline", json={"noun": "книга", "gender": "feminine"})
    assert response.status_code == 200
    data = response.json()
    assert data["знахідний"] == "книгу"


def test_conjugate_endpoint():
    response = client.post("/conjugate", json={"verb": "читати", "tense": "present"})
    assert response.status_code == 200
    data = response.json()
    assert "forms" in data
    assert "я" in data["forms"]


def test_transliterate_endpoint():
    response = client.post("/transliterate", json={"text": "Kyiv"})
    assert response.status_code == 200
    data = response.json()
    assert "ukrainian" in data
    # Phonetic transliteration: "Kyiv" → "Кїв"
    assert "кїв" in data["ukrainian"].lower()


def test_alphabet_endpoint():
    response = client.get("/alphabet/iotated")
    assert response.status_code == 200
    data = response.json()
    assert "letters" in data
    assert "Я" in data["letters"]


def test_chat_endpoint():
    response = client.post(
        "/chat", json={"utterance": "Привіт", "level": "A1", "formal": True}
    )
    assert response.status_code == 200
    data = response.json()
    assert "ukrainian" in data

