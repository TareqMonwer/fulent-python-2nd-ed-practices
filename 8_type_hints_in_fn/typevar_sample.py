from collections.abc import Sequence
from dataclasses import dataclass
from random import shuffle
from typing import TypeVar, Optional

T = TypeVar('T')

def sample(population: Sequence[T], size: int) -> list[T]:
    if size < 1:
        raise ValueError("Size must be >= 1")
    result = list(population)
    shuffle(result)
    return result[:size]


@dataclass
class Plastic:
    item_name: str
    hardness: Optional[int] = 10
    classification: Optional[int] = 3


@dataclass
class Steel:
    item_name: str
    type: Optional[str] = 'SS'
    thickness: Optional[int] = 5


plastics = (
    Plastic("Bottle", 1),
    Plastic("Toy Car", 2),
    Plastic("Watch", 2),
    Plastic("Laptop", 5),
    Plastic("Charger", 3)
)


steels = (
    Steel("Computer", "Alum"),
    Steel("Bridge", "Hard SS"),
    Steel("Watch", "Soft SS"),
    Steel("Toy Car", "Thin Steel"),
    Steel("Fan", "Semi Hard Alum")
)

mix = plastics[:2] + steels[:2]

print(sample(steels, 2))
print(sample(mix, 2))


