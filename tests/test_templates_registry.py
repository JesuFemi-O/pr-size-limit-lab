from tycoon.templates_registry import names


def test_weather_station_registered():
    assert "weather-station" in names()
