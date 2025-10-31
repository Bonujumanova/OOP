class Book:

    def __init__(self, title, author, price):
        self.__title = title
        self.__author = author
        self.__price =price
        pass


    def set_title(self, title):
        self.__title = title


    def set_author(self, author):
        self.__author = author


    def get_title(self):
        return self.__title


    def get_author(self):
        return self.__author


    def get_price(self):
        return self.__price


book = Book("M.Cervantes", "Don Quixote", 3000)
print(book.get_author())
print(book.get_price())
print(book.get_title())