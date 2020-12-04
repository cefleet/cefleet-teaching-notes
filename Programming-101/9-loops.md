# Loops
## Objectives
- While Loop
- Infinite Loop
- Input to stop a loop

## While loop
- ```python
    i = 0
    while i < 10:
        print(i)
        i  = i + 1
    
    i = 20
    while i <= 30:
        print(i)
        i += 1 #increment syntax
        #deincrement (i -= 1) counts down

## Infinite Loop
- ```python
    i = 0
    while True: #True is always a truthy statement
        print(i)
        i += 1
> You can use ctrl+c to stop the python proccess in the terminal

- ```python
    i = 0
    #accidental loop
    while i < 10:
        print(i)
        #Common mistake - forgot to increment

## Input to stop a loop
- ```python
    name = "" #sets starting value to empty string

    while name != "clint":
        name = input("Please say your name is 'clint'\n")
    
    print('GREAT! I knew you could do it!')

## Exercises
1. Create a program that will print from 1-10 using a while loop.
2. Create a program that will print from 10-1 using a while loop.
3. Create a program that has a variable named username and another variabled named password with values of your choice.
    - Prompt the user for a username and then a password.
    - If the both match continue on with the program and give a welcome message.
    - If not it prompts the user for the username and password until they get it correct.
    - (bonus) have a limited amount of attempts and if they reach the limit it tells the user and exits the program.