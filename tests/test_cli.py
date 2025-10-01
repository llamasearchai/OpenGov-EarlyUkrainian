import pytest
from typer.testing import CliRunner
from opengov_earlyukrainian.cli import app

runner = CliRunner()


def test_cli_alphabet_iotated():
    result = runner.invoke(app, ["alphabet", "iotated"])
    assert result.exit_code == 0
    assert "Alphabet Row" in result.stdout
    assert "Я" in result.stdout or "я" in result.stdout


def test_cli_alphabet_basic():
    result = runner.invoke(app, ["alphabet", "basic"])
    assert result.exit_code == 0
    assert "Alphabet Row" in result.stdout


def test_cli_alphabet_vowels():
    result = runner.invoke(app, ["alphabet", "vowels"])
    assert result.exit_code == 0
    assert "Alphabet Row" in result.stdout


def test_cli_decline_feminine():
    result = runner.invoke(app, ["decline", "книга", "feminine"])
    assert result.exit_code == 0
    assert "Declension" in result.stdout
    assert "книга" in result.stdout


def test_cli_decline_masculine():
    result = runner.invoke(app, ["decline", "паспорт", "masculine"])
    assert result.exit_code == 0
    assert "Declension" in result.stdout
    assert "паспорт" in result.stdout


def test_cli_decline_neuter():
    result = runner.invoke(app, ["decline", "місто", "neuter"])
    assert result.exit_code == 0
    assert "Declension" in result.stdout
    assert "місто" in result.stdout


def test_cli_conjugate_present():
    result = runner.invoke(app, ["conjugate", "читати"])
    assert result.exit_code == 0
    assert "Conjugation" in result.stdout
    assert "читати" in result.stdout


def test_cli_conjugate_present_explicit():
    result = runner.invoke(app, ["conjugate", "читати", "--tense", "present"])
    assert result.exit_code == 0
    assert "Conjugation" in result.stdout


def test_cli_conjugate_past():
    result = runner.invoke(app, ["conjugate", "бути", "--tense", "past"])
    assert result.exit_code == 0
    assert "Conjugation" in result.stdout


def test_cli_conjugate_unknown():
    result = runner.invoke(app, ["conjugate", "unknown_verb", "--tense", "future"])
    assert result.exit_code == 0
    # Should handle gracefully


def test_cli_translit_basic():
    result = runner.invoke(app, ["translit", "Hello"])
    assert result.exit_code == 0
    assert "Latin" in result.stdout
    assert "Ukrainian" in result.stdout


def test_cli_translit_kyiv():
    result = runner.invoke(app, ["translit", "Kyiv"])
    assert result.exit_code == 0
    assert "Ukrainian" in result.stdout


def test_cli_aspect():
    result = runner.invoke(app, ["aspect", "читати"])
    assert result.exit_code == 0
    assert "Imperfective" in result.stdout
    assert "Perfective" in result.stdout
    assert "читати" in result.stdout


def test_cli_aspect_unknown():
    result = runner.invoke(app, ["aspect", "unknown_verb"])
    assert result.exit_code == 0
    assert "по-" in result.stdout


def test_cli_business_meeting():
    result = runner.invoke(app, ["business"])
    assert result.exit_code == 0
    assert "Business Template" in result.stdout
    assert "Subject" in result.stdout


def test_cli_business_follow_up():
    result = runner.invoke(app, ["business", "--purpose", "follow_up"])
    assert result.exit_code == 0
    assert "Business Template" in result.stdout
    assert "Subject" in result.stdout


def test_cli_culture():
    result = runner.invoke(app, ["culture"])
    assert result.exit_code == 0
    assert "Regions" in result.stdout or "regions" in result.stdout
    assert "Holidays" in result.stdout or "holidays" in result.stdout


def test_cli_version():
    result = runner.invoke(app, ["version"])
    assert result.exit_code == 0
    assert "OpenGov-EarlyUkrainian" in result.stdout
    assert "Nik Jois" in result.stdout


def test_cli_help():
    result = runner.invoke(app, ["--help"])
    assert result.exit_code == 0
    assert "Ukrainian Language Learning Platform" in result.stdout


def test_cli_alphabet_help():
    result = runner.invoke(app, ["alphabet", "--help"])
    assert result.exit_code == 0
    assert "Display Ukrainian alphabet" in result.stdout


def test_cli_decline_help():
    result = runner.invoke(app, ["decline", "--help"])
    assert result.exit_code == 0
    assert "Decline a Ukrainian noun" in result.stdout


def test_cli_conjugate_help():
    result = runner.invoke(app, ["conjugate", "--help"])
    assert result.exit_code == 0
    assert "Conjugate a Ukrainian verb" in result.stdout


def test_cli_translit_help():
    result = runner.invoke(app, ["translit", "--help"])
    assert result.exit_code == 0
    assert "Transliterate" in result.stdout


def test_cli_aspect_help():
    result = runner.invoke(app, ["aspect", "--help"])
    assert result.exit_code == 0
    assert "aspect pair" in result.stdout


def test_cli_business_help():
    result = runner.invoke(app, ["business", "--help"])
    assert result.exit_code == 0
    assert "business" in result.stdout.lower()


def test_cli_culture_help():
    result = runner.invoke(app, ["culture", "--help"])
    assert result.exit_code == 0
    assert "cultural" in result.stdout.lower()

