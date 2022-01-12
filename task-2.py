import math
y = "Не найден, x - не число"

# Сохранение введенных данных
input_value = str(input())

# Проверка введенного значения
if input_value.isdigit():
    x = int(input_value)

    # Условия
    if x < 17:
        y = 28*x**3 - 91

    elif 17 <= a <= 27:
        y = 11*x**2 +12*x - 13*x**3

    else:
        y = 1/64*x**8 - x**5 +131

print("y= "+str(y))