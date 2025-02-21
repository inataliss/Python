class Table:
    __mass = 0

    def __init__(self, mass0):
        self.__mass = mass0

    # чтение инкапсулированной массы
    def get_mass(self):
        return self.__mass

# журнальный стол
class JournalTable(Table):
    storage = 0

# обеденный стол
class DinnerTable(Table):
    __places = 0

    def __init__(self, mass0):
        Table.__init__(self, mass0)
        self.__places = mass0 // 5

    # чтение инкапсулированного числа мест
    def get_places(self):
        return self.__places

class Truck:
    def __init__(self, max_mass):
        self.__max_mass = max_mass
        self.__tables = []
        self.__current_mass = 0

    def load_table(self, table):
        if self.__current_mass + table.get_mass() <= self.__max_mass:
            self.__tables.append(table)
            self.__current_mass += table.get_mass()
            return True
        else:
            print(f"Масса превышает лимит! Невозможно загрузить стол весом {table.get_mass()} кг.")
            return False

    def current_load(self):
        return self.__current_mass

    def tables_loaded(self):
        return len(self.__tables)

# Пример:
truck = Truck(50)

table1 = JournalTable(20)
table2 = DinnerTable(25)
table3 = JournalTable(10)

truck.load_table(table1)  # True
truck.load_table(table2)  # True
truck.load_table(table3)  # False, так как масса превышает лимит

print(f"Текущая загруженная масса: {truck.current_load()} кг")
print(f"Количество загруженных столов: {truck.tables_loaded()}")
