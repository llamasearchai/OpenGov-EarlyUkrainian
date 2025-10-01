from dataclasses import dataclass, field
from datetime import UTC, datetime, timedelta
from typing import Dict


@dataclass
class ReviewItem:
    id: str
    prompt: str
    answer: str
    interval: int = 1
    ease: float = 2.5
    reps: int = 0
    last_review: datetime = field(default_factory=lambda: datetime.now(UTC))
    next_review: datetime = field(
        default_factory=lambda: datetime.now(UTC) + timedelta(days=1)
    )


class SRS:
    def __init__(self) -> None:
        self.items: Dict[str, ReviewItem] = {}

    def add(self, item_id: str, prompt: str, answer: str) -> ReviewItem:
        it = ReviewItem(id=item_id, prompt=prompt, answer=answer)
        self.items[item_id] = it
        return it

    def review(self, item_id: str, quality: str) -> ReviewItem:
        it = self.items[item_id]
        it.reps += 1
        if quality == "fail":
            it.interval = 1
            it.ease = max(1.3, it.ease - 0.2)
        elif quality == "hard":
            it.interval = max(1, int(it.interval * 1.2))
            it.ease = max(1.3, it.ease - 0.05)
        elif quality == "good":
            it.interval = int(it.interval * it.ease)
        elif quality == "easy":
            it.interval = int(it.interval * (it.ease + 0.15))
            it.ease = min(3.0, it.ease + 0.05)
        it.last_review = datetime.now(UTC)
        it.next_review = it.last_review + timedelta(days=max(1, it.interval))
        return it

