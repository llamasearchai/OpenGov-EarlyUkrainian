import pytest
from opengov_earlyukrainian.core.alphabet import AlphabetTeacher


def test_iotated_row():
    t = AlphabetTeacher()
    row = t.get_row("iotated")
    assert row["letters"] == ["Я", "Ю", "Є", "Ї"]


def test_mnemonic_known_letter():
    t = AlphabetTeacher()
    m = t.mnemonic("Ґ")
    assert "hard g" in m.lower()


def test_basic_row():
    t = AlphabetTeacher()
    row = t.get_row("basic")
    assert "А" in row["letters"]
    assert "Я" not in row["letters"]


def test_vowels_row():
    t = AlphabetTeacher()
    row = t.get_row("vowels")
    assert len(row["letters"]) == 10


def test_unknown_row():
    t = AlphabetTeacher()
    with pytest.raises(ValueError):
        t.get_row("unknown_row")


def test_mnemonic_unknown_letter():
    t = AlphabetTeacher()
    m = t.mnemonic("X")
    assert "No mnemonic available" in m

