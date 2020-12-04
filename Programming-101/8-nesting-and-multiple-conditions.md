# Nesting Code Block
## Objective
- Put code blocks inside of code blocks
- Use multiple condition
- Exercise

## Terms
- *Nesting* - `In programming nesting describes putting code blocks or other syntaxtual items inside of another item`

## Put code blocks inside code blocks
- ```python
    name = input("what is your name?")
    # wrapping a string / varaible in len() outputs how many characters the string is.
    if len(name) > 3:
        print('Your name is long enough')
        if len(name) > 15:
            #new block level
            print("That's way to long partner")
        else:
            print(f"Welcome {name}")
    #back out to the main block level
    else:
        print('%s is too few characters' % len(name))

- ```python
    name = input("What is your name")

    if len(name) > 3:
        if len(name) < 10:
            if len(name) == 4:
                # Even one block lower
                print('Perfect Length!')
            else:
                print("It's an ok length")
            
            print(f"Welcme {name}")
        else:
            print("That's way to long partner")
    else:
        print('%s is too few characters' % len(name))

## Using multiple conditions 
- ```python
    name = input("what is your name?")
    num = len(name)
    ## You can have multiple conditions here
    if num > 3 and num < 15:
        if num = 4:
            print('Perfect Length!')
        else:
            print("It's an ok length")
            
        print(f"Welcme {name}")
    else:
        print('%s is not a good number of characters' % len(name))

## Exercises
1. Create a program that will accept in input that is assigned to the variable pet_name. 
    - If pet_name length is less than 3 characters give a message that the name length is too short.
    - If pet_name lenght is more than 3 characters output "AWWW sweet [pet_name]"
    - If pet_name is "Shadow" output ONLY "El Gato Diablo!"
    - If the input is equal to "Daisy" output ONLY "Good Dog!" 
