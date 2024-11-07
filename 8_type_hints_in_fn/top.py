from typing import Any, Iterable, Protocol, TypeVar


class SupportsLT(Protocol):
    def __lt__(self, other: Any) -> bool: ...


LT = TypeVar('LT', bound=SupportsLT)


def top(series: Iterable[LT], length: int) -> Iterable[LT]:
    ordered = sorted(series, reverse=True)
    return ordered[:length]
