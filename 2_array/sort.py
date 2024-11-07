import bisect


HAYSTACK = [1, 4, 6, 10, 12, 16, 22, 28, 30]
NEEDLES = [0, 1, 3, 5, 11, 25, 31]

for needle in reversed(NEEDLES):
    position = bisect.bisect(HAYSTACK, needle)
    HAYSTACK.insert(position, needle)

print(HAYSTACK)
