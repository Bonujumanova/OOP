class Human:
    default_name: str = ""
    default_age: int = 1

    def __init__(self, name=default_name, age=default_age):
        self.name: str = name
        self.age: int = age
        self.__money: int| float = 0
        self.__house: int| float| None = None

    def info(self):
        print(
            f"Имя покупателя: {self.name}\n"
            f"Возраст покупателя: {self.age}\n"
            f"{self.__house}\n"
            f"Общее количество денег: {self.__money} "
            )

    @classmethod
    # хотят статический метод, но тогда не будет доступа к полям класса,
    # поэтому тут используется метод класса
    def default_info(cls):
        print(cls.default_name, cls.default_age, sep="\n")


    def __make_deal(self, obj, price):
        self.__money -= price
        self.__house = obj


    def earn_money(self, earned_money):
        self.__money += earned_money
        print(
            f"Вы заработали {earned_money}.",
            f"Теперь у Вас {self.__money}!"  )


    def buy_house(self, obj, discount):
        price: int| float = obj.final_price(discount)
        if self.__money >= price: # тут должна быть стоимость дома со скидкой

            self.__make_deal(obj, price)
            print("Поздравляем с покупкой дома!!!")
        else:
            print(
                "\n\tНедостаточно денег!\n"
                "\tНе расстраивайтесь!\n"
                "\tМы готовы предложить Вам кредит под 365% годовых! Успейте получить!\n"
            )


class House:
    def __init__(self, area, price):
        self._area: int| float = area
        self._price: int| float = price


    def final_price(self, discount):
        self._price -=  discount / 100
        print(f"Конечная стоимость дома: {self._price}")
        return self._price


class SmallHouse(House):
    default_area: int| float = 40
    def __init__(self, price):
        super().__init__(SmallHouse.default_area, price)  # Dynamically calls the parent class's __init__
        self._price = price


kitty = Human("hello kitty", 51)
kitty.info()

sm_house = SmallHouse(1000000)

kitty.earn_money(5400000)
print()

kitty.buy_house(sm_house, 12)
print()

print(kitty.info())
