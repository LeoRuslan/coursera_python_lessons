# Дан текст.
# Выведите слово, которое в этом тексте встречается чаще всего.
# Если таких слов несколько, выведите то, которое меньше в лексикографическом порядке.

from collections import Counter

data = open("input_world.txt").read().split()
with open("output_world.txt", "w") as out:
    out.write(sorted(Counter(data).items(), key=lambda x: (-x[1], x[0]))[0][0])
