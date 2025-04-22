import time


# Класс объектов-итераторов для последовательности строк из решеток возрастающей длины
class RangeIterator:
    def __init__(self, size):
        self.x = 0  # начальное значение (число # в строке)
        self.size = size  # общее количество строк

    def __next__(self):
        self.x += 1
        if self.x > self.size:
            raise StopIteration
        return '#' * self.x


# Класс итерируемых объектов, возвращающий объект-итератор RangeIterator
class RangeIterable:
    def __init__(self, size):
        self.size = size

    def __iter__(self):
        return RangeIterator(self.size)


# Главная программа - позволяет запустить файл как модуль
if __name__ == '__main__':
    # Создание итерируемого объекта из 32 строк
    main_iter = RangeIterable(32)

    # Проход по объекту и вывод каждой строки с короткой задержкой
    for line in main_iter:
        print(line)
        time.sleep(0.25)
