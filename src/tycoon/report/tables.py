def two_col(rows: list[tuple[str, str]]) -> list[str]:
    return [f"{a:<16}{b}" for a, b in rows]
