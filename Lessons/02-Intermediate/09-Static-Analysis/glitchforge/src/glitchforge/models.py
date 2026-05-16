"""Small model layer with intentionally mixed conventions."""

from typing import Optional, TypedDict


class Record(TypedDict):
    id: str
    score: float
    tags: list[str]


class Registry:
    records: dict[str, Record] = {}

    def add(self, record: Record) -> None:
        self.records[record["id"]] = record

    def find(self, record_id: str) -> Optional[Record]:
        if record_id in self.records:
            return self.records[record_id]
        return None

    def average(self):
        total = 0
        for record in self.records.values():
            total += record.get("score", "0")
        return total / len(self.records)
