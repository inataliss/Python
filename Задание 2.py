#Задание 1
#В соответствии со своим вариантом написать консольную программу по условиям,
# приведенным в таблице ниже.
# Вариант 12:Есть натуральное двузначное число n. Верно ли, что среди его цифр есть 1 или 9?

def contains_1_or_9(n):
    # Проверяем, что число двузначное
    if not (10 <= n <= 99):
        return "Число должно быть двузначным"

    # Преобразуем число в строку для проверки его цифр
    n_str = str(n)

    # Проверяем наличие цифры 1 или 9
    if '1' in n_str or '9' in n_str:
        return "Среди цифр есть числа 1 или 9"
    else:
        return "Среди цифр нет числа  1 или 9"


# Пример использования
n = int(input("Введите двузначное число: "))
result = contains_1_or_9(n)
print(result)


#Задание 2
#Фирма ежегодно на протяжении n лет закупала оборудование стоимостью соответственно s1, s2, ...,
# sn pублей в год (эти числа вводятся и обрабатываются последовательно).
# Ежегодно в результате износа и морального старения (амортизации) все имеющееся оборудование
# уценивается на р%. Какова общая стоимость накопленного оборудования за n лет?
def calculate_total_equipment_value(years, costs, depreciation_rate):
    total_value = 0
    current_value = 0

    for year in range(years):
        current_value += costs[year]  # Добавляем стоимость нового оборудования
        current_value *= (1 - depreciation_rate / 100)  # Применяем амортизацию
        total_value += current_value

    return total_value

# Ввод данных
years = int(input("Введите количество лет: "))
costs = []
for i in range(years):
    cost = float(input(f"Введите стоимость оборудования за {i + 1} год: "))
    costs.append(cost)
depreciation_rate = float(input("Введите процент амортизации: "))

# Расчет и вывод результата
total_value = calculate_total_equipment_value(years, costs, depreciation_rate)
print(f"Общая стоимость накопленного оборудования: {total_value:.2f} рублей")


#Задание 3
#Сформировать одномерный список целых чисел A, используя генератор случайных чисел (диапазон от 0 до 99).
# Размер списка n ввести с клавиатуры. В соответствии со своим вариантом написать программу по условию,
# представленному в таблице ниже.
# Вариант 12: Найти номер минимального элемента списка.

import random

def generate_random_list(n):
    return [random.randint(0, 99) for _ in range(n)]

def find_index_of_min_element(lst):
    min_index = 0
    for i in range(1, len(lst)):
        if lst[i] < lst[min_index]:
            min_index = i
    return min_index

# Ввод размера списка
n = int(input("Введите размер списка: "))

# Генерация случайного списка
random_list = generate_random_list(n)
print("Сгенерированный список:", random_list)

# Нахождение номера минимального элемента
min_index = find_index_of_min_element(random_list)
print("Номер минимального элемента:", min_index)






