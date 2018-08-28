# В выборах Президента побеждает кандидат,
# набравший свыше половины числа голосов избирателей.
# Если такого кандидата нет, то во второй тур выборов выходят два кандидата,
# набравших наибольшее число голосов.

# Если есть кандидат, набравший более 50% голосов, программа должна вывести его имя.
# Если такого кандидата нет, программа должна вывести имя кандидата, занявшего первое место,
# затем имя кандидата, занявшего второе место.
# Выводите данные в файл output.txt с указанием кодировки utf8.

from collections import Counter

with open("input_elections.txt", encoding="utf8") as f:
    candidates = Counter(map(str.strip, f))

voices = sum(candidates.values())

with open("output_elections.txt", "w", encoding="utf8") as f:
    percent = candidates.most_common(1)[0][1] / voices * 100
    if percent > 50:
        print(candidates.most_common(1)[0][0], file=f)
    else:
        for name, _ in candidates.most_common(2):
            print(name, file=f)
