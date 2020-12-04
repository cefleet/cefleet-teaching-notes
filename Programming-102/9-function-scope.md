# Function scope

## Objectives
- Global scope
- Local scope
- Nested Functions and scope
- Scoping gotchas
- Exercises

## Terms
- *Scope* - `the place in a program where a declared variable can be accessed`

## Global Scope
- ```python
    x = 10  
    #x not declared inside a function. It's a globally scoped variable.
    def add_to_x(a):
        # can access x because it is a global variable 
        return x + a

    print(add_to_x(2)) #12
## Local Scope
- ```python
    def add_two_numbers(a,b):
        c = a+b
        print(c)
        return c
    
    result = add_two_numbers(2,4)
    print(result)

    print(c) # Error c is not in global scope!
- ```python
    def add_two_numbers(a,b):
        c = a+b
        print(c)
        return c

    def add_to_c(d):
        e = c+d
        print(e)
        return e 
    
    add_two_numbers(1,2) #c is in the function, but its local
    add_to_c(12) # errors .. c is not in scope
## Nested Functions and scope
- ```python
    def repeat_stuff():
        x = 10
        def update_x():
            return x + x
        
        while x < 100:
            x = update_x()
            print(x)
    
    #update_x cannot be accessed outside 
    repeat_stuff()
## Gotchas
- ```python
    ## Cannot modify a global inside of a function
    x = 10
    def change_x_to(newX):
        x = newX
        print(x)
        return x

    change_x_to(15) #prints 15..yea! x is 15
    print(x) #x is 10? WTH?!?
- ```python
    def change_x_to(newX):
        global x #saying 'Hey x if your global stay that way or be a global var if not already created'
        x = newX
        print(x)
        return x
    
    change_x_to(15)
    print(x)
- ```python
    x = 10
    def change_x_to(newX):
        global x
        x = newX
        print(x)
        return x

    print(x) #10
    change_x_to(15)
    print(x) #15
- ```python
    # Global variable conditionally set is possible... but not a best practice
    number = int(input("Give me a number:\n"))
    if number > 10:
        x = number * 10
    
    print(x)#if user entered <9 then it will error


## Exercises
1. Create a program that has a global varaible 'name' that is assigned a string value.
    - Define a function that has an parameter called 'message' and will print out the name coma and then the message supplied in the argument when the function is called.
    - call that function 3 times with 3 different messages.
```
    #sample output
    Clint, You are awesome and really tall.
```
2. Create a program that has a global variable 'name' like the exercise above.
    - Have a function that can modify the name variable with a supplied argument.
    - call that function changing the name 3 times.