class Nicola:
    __slots__ = ["name", "age"]

    def __init__(self, name: str, age: int):
        self.name = self.__get_name(name)
        self.age = age

    def __get_name(self, value):
        if value.lower() == "николай":
            return value
        return f"Я не {value}, а Николай."

    def show_result(self):
        print(f"{self.name} Мне {self.age} лет")


if __name__ == "__main__":
    res1 = Nicola("Николай", 999)

    # res1.surname = "Иванов"
    # print(res1.surname)  # AttributeError: 'Nicola' object has no attribute 'surname'

    res1.show_result()
    print(res1.name)
