from tokenize import group


class Human:
    count = 0
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def show_info(self):
        return f"{self.first_name} {self.last_name} {self.age}"


class Student(Human):
    def __init__(self, first_name, last_name, age, group, mark):
        super().__init__(first_name, last_name, age)
        self.group = group
        self.mark = mark

    def show_info(self):
        return f"{super().show_info()} {self.group} {self.mark}"


student = Student(
    "Nadir",
    "Zamanov",
    45,
    "FBAS_Nov_23_2_ru",
    10.5
)

print(student.show_info())

# @abstractmethod
# C#, C++ (inheritance, polymorphism, encapsulation, abstraction)