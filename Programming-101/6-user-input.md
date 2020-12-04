# User Input

## Objectives
- How to receive user input
- Exercises

## Terms

- *Blocking* - `In programming blocking is refered to when the code is waiting for something else to happen (computation, user input, request return etc) before moving onto the next line of code`
- *Type Casting* - `Type casting is turning one value type into another data type.`

## How to receive user input
- ```python
    name = input('Name Please:') #input is blocking
    print(f"Your name is {name}")

    subject = input("Favorite Subject?\n")
    # \n pushes the input down
    print("You chose %s as your subject" % subject)

    age = input('How old are you?\n')
    if age >= 21: #<- error caused here
        print('You are old enough')
> You need to cast the input which is always a string into an integer if you are going to compare it to an integer. You do this by wrapping the value in int().
- ```python
    age = input('How old are you?\n')
    if int(age) >= 21: #<- error caused here
        print('You are old enough')


## Exercises
1.  Create a program that prompts the user for their name. Once the name is recieved replay a greeting that includes their name.
2. Create a program that will prompt the user for their first name and then after they enter their first name prompt for their last name.
    - After they have entered both, print a greeting that includes their first and last name.
