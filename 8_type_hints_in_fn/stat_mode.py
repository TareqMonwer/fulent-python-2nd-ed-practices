from collections import Counter
from decimal import Decimal
from fractions import Fraction
from typing import Any, Hashable, Iterable, TypeVar

NumberT = TypeVar("NumberT", float, Decimal, Fraction, list[Any])


# def mode(data: Iterable[NumberT]) -> NumberT:
#     pairs = Counter(data).most_common(1)
#     if len(pairs) == 0:
#         raise ValueError("no mode for empty data")

#     return pairs[0][0]
# y = mode([[1, 2, 3], [1, 2, 3], [1, 2]])  # throws error
# y = mode([1, 1, 2]) # works well


# def mode(data: Iterable[Hashable]) -> Hashable:
#     pairs = Counter(data).most_common(1)
#     if len(pairs) == 0:
#         raise ValueError("no mode for empty data")

#     return pairs[0][0]


# y = mode([1, 1, 2])
# print(y)

# a: float = y * 4  # error

HashableT = TypeVar("HashableT", bound=Hashable)


def mode(data: Iterable[HashableT]) -> HashableT:
    pairs = Counter(data).most_common(1)
    if len(pairs) == 0:
        raise ValueError("no mode for empty data")

    return pairs[0][0]


y = mode([1, 1, 2])
a: float = y * 4  # correct
