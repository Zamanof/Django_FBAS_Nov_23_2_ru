from logging import raiseExceptions


class Human:
    # name = None
    # surname = None
    count = 0 # class attribute
    def __init__(self, name, surname, age, mark):
        self.name = name    # object attribute
        self.surname = surname
        self.__age = age if age > 0  else 0     # __private
        self._mark = mark    # _protected
        Human.count += 1

    def show_info(self):
        print(f"{self.name} {self.surname} {self.__age} {self._mark}")

    def initialize(self, name, surname):
        self.name = name
        self.surname = surname

    # def set_age(self, age):
    #     self.__age = age if age > 0  else 0
    #
    # def get_age(self):
    #     return self.__age

    # python property

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.__age = age if age > 0 else 0


    @staticmethod
    def show_count():
        print(Human.count)


# Human.show_count()

human = Human("Nadir", "Xamanov", 44, 8.6)
# print(human.name)
# print(human.surname)
# human.initialize("Salam", "Salamzade")
# human.show_info()
#
# print(Human.count)
# Human.count+=1
# human.count += 10
# print(human.count)

# Human.show_count()
# human.show_count()
# human.set_age(89)
# print(human.get_age())

# human.age = -5
# print(human.age)


# print(dir(human))
# print(Human.__dict__)
# print(dir(Human))

# print(Human.count)
# Human.count = 25
print(human.__dict__)
human.count = 25
print(human.__dict__)
# print(Human.count)
# print(human.count)

# magic methods, Inheritance, "утиная типизация"   
