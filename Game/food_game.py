import io

# Главная программа
if __name__ == '__main__':
    main_iter = io.open('food.csv', encoding='utf-8')

    # Вывод инструкций для игры
    print("Игра \"Съедобное-несъедобное\".")
    print("Вам будут по очереди выводиться названия предметов.")
    print("Вводите 0 если предмет несъедобный и 1 - если съедобный.")
    print("Для начала нажмите Enter.")
    input()

    score = 0  # Счётчик правильных ответов

    # Цикл по каждой строке файла
    for line in main_iter:
        # Разбиваем строку по символу ';' и удаляем лишние пробелы/символы новой строки
        cells = line.strip().split(';')

        # Первый элемент списка cells - название предмета или строка стихотворения
        print(cells[0])

        # Принимаем ответ пользователя
        user_ans = input("Ваш ответ: ")

        # Проверяем ответ: сравниваем первый символ введённого ответа с первым символом второго столбца
        if user_ans and user_ans[0] == cells[1][0]:
            print("Правильно!")
            score += 1
        else:
            print("Неправильно!")

    # Вывод итогового счёта
    print("Вы набрали " + str(score) + " очков.")
    print("КОНЕЦ.")
