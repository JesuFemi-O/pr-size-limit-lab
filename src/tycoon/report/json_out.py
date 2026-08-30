import json


def dumps(summary: dict) -> str:
    return json.dumps(summary, indent=2)
