from collections.abc import Callable


def make_averager() -> Callable[..., float]:
    series: list[float] = []

    def averager(new_value: float) -> float:
        series.append(new_value)
        total: float = sum(series)
        return total / len(series)

    return averager


if __name__ == "__main__":
    avg = make_averager()
    print(avg(10))
    print(avg(11))
    print(avg(12))
