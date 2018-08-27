# __add__, принимающий вторую матрицу того же размера и возвращающий сумму матриц.
# __mul__, принимающий число типа int или float и возвращающий матрицу, умноженную на скаляр.
# __rmul__, делающий то же самое, что и __mul__. Этот метод будет вызван в том случае, аргумент находится справа.
# Для реализации этого метода в коде класса достаточно написать __rmul__ = __mul__.

# Добавьте в программу из предыдущей задачи класс MatrixError,
# содержащий внутри self поля matrix1 и matrix2 — ссылки на матрицы.

# В класс Matrix внесите следующие изменения:
# Добавьте в метод __add__ проверку на ошибки в размере входных данных,
# чтобы при попытке сложить матрицы разных размеров было выброшено исключение MatrixError таким образом,
# чтобы matrix1 поле MatrixError стало первым аргументом __add__ (просто self),
# а matrix2 — вторым (второй операнд для сложения).

# Реализуйте метод transpose, транспонирующий матрицу и возвращающую результат
# (данный метод модифицирует экземпляр класса Matrix)

# Реализуйте статический метод transposed, принимающий Matrix и возвращающий транспонированную матрицу.


from sys import stdin
from copy import deepcopy


class MatrixError(BaseException):
    def __init__(self, matrix, other):
        self.matrix1 = matrix
        self.matrix2 = other


class Matrix:
    def __init__(self, lists):
        self.lists = deepcopy(lists)

    def __str__(self):
        str_rep = ""
        amount = 0
        for lists in self.lists:
            if amount != 0:
                str_rep += "\n"
            new_str = "\t".join(str(elem) for elem in lists)
            str_rep += new_str
            amount += 1
        return str_rep

    def size(self):
        return len(self.lists), len(self.lists[0])

    def __add__(self, other):
        if len(self.lists) == len(other.lists):
            lenght = len(self.lists[0])
            for row in self.lists:
                if len(row) != lenght:
                    raise MatrixError(self, other)
            for row2 in other.lists:
                if len(row2) != lenght:
                    raise MatrixError(self, other)
            result = []
            numbers = []
            for i in range(len(self.lists)):
                for j in range(len(self.lists[0])):
                    summa = other.lists[i][j] + self.lists[i][j]
                    numbers.append(summa)
                    if len(numbers) == len(self.lists[0]):
                        result.append(numbers)
                        numbers = []
            return Matrix(result)
        else:
            raise MatrixError(self, other)

    def __mul__(self, alpha):
        if isinstance(alpha, int) or isinstance(alpha, float):
            result = []
            numbers = []
            for i in range(len(self.lists)):
                for j in range(len(self.lists[0])):
                    summa = self.lists[i][j] * alpha
                    numbers.append(summa)
                    if len(numbers) == len(self.lists[0]):
                        result.append(numbers)
                        numbers = []
            return Matrix(result)

    def transpose(self):
        t_matrix = list(zip(*self.lists))
        self.lists = t_matrix
        return Matrix(t_matrix)

    def transposed(self):
        t_matrix = list(zip(*self.lists))
        return Matrix(t_matrix)

    __rmul__ = __mul__


exec(stdin.read())
