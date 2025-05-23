import time


# Класс объектов, которые одновременно являются
# и итерируемыми (есть метод __iter__),
# и итераторами (есть метод __next__).
# Генерирует последовательность строк из решеток убывающей длины.
class RangeIterableIterator:
    def __init__(self, size):
        self.x = size  # начинаем с заданного значения

    # Для работы цикла for объект должен возвращать себя как итератор.
    def __iter__(self):
        return self

    # Метод, который возвращает следующий элемент последовательности.
    def __next__(self):
        self.x -= 1
        # Если значение становится меньше или равно 0, последовательность завершена.
        if self.x <= 0:
            raise StopIteration
        # Возвращаем строку, состоящую из self.x символов "#".
        return '#' * self.x


# Главная программа
if __name__ == '__main__':
    # Создаем объект-итератор с начальными значением для строк (например, 32)
    main_iter = RangeIterableIterator(32)

    # Проходим по последовательности и выводим каждую строку
    for line in main_iter:
        print(line)
        # Задержка между выводами (0.25 секунды)
        time.sleep(0.25)
