# Error Handling

## Objectives 
- Try / Except in action
- Error Types
- When/how to use Try / Except and when not to
- Exercises

## Terms
- *Error Handling* - `As the name implies, error handling (sometimes called error catching), in programming terms is how the developer can manage and handle inputs and other actions from a user or outside source that would cause the program to 'crash'`

## Try / Except in action

- ```python
    #Creating an error
    if 2 > "3":           # Number compared to a string
        print('Never Prints')
    
- ```python
    # Handling error
    try:
        if 2 > "3":
            print('Never Prints')
    except TypeError:
        print("The program doesn't crash now")

## Error Types
- ```python
    #still crashes
    try:
        impossible = 100/0
    except TypeError:
        # Trying to catch the wrong error type
        print('You cannot divide by 0')

- ```python
    #fixed and has more than one error catch
    try:
        impossible = 100/0
    except TypeError:
        # Trying to catch the wrong error type
        print('It does not get here')
    except ZeroDivisionError:
        print("You cannot divid by 0")

> TypeError, SyntaxError, ValueError and ZeroDivisionError are some of the common errors.

## When/how to use Try / Except and when not to

- ```python 
    try:
        imp = 100/0
    except: #Technically you can have a catchall
            #but this is BAD
        print('You cannot divide by 0')

- ```python
    try:
        imp = 100/"0" #This is a type error
    except:
        #This tells the developer the wrong information!
        print('You cannot divid by 0!')
>try / except should be as explicit as possible to prevent bugs that are hard to find.

>Do not use try/ except to attempt to cover improper coding practices or sloppy code. 

>Do use try / except to handle user input or data returned from a source you as the developer are not in control of.

- ```python
    input_string = input("Give me a number please!\n")
    # inputs are a string so we need to convert it
    try:
        number_value = int(input_string)
        print("Our number is %s" % number_value)
    except ValueError: 
        print('You did not give a number')

## Excercises
1. Create a program that asks the user for a number and then prints from that number to 0.
    - Handle the error if the user enters something other than a number.
1. Create a program that ask a user for two numbers and then returns the sum (add), product(multiply), and quotient (division) of the two numbers.
    - Catch all errors possible from the user and explicitly tell the user what caused the error.