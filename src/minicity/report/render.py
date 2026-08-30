def render_summary(summary: dict) -> list[str]:
    return [f"{k:>12}: {v}" for k, v in summary.items()]
