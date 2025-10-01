from opengov_earlyukrainian.core.cases import CasesTeacher


def test_decline_feminine_a():
    c = CasesTeacher()
    table = c.decline_noun("книга", "feminine")
    assert table["знахідний"] == "книгу"
    assert table["орудний"].endswith("ою")
    assert table["називний"] == "книга"
    assert table["родовий"] == "книги"


def test_decline_masc_simple():
    c = CasesTeacher()
    table = c.decline_noun("паспорт", "masculine")
    assert table["родовий"] == "паспорта"
    assert table["місцевий"] == "паспорті"
    # inanimate accusative equals nominative
    assert table["знахідний"] == "паспорт"


def test_decline_neuter():
    c = CasesTeacher()
    table = c.decline_noun("місто", "neuter")
    assert table["родовий"] == "міста"
    assert table["знахідний"] == "місто"
    assert table["місцевий"] == "місті"


def test_decline_feminine_ya():
    c = CasesTeacher()
    table = c.decline_noun("земля", "feminine")
    assert table["родовий"] == "землї"
    assert table["знахідний"] == "землю"


def test_all_cases_present():
    c = CasesTeacher()
    table = c.decline_noun("книга", "feminine")
    for case in c.cases_order:
        assert case in table


def test_decline_unknown_pattern():
    """Test declension fallback for unknown patterns."""
    c = CasesTeacher()
    table = c.decline_noun("xyz", "unknown")
    assert table["називний"] == "xyz"
    # Other cases should have fallback
    assert "?" in table["родовий"]

