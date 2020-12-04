# Function arguments and parameters

## Objectives
- function arguments
- function parameters
- using parameters and arguments
- Exercise

## Function arguments
- ```python
    print('Hello World') #The string 'hello world' is an argument
    print(1,2,3) # more than one argument

    my_list = ['I','am','a','list']

    len(my_list) #my_list is an argument
## function parameters
- ```python
    # a and b are parameters
    def add_two_numbers(a,b):
        print(a+b)
    
    # a list datatype 
    def print_list(a_list):
        for item in a_list:
            print(item)
## Using Parameters and Arguments
- ```python
    # Functions from above example
    add_two_numbers(10,20)
    print_list(["I","Am","Awesome"])

    a = 10
    b = 10
    add_two_numbers(a,b)
> In python and many other languages the number of arguments must match the number of parameters that the function expects. There are some exceptions to this rule.

- ```python
    # Order matters
    def tell_me_stuff(first_name, age, gender):
        print(f"My name is {first_name}")
        print(f"I am {age} years old.")
        print(f"I am {gender} human")

    tell_me_stuff("Clint", 38, "Male")
    tell_me_stuff("Male", "Clint", 38)


- ```python
    #Giving the wrong type causes an error
    add_two_numbers("foo", "bar")


## Exercies
1. Creat a program that has a function that will multiply two numbers together and print out the results.
    - Make the program properly handle an exception if something besides a number is passed as an argument.
    - Have it print out 3 different sets of numbers

2. Create a program that has a function that will accept 3 arguments as title, genre, year and then print out the values in list format.
```
    1. Title : Star Wars - A new Hope
    2. Genre : Sci-Fi
    3. Year  : 1977
```
3. Create a program that does the same thing as above, but the function only accepts a single argument to get the same results.
    - (hint) - You will need to use a datatype other than a string in the argument.
