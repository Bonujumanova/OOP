class TriangleChecker:

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def is_correct_value(self):
        for side in [self.a, self.b, self.c]:
            if not isinstance(side, (int, float)):
                return False
        return True

    def is_valid_triangle(self):
        return (
                self.a + self.b > self.c
                or self.b + self.c > self.a
                or self.a + self.c > self.b
        )

    def check_triangle(self):
        if not self.is_correct_value():
            return "Нужно вводить только числа!"

        if any([i for i in [self.a, self.b, self.c] if i < 0]):
            return "С отрицательными числами ничего не выйдет!"

        if self.is_valid_triangle():
            return "Ура, можно построить треугольник!"

        return "Жаль, но из этого треугольник не сделать."


if __name__ == "__main__":
    triangle_1 = TriangleChecker(3, "g", -6)
    print(triangle_1.check_triangle())
