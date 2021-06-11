class MyClass:  # define classs


    x = 10
    y = 20

o = MyClass()  # object create
print(o.x)
print(o.y)

###############################################################
# __init__() Function


class Student:

    def __init__(self, first, last, marks):
        self.first = first
        self.last = last
        self.marks = marks

std_1 = Student('Ram', 'Sharma', 70)
std_2 = Student('Adi', 'Sharma', 60)

print(std_1.first)
print(std_2.last)
print(std_1.marks)
print(std_2.marks)

print('{} {}' .format(std_2.first, std_2.last))

