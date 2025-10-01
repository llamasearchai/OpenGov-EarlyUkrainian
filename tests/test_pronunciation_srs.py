from opengov_earlyukrainian.core.pronunciation import PronunciationCoach
from opengov_earlyukrainian.core.srs import SRS


def test_pronunciation_features():
    p = PronunciationCoach()
    feat = p.get_feature("apostrophe")
    assert "Blocks palatalization" in feat["rule"]
    pairs = p.sample_pairs()
    assert "Г vs Ґ" in pairs


def test_pronunciation_iotated():
    p = PronunciationCoach()
    feat = p.get_feature("iotated")
    assert "letters" in feat
    assert "я" in feat["letters"]


def test_pronunciation_hard_g():
    p = PronunciationCoach()
    feat = p.get_feature("hard_g")
    assert "Ґ" in feat
    assert "Г" in feat


def test_srs_cycle():
    srs = SRS()
    it = srs.add("n1", "книга (gen.)?", "книги")
    assert it.id == "n1"
    assert it.interval == 1

    after = srs.review("n1", "good")
    assert after.interval >= 2
    assert after.next_review > after.last_review


def test_srs_fail():
    srs = SRS()
    srs.add("n2", "test", "answer")
    after = srs.review("n2", "fail")
    assert after.interval == 1
    assert after.ease < 2.5


def test_srs_easy():
    srs = SRS()
    srs.add("n3", "test", "answer")
    after = srs.review("n3", "easy")
    assert after.interval > 1
    assert after.ease > 2.5


def test_pronunciation_unknown_feature():
    p = PronunciationCoach()
    try:
        p.get_feature("unknown")
        assert False, "Should raise ValueError"
    except ValueError:
        pass


def test_srs_hard():
    """Test SRS 'hard' quality review."""
    srs = SRS()
    srs.add("n4", "test", "answer")
    after = srs.review("n4", "hard")
    assert after.interval >= 1
    assert after.ease <= 2.5

