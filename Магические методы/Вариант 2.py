class Abiturient:
    total_abiturients = 0

    def __new__(cls, *args, **kwargs):
        # Пример использования __new__
        print(f"Creating a new Abiturient instance...")
        instance = super().__new__(cls)
        return instance

    def __init__(self, id, фамилия, имя, отчество, адрес, телефон, оценки):
        print(f"Initializing Abiturient instance with id {id}...")
        self.id = id
        self.фамилия = фамилия
        self.имя = имя
        self.отчество = отчество
        self.адрес = адрес
        self.телефон = телефон
        self.__оценки = оценки
        Abiturient.total_abiturients += 1

    def __setattr__(self, name, value):
        # Добавляем проверку для избежания пустых фамилий
        if name == 'фамилия' and not value:
            raise ValueError("Фамилия не может быть пустой.")
        super().__setattr__(name, value)


    def __str__(self):
        return f"Abiturient(ID: {self.id}, Фамилия: {self.фамилия}, Имя: {self.имя}, Отчество: {self.отчество})"

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

    # Магические методы арифметики
    def __add__(self, other):
        """Сложение сумм оценок двух абитуриентов"""
        if isinstance(other, Abiturient):
            return sum(self.оценки) + sum(other.оценки)
        else:
            raise TypeError("Можно складывать только с другим Abiturient.")

    def __mul__(self, factor):
      """Умножение каждой оценки на фактор (например, для нормализации)"""
      if isinstance(factor, (int, float)):
          new_grades = [min(10, grade * factor) for grade in self.оценки]  #ограничиваем макс. оценку 10
          return Abiturient(self.id, self.фамилия, self.имя, self.отчество, self.адрес, self.телефон, new_grades)
      else:
          raise TypeError("Множитель должен быть числом.")

    # Магические методы сравнения
    def __gt__(self, other):
        """Сравнение абитуриентов по сумме оценок (больше)"""
        if isinstance(other, Abiturient):
            return sum(self.оценки) > sum(other.оценки)
        else:
            raise TypeError("Можно сравнивать только с другим Abiturient.")

    def __eq__(self, other):
        """Сравнение абитуриентов по фамилии и имени (равно)"""
        if isinstance(other, Abiturient):
            return (self.фамилия == other.фамилия) and (self.имя == other.имя)
        else:
            raise TypeError("Можно сравнивать только с другим Abiturient.")

    def __del__(self):
        print(f"Deleting Abiturient instance: {self}")
        Abiturient.total_abiturients -= 1

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


# Пример использования __str__
print(f"\nИнформация об абитуриенте: {abiturients[0]}")

# Пример использования __add__
print(f"\nСумма оценок Иванова и Петрова: {abiturients[0] + abiturients[1]}")

# Пример использования __mul__
ivanov_normalized = abiturients[0] * 2  # Умножаем оценки Иванова на 2, ограничивая максимум 10
print(f"\nНормализованные оценки Иванова (умноженные на 2): {ivanov_normalized.оценки}")
ivanov_normalized.display_info() # выводим информацию по абитуриенту

# Пример использования __gt__
print(f"\nСумма баллов у Иванова больше чем у Петрова? {abiturients[0] > abiturients[1]}")

# Пример использования __eq__
print(f"\nИванов и Петров имеют одинаковую фамилию и имя? {abiturients[0] == abiturients[1]}")

# Пример использования __del__ (удаление объектов)
del abiturients[0]
print(f"Общее количество абитуриентов после удаления: {Abiturient.get_total_abiturients()}")

del abiturients # Удаляем список целиком