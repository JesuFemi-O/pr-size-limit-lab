from minicity.report import render_summary


def test_render_summary():
    assert render_summary({"a": 1})[0].strip() == "a: 1"
