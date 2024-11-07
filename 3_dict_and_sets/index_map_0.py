"""Build an index mapping word -> list of occurences"""

import sys
import re


WORD_RE = re.compile('\w+')

index = dict()
with open(sys.argv[1], encoding='utf-8') as fp:
    for line_num, line in enumerate(fp, 1):
        for match in WORD_RE.finditer(line):
            word = match.group()
            column_num = match.start() + 1
            location = (line_num, column_num)

            # occurrences = index.get(word, [])
            # occurrences.append(location)
            # index[word] = occurrences
            # THESE THREE LINES ARE REPLACED BY NEXT LINE
            index.setdefault(word, []).append(location)

for word in sorted(index, key=str.upper):
    print(word, index[word])
