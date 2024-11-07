class ArithmaticProgression:
    def __init__(self, begin, step, end):
        self.begin = begin
        self.step = step
        self.end = end

    def __iter__(self):
        result_type = type(self.begin + self.step)
        result = result_type(self.begin)
        forever = self.end is None

        # index = 0
        # while forever or result < self.end:
        #     yield result
        #     index += 1
        #     result = self.begin + self.step * index

        while forever or result < self.end:
            yield result
            result += self.step
