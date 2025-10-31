class Point:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def get_coords(self):
        return self.__x, self.__y


class Rectangle:
    def __init__(self, x1, y1, x2=None, y2=None):

        if isinstance(x1, Point) and isinstance(y1, Point):
            self.__sp = x1
            self.__ep = y1
        elif all(map(lambda x: type(x) in (int, float), (x1, y1, x2, y2))):
            # создаем объекты класса Point, но программа считает, что Point не принимает аргументов
            self.__sp = Point(x1, y1)
            self.__ep = Point(x2, y2)

    def set_coords(self, sp, ep):
        self.__sp = sp
        self.__ep = ep

    def get_coords(self):
        return self.__sp, self.__ep


    def draw(self):
        print(f"Прямоугольник с координатами {self.__sp.get_coords()}), {self.__ep.get_coords()}")


point = Point(1, 2)
rect = Rectangle(Point(12, 10), Point(14, 16))
rect2 = Rectangle(0, 1, 2, 3)
print(point.get_coords())
rect.draw()
rect2.draw()