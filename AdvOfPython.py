# Polymorphism

# Polymorphism (in-built functions) - Program
print(len("arcworkshop"))
print(len([10, 20, 30]))

# Polymorphism (user-defined functions) - Program

def add(p, q, r = 0):
    return p+q+r

print(add(10, 20, 30))
print(add(10, 20))



# Polymorphism (with class functions)


class Nepal():
    def capital(self):
        print("Kathmandu is the capital of Nepal.")

    def language(self):
        print("Nepali is the primary language of Nepal.")

class USA():
     def capital(self):
         print("Washington, D.C. is the capital of USA.")

     def language(self):
         print("English is the primary language of USA.")

obj_nep = Nepal()
obj_usa = USA()
for country in (obj_nep, obj_usa):
        country.capital()
        country.language()

# Polymorphism in Inheritance (Method Overriding) - Program

class parent:
    def fun1(self):
        print("This is function-1.")

class child(parent):
    def fun1(self):
        print("This is function-2.")

obj = child()
print(obj.fun1())





############################################################################################
# Inheritance

class Vehicle:   # parent/base class
    def type(self):
        print("Types of Vehicle")


class Trucks(Vehicle):   # child/derived class
    def q(self):
        print("Heavy vehicle")


t = Trucks()
t.q()
t.type()

# Types of Inheritance (Single, Multi-level, Multiple, Multi-path, Hierarchical & Hybrid) (SS)
###########################################################################
# Abstraction - Program

from abc import ABC, abstractmethod

class Employee(ABC):
      @abstractmethod  # keyword

      def sal(self, sal):
          pass
      
class Developer(Employee):
      def sal(self, sal):
          fsal = sal*10
          return fsal

e1 = Developer()
print(e1.sal(10000))





