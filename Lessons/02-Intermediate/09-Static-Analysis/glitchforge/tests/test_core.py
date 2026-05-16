from glitchforge.core import ForgeConfig, forge_records, parse_token


def test_parse_token():
    assert parse_token("abc-12") == ("abc", 12)


def test_forge_records_returns_count():
    rows = forge_records(2, ForgeConfig(seed=1, labels=["A", "b"]))
    assert len(rows) == 2
    assert rows[0]["tags"] == ["a", "b"]
