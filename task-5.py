import random

# Пустой список
list_values = []
# Цикл на заполнение массива чисел
for i in range(24):
    list_values.append(round(random.uniform(-10,10), 3))

# Печать первоначального массива
print("Первоначальный массив:")
print(list_values)


# print(min(list_values))
# Предположим, что минимальный элемент равен list_values[0]
min = first_value = list_values[0]
index = 0

# Цикл выбора наименьшего элемента
for i in range(1, len(list_values)):
    if list_values[i] < min:
        min = list_values[i]
        index = i

# Меняем местами
print("Минимальный элемент: " + str(min))
list_values[0] = min
list_values[index] = first_value

# Печать конечного массива
print("Конечный массив:")
print(list_values)


