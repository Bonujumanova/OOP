def one():
    pass


"abc"  # объект строки, экземпляр строки | представитель строки
15  # объект, экземпляр целовго числа
[]  # объект, экземпляр списка
list()  # объект, экземпляр списка

s = "abc"

s = s.capitalize()


# Вася  # объект человека
# Петя  # объект человека


class Human:
    legs = 2  # поле, свойство, атрибут - класса

    # инициализатор, конструктуор, магический метод __init__
    def __init__(self, name, age):
        # поле, свойство, атрибут -> объекта
        # self.n = name
        self.name = name
        # self.a = age
        self.age = age
        self.flag = True

    # метод
    def think(self):
        print(f"Я {self.name} и я думаю")

    def walk(self):
        print("Гуляю")

    def run(self):
        print("Бегу")


class User:

    def __init__(self, nickname, password):
        self.nick = nickname
        self.psswd = password

    def register(self):
        pass

    def login(self):
        pass

    def logout(self):
        pass

    def two_fa(self):
        pass


class Authentication:
    pass


def think(name):
    print("Думаю")


def walk(name):
    print("Гуляю")


def run(name):
    print("Бегу")


if __name__ == "__main__":
    vasya = Human("Вася", 18)

    vasya.think()
    vasya.run()
    print(vasya.legs)  # атрибут класса, общее
    print(vasya.name)  # атрибут объекта, частное

    petya = Human("Петя", 26)
    print(petya.name)  # атрибут объекта, частное

    masha = Human("Маша", 22)
    dasha = Human("Даша", 19)

    petya.think()

    print(type(vasya))
