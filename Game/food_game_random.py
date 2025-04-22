import io
import numpy as np

if __name__ == '__main__':

    load_iter = io.open('food2.csv', encoding='utf-8')

    # Считываем данные из файла в два списка: один для названий, второй для признаков съедобности
    lines = []  # список с названиями или строками
    isFood = []  # список с признаком съедобности (0 или 1)
    for line in load_iter:
        cells = line.strip().split(';')
        if len(cells) >= 2:
            lines.append(cells[0])
            isFood.append(cells[1])

    # Создаем случайную перестановку индексов строк
    main_iter = np.random.permutation(len(lines))

    # Вывод инструкции для пользователя
    print("Игра \"Съедобное-несъедобное\".")
    print("Вам будут по очереди выводиться названия предметов.")
    print("Вводите 0 если предмет несъедобный и 1 - если съедобный.")
    print("Для начала нажмите Enter.")
    input()

    score = 0
    # Проходим по случайной перестановке номеров строк
    for num in main_iter:
        print(lines[num])
        user_input = input("Ваш ответ: ")
        # Сравниваем первый символ пользовательского ввода с первым символом из соответствующего элемента isFood
        if user_input and user_input[0] == isFood[num][0]:
            print("Правильно!")
            score += 1
        else:
            print("Неправильно!")

    print("Вы набрали " + str(score) + " очков.")
    print("КОНЕЦ.")
