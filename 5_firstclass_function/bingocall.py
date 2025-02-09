import random


class BingoCall:

    def __init__(self, items):
        self._items = list(items)
        random.shuffle(self._items)

    def pick(self):
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError('pick from empty BingoCall')

    def __call__(self):
        return self.pick()


if __name__ == '__main__':
    bingo = BingoCall(range(5))
    print(bingo.pick())
    print(bingo())
    print(callable(bingo))