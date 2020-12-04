# Comparisons Conditions and Booleans

## Objectives
- What is a comparison
- How to use comparisons for conditions
- Exercises

## Terms
- *Boolean* - `A data type that is always either true or false. It can be represented as 'True' or 'False' or 1 or 0.`
- *If Statements* - `A statement that executes the following code block if the value is true`
- *Code Block* - `A sections of code that is executed in sequence. With python these are created by adding a colon at the end of the line and using indentions to mark the code block. Normally 4 spaces or tab.`

## What is a comparison

- ```python
    #Using comparision operators
    print(1 == 2)   #False
    print(1 <  2)   #True
    print(1 >  2)   #False
    print(1 >= 1)   #True
    print(1 <= 2)   #True
    print(1 != 1)   #False
- ```python
    #Using variables
    a = 1
    b = 2
    print(a == b)   #False
    print(b > a)    #True
- ```python
    #Using Strings
    name = "Clint"
    print(name == "George") #False
    print(name != "Bob")    #True
    print(name == "Clint")  #True
    print(name == "clint")  #False  !?
    print(name > "a")       #False  ?!?!
    print(name < "c")       #True   ?!?!?!

## How to use comparisons for conditions
- ```python
    if 1 > 3:
        print('This will not be printed')
    
    if 1 < 3:
        print('This will be printed')
    
    if False: 
        print('False is never true. No Print')
    
    if True:
        print('True is always true. Print it!')
    
    if 0:
        print('0 is a "falsey" statement. No Print')
    
    if 3: #WTH?
        print('3 exists so it is a Truthy statment. Print!')
## Exercises
1. Write a program that prints out the results of the following statments:
    - ```python
        1 == 3
        4 <= 4
        "a" == "a"
        10 > 11
        "b" > "c"
2. Write a program that assigns the variable "my_number" any number of your choice. And prints out the results of any comparrison with 3 different numbers of your choosing.
3. Write a program that assigns the varaible "name" a string.
    - Create an if statement that compares the value of "name" to another string that has the same value of "name", and if it is the same print "YES these strings are the same!"
    - Create another if statement that compares the value of "name" with a string that does not have the same value, and if it does not have the same value print "NO These strings are different!"