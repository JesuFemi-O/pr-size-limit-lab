from minicity.templates_registry import names


def test_weather_registered():
    assert "weather" in names()
