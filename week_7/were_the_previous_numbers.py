# Во входной строке записана последовательность чисел через пробел.
# Для каждого числа выведите слово YES (в отдельной строке),
# если это число ранее встречалось в последовательности или NO, если не встречалось.

input_list = list(map(int, input().split()))

worl_set = set()
for i in input_list:
    if i in worl_set:
        print('YES')
    else:
        print('NO')
        worl_set.add(i)
