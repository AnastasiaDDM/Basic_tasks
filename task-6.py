import random
import numpy as np

# Размерности матрицы
n = 3
m = 4
# Пустой список
array = []


# Ф-ия вывода массива
def print_array(self, caption=""):
    print(caption)
    for row in self:
        print(row)


# Цикл на заполнение массива чисел
# Заполнение строк матрицы
for i in range(n):
    # Пустой список
    list_row = []
    # Заполнение столбцов матрицы
    for j in range(m):
        list_row.append(round(random.uniform(-10, 10), 1))
    array.append(list_row)

# Печать матрицы
print_array(array, caption="Исходная матрица:")

# Получаем сумму элементов диагонали
sum_diagonal = 0
for x in range(0, len(array)):
    sum_diagonal = sum_diagonal + round(array[x][x], 1)
print("Сумма элементов по диагонали = " + str(sum_diagonal))

# Меняем значение крайнего элемента матрицы на сумму
array[n-1][m-1] = sum_diagonal

# Печать матрицы
print_array(array, caption="Полученная матрица:")
