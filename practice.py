# Using modules
import Modules

Modules.greet("We are ARC Team.")
Modules.greet("It's nice to have you all.")

################################################################
# Adding to modules and displaying it

import Modules

a = Modules.Birds["name"]
print(a)

#################################################################
# Renaming a module

import Modules as md

a = md.Birds["color"]
print(a)

################################################################
# Built-in Modules

import math
print("The value of pi is ", math.pi)

###############################################################
# dir() function

import math

p = dir(math)
print(p)

import abc

q = dir(abc)
print(q)