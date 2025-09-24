class Human:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def info(self):
        return f"{self.first_name} {self.last_name} {self.age}"


    def __str__(self):
        return f"{'{'} first_name:{self.first_name} {'}'}"

    def __int__(self):
        return len(self.first_name)

    def __add__(self, other):
        return Human(self.first_name, self.last_name, self.age + other.age)

    def __eq__(self, other):
        return (self.first_name == other.first_name
                and self.last_name == other.last_name
                and self.age == other.age)

    def __lt__(self, other):
        return self.age < other.age

    # def __repr__(self):
    #     return "<class 'Human'>"

# human = Human("Nadir", "Zamanov", 44)
# human1 = Human("Nadir", "Zamanov", 35)
#
#
# human3 =  human + human1
# print(human3.info())
#
# print(human1 == human)
# print(human1 < human)

# print(15 + 25.5)

# lst = [25, 87, 15]
# print(list)