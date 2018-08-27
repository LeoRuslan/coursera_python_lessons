# На вход подаётся последовательность натуральных чисел длины n≤1000.
# Посчитайте произведение пятых степеней чисел в последовательности.
#
# Формат ввода
# Вводится последовательность чисел
#
# Формат вывода
# Выведите ответ на задачу
#
# Примечания
# Для решения задачи используйте функцию reduce из модуля functools

from functools import reduce

print(
    (reduce
     (lambda x, y: x * y,
      map(
          int,
          input().split())
      )
     ) ** 5
)
