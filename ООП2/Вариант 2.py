#Kласс Abiturient: id, Фамилия, Имя, Отчество, Адрес, Телефон,
# Оценки. Функции-члены реализуют запись и считывание полей (проверка корректности).
#Создать список объектов. Вывести:
#а)список абитуриентов, имеющих неудовлетворительные оценки;
#б) список абитуриентов, у которых сумма баллов выше заданной;


class Abiturient:
    total_abiturients = 0

    def __init__(self, id, фамилия, имя, отчество, адрес, телефон, оценки):
        self.id = id
        self.фамилия = фамилия
        self.имя = имя
        self.отчество = отчество
        self.адрес = адрес
        self.телефон = телефон
        self.__оценки = оценки
        Abiturient.total_abiturients += 1

    @property
    def оценки(self):
        return self.__оценки

    @оценки.setter
    def оценки(self, value):
        if all(isinstance(x, (int, float)) and 0 <= x <= 10 for x in value):
            self.__оценки = value
        else:
            raise ValueError("Оценки должны быть числами от 0 до 10.")

    def display_info(self):
        print(f"ID: {self.id}, {self.фамилия} {self.имя} {self.отчество}, Адрес: {self.адрес}, Телефон: {self.телефон}, Оценки: {self.__оценки}")

    @classmethod
    def get_total_abiturients(cls):
        return cls.total_abiturients

    @staticmethod
    def has_failing_grades(оценки):
        return any(оценка < 4 for оценка in оценки)

# Пример
abiturients = [
    Abiturient(1, "Иванов", "Иван", "Иванович", "ул. Ленина, 10", "123-456", [3, 4, 5, 6]),
    Abiturient(2, "Петров", "Петр", "Петрович", "ул. Победы, 5", "789-012", [8, 9, 7, 9]),
    Abiturient(3, "Сидоров", "Сидор", "Сидорович", "ул. Мира, 15", "345-678", [2, 3, 4, 5])
]

print("Абитуриенты с неудовлетворительными оценками:")
for abiturient in abiturients:
    if Abiturient.has_failing_grades(abiturient.оценки):
        abiturient.display_info()

threshold = 25
print(f"\nАбитуриенты с суммой баллов выше {threshold}:")
for abiturient in abiturients:
    if sum(abiturient.оценки) > threshold:
        abiturient.display_info()

print(f"\nОбщее количество абитуриентов: {Abiturient.get_total_abiturients()}")
