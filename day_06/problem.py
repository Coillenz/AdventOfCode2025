from typing import TypedDict, Literal

class Problem(TypedDict):
  numbers: list[int]
  operator: Literal['+', '*']