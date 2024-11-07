class Averager:
    def __init__(self) -> None:
        self.series: list[float] = []

    def __call__(self, new_value: float) -> float:
        self.series.append(new_value)
        total: float = sum(self.series)
        return total / len(self.series)


if __name__ == "__main__":
    avg = Averager()
    print(avg(10))
    print(avg(11))
    print(avg(12))
