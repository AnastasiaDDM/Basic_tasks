import math
D = "Не найден, x - не число"

# Сохранение введенных данных
input_value = str(input())

# Проверка введенного значения
if input_value.isdigit():
    x = int(input_value)

    # Уравнение для решения
    D = -math.exp(-math.cos(math.sqrt(x+5/3)))-1.7*math.atan(x/5-3/4)*math.sin(1.7*x)
    # Вывод ответа
print("D= "+str(D))

