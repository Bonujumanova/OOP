class Soda:

    def __init__(self, topping=""):
        self.topping: str = topping

    def show_my_drink(self) -> None:
        if self.topping:
            print(f"Газировка и {self.topping}")
        else:
            print(f"Газировка")


if __name__ == "__main__":
    drink = Soda()
    drink.show_my_drink()
