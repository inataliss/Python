#Реализуйте рекурсивную функцию нарезания прямоугольника с заданными пользователем сторонами
#a и b на квадраты с наибольшей возможной на каждом этапе стороной. Выведите длины ребер получаемых квадратов
#и кол-во полученных квадратов.


def cut_squares(a, b):
    squares = []

    def cut_rectangle(a, b):
        if a == 0 or b == 0:
            return
        if a > b:
            squares.append(b)
            cut_rectangle(a - b, b)
        else:
            squares.append(a)
            cut_rectangle(a, b - a)

    cut_rectangle(a, b)

    return squares, len(squares)


# Пример:
a = 6
b = 4
squares, count = cut_squares(a, b)

print(f"Длины сторон квадратов: {squares}")
print(f"Количество квадратов: {count}")

