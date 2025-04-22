import time
import itertools

from A_increase import RangeIterable
from B_decrease import RangeIterableIterator
from C_sinus import SinusIterableWithGenerator

if __name__ == '__main__':
    # Создаем цепочку итерируемых объектов из разных заданий:
    # - RangeIterableIterator(32): выводит строки убывающей длины (начиная с 32 # и уменьшаясь)
    # - RangeIterable(16): выводит строки возрастающей длины (от 1 до 16 #)
    # - SinusIterableWithGenerator(64, 32): выводит строки с длиной по синусоиде (бесконечная последовательность)
    main_iter = itertools.chain(
        RangeIterableIterator(32),
        RangeIterable(16),
        SinusIterableWithGenerator(64, 32)
    )

    # Проходим по объединенной цепочке и выводим каждую строку с задержкой 0.25 секунды.

    for line in main_iter:
        print(line)
        time.sleep(0.25)
