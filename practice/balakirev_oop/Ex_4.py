class Money:

    def __init__(self, money):
        self.__money = 0
        if self.__check_money(money):
            self.__money = money


    def set_money(self, money_):
        if self.__check_money(money_):
            self.__money = money_


    def get_money(self):
        return self.__money


    def add_money(self, money):
        # тут в money - экземпляр класса?, который мы получили вот так:
        # obj_2 = Money(10)
        # obj_2 = Money(20)
        # obj_2.add_money(obj_1)
        self.__money += money.get_money()


    @classmethod
    def __check_money(cls, money):
        return money > 0 and isinstance(money, int)



obj_1 = Money(10)
obj_2 = Money(20)
obj_1.set_money(100)

# obj_1 - возвращает 10 после всех проверок. И этот результат передается в метод add_money(obj_1)
obj_2.add_money(obj_1)

print(obj_1.get_money())
print(obj_2.get_money())
