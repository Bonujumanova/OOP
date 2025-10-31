# class Pizza:
#     __default_size = 27
#
#     def __init__(self, name: str, size: int, ingredients: list | tuple):
#         self.name = name
#         self.size = size
#         self.ingredients = ingredients
#
#     @classmethod
#     def create_default_pizza(cls, name: str = ""):
#         new_obj = cls(name or "Лучшая", 30, ["o", "p", "r"])
#
#         return new_obj
#
#     def create_margarite(self):
#         new_obj = Pizza("Маргарита", 23, ['a', 'b', 'c'])
#
#         return new_obj
#
#     @staticmethod
#     def create_pepperoni():
#         new_obj = Pizza("Пепперони", 30, ['a', 'b', 'c'])
#
#         return new_obj
#
#     # Строковое представление объекта
#     def __str__(self) -> str:
#         return f"{self.name} {self.size} см | {', '.join(self.ingredients)}"
#
#     def __repr__(self) -> str:
#         return f"Название: {self.name}Размер:{self.size}Ингредиенты: {self.ingredients}"
#
#
# if __name__ == '__main__':
#     caser = Pizza("Цезарь", 27, ['a', 'b', 'c'])
#
#     default = Pizza.create_default_pizza()
#     margarite = caser.create_margarite()
#     pepperoni = Pizza.create_pepperoni()
#
#     print(caser)
#     print(default)
#     print(margarite)
#     print(pepperoni)

# print(caser.name)
# print(default.name)
# print(margarite.name)

print("--------------------------------------")

# class Database:
#     __instance = None
#
#     # Singleton | Одиночка
#     def __new__(cls, *args, **kwargs):
#         if cls.__instance is None:
#             new_obj = super().__new__(cls)
#             # new_obj.check = True
#             cls.__instance = new_obj
#
#         return cls.__instance
#
#     def __init__(self, name, password, port, quite_mode=False):
#         self.name = name
#         self.password = password
#         self.port = port
#         self.qm = quite_mode
#
#
# if __name__ == '__main__':
#     db = Database("users.db", "12345", 5432, quite_mode=True)
#     db2 = Database("goods.db", "12345", 5432, quite_mode=True)
#     db3 = Database("orders.db", "12345", 5432, quite_mode=True)
#     print(db.name)
#     print(db2.name)
#     print(db3.name)
#     # print(db.__dict__)
#
#     print(id(db))
#     print(id(db2))
#     print(id(db3))
#
#
#
print("--------------------------------------")

# class ShowMessage:
#     __instance = None
#
#     def __new__(cls, *args, **kwargs):
#         if cls.__instance is None:
#             cls.__instance = super().__new__(cls)
#
#         return cls.__instance
#
#     def __call__(self, *args, **kwargs):
#         for arg in args:
#             print(arg.swapcase())
#
#
# if __name__ == '__main__':
#     show = ShowMessage()
#     show2 = ShowMessage()
#     show3 = ShowMessage()
#     show4 = ShowMessage()
#     show5 = ShowMessage()
#
#     show("Hello", "Bonjour", "Privet", "Hola!")
#     show2("Hello", "Bonjour", "Privet", "Hola!")
#
#     print(id(show))
#     print(id(show2))
#
print("--------------------------------------")

# --------------------------------------

# # Базовый класс, Родительский класс, Супер класс
# class Animal:
#     def voice(self):
#         raise NotImplemented
#
#     def show_info(self):
#         print("Я очень милый")
#
#
# # Дочерний класс, Под класс
# class Cat(Animal):
#     def voice(self):
#         print("Мяу")
#
#
# class Dog(Animal):
#     def voice(self):
#         print("Гав")
#
#
# class Bear(Animal):
#     def voice(self):
#         print("Грр")
#
#     def show_info(self):
#         print("Я очень злой")
#
#
# if __name__ == '__main__':
#     c1 = Cat()
#     d1 = Dog()
#     b1 = Bear()
#
#     c1.voice()
#     d1.voice()
#     b1.voice()
#
#     c1.show_info()
#     d1.show_info()
#     b1.show_info()


# --------------------------------------
