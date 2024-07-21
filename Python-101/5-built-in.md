## Objective
- Built in Functions
- Built in Constants
- Built in Types

## Terms

## Built in functions
- ```python
    #We have been using one all the time:
    print('Print is a built in function')

    #Other built in functions we have used
    input("what is your name?")

    myString = str(1)

    myNumber = int("0")

> Built in functions can be used without any additional code

> full list of built in functions https://docs.python.org/3/library/functions.html

## Built in Constants
- ```python
    if True:
        print('True is a constant!')
    
    myFalseVar = False

    myEmptyVar = None #none is a constant

    ... #This is a placeholder constant!
## Built in Types
- ```python
    bool # True or False
    str #It's a function and a type?..
    list #function and type again?
    int 
    float
- ```python
    # testing types
    type(1.34) #<class 'float'>
    type('i heart programming') #<class 'str'>

    # using checked type
    myName = 'Clint'
    if type(myName) is str:
        print(myName+' is a good name!') 
- ```python
    #Side note what about types of custom items
    class Guy:
        ...
    
    bob = Guy()

    type(bob) #<class '__main__.Bob'> 
    #ok the instance of Bob is type
    type(Guy) #<class 'type'> # WHA? we created a type?

    if type(bob) is Guy:
        print('Oh this is kinda neat')  
## Exercises
1. Write a program that uses the uses the following standard functions at least one time each. round, range and reversed.
    - The functions mentioned are in the link given earlier in the lesson.
    - Doing a google search like "How to use reversed in python" can help you find how to use the functions.
2. Write a program that has 3 different classes Person, Friend, and Foe with a property of name and any other properties you may want.
    - create an instance of the Person class and 2 instances of each class Friend and Foe
    - For every instanced item (there should be 4) print out "{person.name} is {friend or foe} of {other instanced item}. for example the output should be:
    ```bash
        Clint is a foe of Shadow
        Clint is a friend of Daisy
        Clint is a foe of Rainbow
        Clint is a friend of Molly
    ```
    - Negative points for being a smart alic and just writing the print statements without using classes properly.
    - Bonus points for using a list