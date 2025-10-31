class Clock:

    def __init__(self, time):
        self.__time = 0
        if self.__check_time(time):
            self.__time = time

    @property
    def prop(self):
        return self.__time
    @prop.setter
    def prop(self, tm):
        if 0 < tm < 100000:
            self.__time = tm

    def set_time(self, tm):
        if self.__check_time(tm):
            self.__time = tm

    def get_time(self):
        return self.__time
    #Почему интерпретатору не нравится этот метод? Потому что этот метод принадлежит экземпляру?
    # Тк проверка осуществляется внутри класса и экземпляр никак не будет взаимодействовать в данным методом?
    # def __check_time(self, tm):
    #     return 0 < tm < 100000 and type(tm) == int

    @classmethod
    def __check_time(cls, tm):
        return 0 < tm < 100000 and type(tm) == int


clock = Clock(-5)
print(clock.get_time())
clock.set_time(15)
print(clock.get_time())
clock.prop = 10000
print(clock.prop)