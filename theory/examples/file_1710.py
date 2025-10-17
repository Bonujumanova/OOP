class BankAccount:
    __slots__ = ["__name", "surname", "balance", "age"]

    def __init__(self, name, surname, balance, age):
        # public
        # _ | protected
        # __ | private

        self.__name = name
        self.surname = surname
        self.balance = balance
        self.age = age

    @property
    def name(self):  # геттер
        return self.__name

    @name.setter
    def name(self, new_value):
        self.__name = new_value


class User:
    @property
    def login(self):  # геттер
        return self.__login

    @login.setter
    def login(self, new_value):
        self.__login = new_value

    @property
    def password(self):  # геттер
        return self.__password

    @password.setter
    def password(self, new_value):
        self.__password = new_value

    __last_username = None

    def __init__(self, login, password):
        self.__login = login
        self.__password = password
        self.__is_active = False
        self.__is_admin = False
        self.set_last_username(login)

    @classmethod
    def set_last_username(cls, username):
        cls.__last_username = username

    @classmethod
    def get_last_username(cls):
        return cls.__last_username

    @staticmethod
    def is_valid_login(value: str):
        return not value[0].isdigit() and value.isalnum()



if __name__ == "__main__":
    # Модификаторы доступа и геттеры и сеттеры

    # ba_1 = BankAccount("Иван", "Иванов", 100, 19)
    #
    # print(str(ba_1.name))
    # ba_1.name = "Петр"
    # print(str(ba_1.name))

    # ----------------

    # Виды методов класса

    vasya = User("vasya", "123")

    print(User.is_valid_login("a1petya"))

    print(User.get_last_username())
