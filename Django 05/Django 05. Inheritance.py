class Human:
    count = 0
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age



class Student(Human):
    def __init__(self, first_name, last_name, age, group, mark):
        super().__init__(first_name, last_name, age)
        self.group = group
        self.mark = mark


student = Student(
    "Nadir",
    "Zamanov",
    45,
    "FBAS_Nov_23_2_ru",
    10.5
)
# print(isinstance(student, Human))
# print(issubclass(Student, Human))
# print(issubclass(Student, object))

#
# print(isinstance(int, object))

print(student.first_name)

