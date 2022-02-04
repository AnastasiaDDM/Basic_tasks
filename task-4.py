# Сохранение введенных данных
input_str = str(input())
print("Первоначальная строка- "+input_str)

# Проверка на нечетность
if len(input_str) % 2 != 0:
    # Деление с получением целого значения
    middle_char = len(input_str) // 2
    # Удаление среднего символа
    new_str = input_str[:middle_char] + input_str[middle_char + 1:]
    print("Конечный результат- "+new_str)
