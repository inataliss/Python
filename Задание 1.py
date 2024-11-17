# Вариант 1
# Удалить в списке все числа, которые повторяются более двух раз.
# Найти подмножество данного множества чисел такое, что сумма его элементов равна заданному числу.

from collections import Counter

# Исходный список чисел
numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 6]

# Подсчитываем количество вхождений каждого числа
counts = Counter(numbers)

# Создаем новый список, исключая числа, которые повторяются более двух раз
filtered_numbers = [num for num in numbers if counts[num] <= 2]

print(filtered_numbers)

#Найти подмножество данного множества чисел такое, что сумма его элементов равна заданному числу.
import itertools

def find_subset_with_sum(numbers, target_sum):
    # Перебираем все возможные подмножества
    for r in range(len(numbers) + 1):
        for subset in itertools.combinations(numbers, r):
            if sum(subset) == target_sum:
                return list(subset)
    return None

# Пример использования
numbers = [3, 34, 4, 12, 5, 2]
target_sum = 9
subset = find_subset_with_sum(numbers, target_sum)
print(subset)


#Вариант 2
#Введите одномерный целочисленный список. Найдите наибольший нечетный элемент.
def find_largest_odd_element(numbers):
    # Ищем все нечетные элементы в списке
    odd_numbers = [num for num in numbers if num % 2 != 0]

    # Если нечетных элементов нет, возвращаем None
    if not odd_numbers:
        return None

    # Возвращаем наибольший нечетный элемент
    return max(odd_numbers)


# Пример использования
numbers = [10, 3, 5, 6, 8, 11, 13, 2, 14, 7]
largest_odd = find_largest_odd_element(numbers)
print(largest_odd)


#Найдите минимальный по модулю элемент списка.
def find_min_abs_element(numbers):
    # Проверяем, что список не пустой
    if not numbers:
        return None

    # Находим элемент с минимальным абсолютным значением
    min_abs_element = min(numbers, key=abs)

    return min_abs_element


# Пример использования
numbers = [10, -3, 5, -6, 8, 11, -13, 2, -14, 7]
min_abs_element = find_min_abs_element(numbers)
print(min_abs_element)



#Задание 2
#В матрице найти номер строки, сумма чисел в которой максимальна.
def find_row_with_max_sum(matrix):
    max_sum = float('-inf')
    row_index = -1

    for i, row in enumerate(matrix):
        current_sum = sum(row)
        if current_sum > max_sum:
            max_sum = current_sum
            row_index = i

    return row_index

# Пример использования
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0, -1, -2]
]
max_sum_row_index = find_row_with_max_sum(matrix)
print(max_sum_row_index)








