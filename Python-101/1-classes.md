# Classes

## Objective
- Defining and Instantiating classes 
- class constructor
- using self
- default values
- Exercises

## Terms
- *Instantiation* - `In programming terms this is creating an self contained 'instance' of a class that can be used in the program.`
- *attributes* - `Are values in a class that can be accessed using the accessed using the attribute name. Much like key in a dictionary`

## Defining and Instantiating classes
- ```python
    class Person:
        pass #this simply allows you to create an empty class
    
    clint = Person()
    anna = Person()

- ```python
    class Person:
        def __init__(ignore_for_now):
            print('You have initilized the person class')

    #__init__ is special and called automatically, otherwise it's just a function

    clint = Person() 
    anna = Person()

- ```python
    class Person:
        def __init__(self):
            #using self allows us to modify the class
            # name attribute
            self.name = "Clint"
            # age attribute
            self.age = 38

    clint = Person()
    print(clint.name)
> When __init\__ is automatically called, it is given the first argument which is a reference to the instance of the object itself. Thus when defining the __init\__ function it is expected to use self as the name for the first argument.
## Using self
- ```python
    class Person:
        def __init__(self, name, age):
            self.name = name
            self.age = age

    clint = Person("Clint", 38)
    anna = Person("Anna", 37)

    print(clint.name, clint.age)
    print(anna.name, anna.age)
## default values
- ```python
    class Person:
        # adding a default value for height
        def __init__(self, name, age, height="normal"):
            self.name = name
            self.age = age
            self.height = height

    clint = Person("Clint", 38, "short")
    anna = Person("Anna", 37)

    print(clint.name, clint.age, clint.height)
    print(anna.name, anna.age, anna.height)

## Exercises
1. Create a program that has a class named Vehicle.
    - Mae the Vehicle have a 'category' which can be anything like, sport, truck, motorcycle, minivan.
    - Make the Vehicle class have 'wheels' as an attribute.
    - Make the Vehicle class have 4 as the default value for the class.
    - Create 5 different instances of the class with at least one being a motorcycle.
