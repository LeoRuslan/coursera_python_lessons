# Во входном файле (вы можете читать данные из файла input.txt) записан текст.
# Словом считается последовательность непробельных подряд идущих символов.
# Слова разделены одним или большим числом пробелов или символами конца строки.
# Для каждого слова из этого текста подсчитайте, сколько раз оно встречалось в этом тексте ранее.

import sys

text = sys.stdin.read().strip('\n').split()
result_set = {}

list_answer = []
for w in text:
    result_set[w] = result_set.get(w, 0) + 1
    list_answer.append(result_set[w] - 1)

print(*list_answer)

# one two one tho three
# 0 0 1 0 0
#
# aba aba; aba @?"
# 0 0 1 0
