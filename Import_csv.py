import csv
import io
from typing import Optional


def parse_csv(data: str) -> list[dict]:
    reader = csv.DictReader(io.StringIO(data))
    return list(reader)


def calculate_item_revenue(row: dict) -> float:
    return float(row["quantity"]) * float(row["price"])


def compute_revenue(rows: list[dict]) -> float:
    return sum(calculate_item_revenue(row) for row in rows)


def top_item(rows: list[dict]) -> Optional[dict]:
    if not rows:
        return None

    return max(rows, key=calculate_item_revenue)


data = """date,item,quantity,price
2026-03-12,phone,4,1000
2025-08-16,notebook,14,88
2024-06-14,beer,100,20
"""

rows = parse_csv(data)

print(compute_revenue(rows))
print(top_item(rows))
print(rows)