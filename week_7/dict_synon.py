# Вам дан словарь, состоящий из пар слов. Каждое слово является синонимом к парному ему слову.
# Все слова в словаре различны. Для одного данного слова определите его синоним.

n = int(input())
p = dict(input().split() for j in range(n))
k = input()

if k in list(p.keys()):
    print(p[k])
else:
    for i in list(p.keys()):
        if p[i] == k:
            print(i)
