class Nicola:
    def __init__(self, name: str, age: int):
        if name.lower() == "николай":
            self.name = name
        else:
            self.name = f"Я не {name}, а Николай."

        self.age = age

    def show_result(self):
        print(f"{self.name} Мне {self.age} лет")

res1 = Nicola("Николай", 999)
res1.show_result()
print(res1.name)