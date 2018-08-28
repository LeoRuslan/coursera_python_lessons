# Даны два списка чисел, которые могут содержать до 10000 чисел каждый.
# Выведите все числа, которые входят как в первый, так и во второй список, в порядке возрастания.

first_list = list(map(int, input().split()))
second_list = list(map(int, input().split()))

print(*sorted(set(first_list) & set(second_list)))
