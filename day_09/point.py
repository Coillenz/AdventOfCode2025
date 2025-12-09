from typing import Self
from dataclasses import dataclass

@dataclass
class Point:
    x: int
    y: int

    def get_area(self, other: Self) -> int:
        return (abs(self.x - other.x) + 1) * (abs(self.y - other.y) + 1)