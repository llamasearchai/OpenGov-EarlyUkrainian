from opengov_earlyukrainian.core.business import BusinessUkrainian
from opengov_earlyukrainian.core.culture import CulturalGuide


def test_business_email_template_meeting():
    b = BusinessUkrainian()
    template = b.email_template("meeting")
    assert "subject" in template
    assert "body" in template
    assert "signoff" in template
    assert "зустріч" in template["subject"].lower()


def test_business_email_template_follow_up():
    b = BusinessUkrainian()
    template = b.email_template("follow_up")
    assert "домовленості" in template["body"]


def test_business_phone_phrases():
    b = BusinessUkrainian()
    phrases = b.phone_phrases()
    assert "intro" in phrases
    assert "closing" in phrases
    assert "Доброго дня" in phrases["intro"]


def test_cultural_guide_regions():
    guide = CulturalGuide()
    regions = guide.regions()
    assert len(regions) > 0
    assert "Київщина" in regions


def test_cultural_guide_holidays():
    guide = CulturalGuide()
    holidays = guide.holidays()
    assert "Різдво" in holidays
    assert "День Незалежності" in holidays


def test_cultural_guide_etiquette():
    guide = CulturalGuide()
    etiquette = guide.etiquette()
    assert len(etiquette) > 0
    assert any("української мови" in rule for rule in etiquette)

