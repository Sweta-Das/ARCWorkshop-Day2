# ARCWorkshop-Day2
Python Codes for understanding Classes, Objects, Modules, and PIP.
## Class
A class is the user-defined blueprint of objects. It provides a means of bundling data & functionality together. The syntax for class definition:

>>class Class_Name:<br/>
    //body_statement

The class creates a user-defined data structure, which holds its own data members and functions together. Some key points related to Python class:
  - Classes are created by the keyword "class".
  - Attributes are the variables that belong to a class.
  - Attributes are always public and can be accessed using the dot (.) operator.
    E.g., class.My_attribute

## Object
An object is an instance of a class i.e., a copy of the class with actual values. An object consists of:
  - State => represented by the object attributes and reflects the properties of the object.
  - Behavior => represented by the object methods and reflects the response of an object to other objects.
  - Identity => gives the object a unique name and enables the object to interact with another object.

The syntax for object:

>>obj = ClassName() <br/>
>>print(obj.attr)


![Class Obj](https://github.com/Sweta-Das/ARCWorkshop-Day2/assets/73231461/8286a563-52d7-46c5-90e4-2fe7855f783c)
<br/>P.C. https://intellipaat.com/mediaFiles/2019/03/python10.png


## Modules in Python
A module is a file written in Python and saved with a ".py" file extension. It organizes code into logical units, promotes code reuse, and makes maintaining and understanding the codebase easier.<br/>
Python provides a rich set of modules in its standard library with pre-written modules that get downloaded with the installation of Python. These modules cover a wide range of functionalities, such as file I/O, networking, database access, mathematical operations, data serialization, etc.<br/>
To use a module in Python:<br/>
import module_name <br/><br/>Or,<br/><br/>
from math import module_name<br/><br/>
User-defined modules can also be created by defining functions, classes, or variables in a .py file and then importing them into other Python scripts.
Python also allows downloading of 3rd-party modules using "pip" package managers.

## PIP in Python
PIP is the abbreviation of "Python Package Installer". It's a package manager for Python, which is used to install, upgrade, and manage software packages or libraries written in Python. It lets us easily install packages from the Python Package Index (PyPI) and other sources.<br/>
Some of the commonly used commands of PIP:<br/>
1. Installing a package. <br/>
>>pip install package_name <br/><br/>
2. Installing a specific version of a package.<br/>
>>pip install package_name==version_number<br/><br/>
3. Upgrading a package.<br/>
>>pip install --upgrade package_name<br/><br/>
4. Uninstalling a package.<br/>
>>pip uninstall package_name<br/><br/>
