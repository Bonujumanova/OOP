class TriangleChecker:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def check_triangle(self):
        if list(i for i in [self.a, self.b, self.c] if str(i).isalpha()):
            return "Нужно вводить только числа!"
        else:
            if self.a + self.b > self.c and self.b + self.c > self.a:
                return "Ура, можно построить треугольник!"
            elif list(i for i in [self.a, self.b, self.c] if i < 0 ):
                return "С отрицательными числами ничего не выйдет!"
            else:
                return "Жаль, но из этого треугольник не сделать."



# class  TriangleChecker:
#     flag = None
#     def __init__(self, data: list):
#         self.a = data[0]
#         self.b = data[1]
#         self.c = data[2]
#         self.data = data
#
#     def check_triangle(self):
#         if list(i for i in self.data if str(i).isalpha()):
#             return "Нужно вводить только числа!"
#         else:
#             if self.a + self.b > self.c and self.b + self.c > self.a:
#                 return "Ура, можно построить треугольник!"
#             elif list(i for i in self.data if i < 0 ):
#                 return "С отрицательными числами ничего не выйдет!"
#             else:
#                 return "Жаль, но из этого треугольник не сделать."



triangle_1 = TriangleChecker(3, "g", -6)
print(triangle_1.check_triangle())
