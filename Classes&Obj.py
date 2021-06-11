# self parameter and object functions


class MyProfile:
    def __init__(silly, name, age):
        silly.name = name
        silly.age = age

    def fun(silly):
        print("My name is ", silly.name)


a = MyProfile("Julia", 20)
a.fun()

######################################################################
#Obj. Modification


class Student:

    def __init__(self, first, last, marks):
        self.first = first
        self.last = last
        self.marks = marks


std_1 = Student('Ram', 'Sharma', 70)
std_2 = Student('Adi', 'Singh', 50)


# modifying object properties
std_1.marks = 90
print('Marks = ', std_1.marks)

std_2.first = 'Shyam'
print('First name = ', std_2.first)

# deleting object properties
#print(std_2.last)
#del std_2.last
print(std_2.last)

print(std_2.first)

# deleting object
print('{} {}'.format(std_2.first, std_2.last))
print(std_2.marks)

#del std_2
print(std_2.marks)

##############################################################################################
# Pass Statement


class Person:
    pass


p1 = Person()
p2 = Person()

p1.name = 'Hari'
p1.email = 'Hari@gmail.com'

p2.name = 'Shyam'
p2.email = 'Shyam@gmail.com'

print(p1.email)
print(p2.name)

