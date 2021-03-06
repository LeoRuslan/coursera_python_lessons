# Дан текст.
# Выведите все слова, встречающиеся в тексте, по одному на каждую строку.
# Слова должны быть отсортированы по убыванию их количества появления в тексте,
# а при одинаковой частоте появления — в лексикографическом порядке.

import sys

d = {}
text = sys.stdin.read().strip('\n').split()

for word in text:
    d[word] = d.get(word, 0) + 1

for i in sorted(d.items(), key=lambda x: (-x[1], x[0])):
    print(i[0])

