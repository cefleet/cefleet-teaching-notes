# Lists

## Objectives
- What are the parts of a list?
- Creating lists
- Accessing items from a list
- Exercises

## Terms 
- *lists* - `Lists are a data type of ordered gropuing of values. They are called arrays in most other languages.`

- *index* - `In a list or an array, it is the number representation of the position of an item in the list or array`

## What are the parts of a list?

- ```python
    [1,2,3] #List of intergers
    ["hi", "my", "name", "is", "Clint"] #List of strings
    [1,"stringy", False] # List of mixed types
> List start with an opening square bracket '[' have coma seperated values and then end with the closing sqaure bracket ']'.

## Creating lists
- ```python
    # creating a list and assigning it to a variable
    some_numbers = [1,2,3]
    my_children = ["Olivia", "Alle", "Mark"]

    name = "Clint"
    age = 38
    married = True
    my_info = [name, age, married] 
    #Putting the variables in the array
## Accessing items from a list

- ```python
    my_children = ["Olivia", "Alle", "Mark"]
    print(my_children[0]) #Olivia
    print(my_children[2]) #Mark
    print(my_children[1]) #Alle
>Lists are ordered so the order will remain the same.

>The list starts with 0, so the first item is always 0 and counts up in order.

- ```python
    my_children = ["Olivia", "Alle", "Mark"]
    #Assigning the results to a variable
    only_son = my_children[2]
    print(only_son) #Mark
## Exercises
1. Create a program that has a list of at least 3 of your favorited foods in order and assign that list to a variable named "favorite_foods".
    - print out the value of your favorite food by accessing by it's index.
    - print out the last item on the list as well.

2. Create a program that contains a list of 4 different "things" around you.
    - Print out the each item on a new line with the number of it's index in front of the item.

    ```python
    0. Coffee Cup
    1. Speaker
    2. Monitor
    3. Keyboard
    ```

3. Using the code from exercise 2, prompt the user for which item the user thinks is the most interesting. Tell the user to use numbers to pick. (IE 0-3). 
    - When the user has entered the value print out the selection that the user chose with some sort of pithy message associated with the choice.

    ```python
        "You chose Coffee Cup, You must like coffee!"