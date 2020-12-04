# else and elif

## Objectives
- Using else and elif
- Exercises

## using else and elif
- ```python
    age = input('How old are you?\n')
    if int(age) >= 21:
        print('You are old enough')
    else:
        print('You are not old enough')

- ```python 
    age = input('How old are you?\n')
    age = int(age)

    if age == 21:
        print('Looks like your lucky year')
    elif age > 21:
        print('You are old enough')
    else:
        print('You are not old enough')
    
    #It will stop after a truthy condition
    if age > 18:
        print('Getting close')
    elif age > 21:
        print('you are old enough')
    else: 
        print('You are too young')

## Exercises
1. Create a program that prompts the user for a number and compare that number with random number of your choice.
    - If the number is too high tell the user.
    - If the number is too low tell the user.
    - If the number is correct tell the user.