# Iterate through lists

## Objectives
- Loop through list with while
- Loop using for
- Exercises

## Terms 
- *Iterate* - `In programming to interate is to repeat actions on a set list or grouping of items`

## Loop through list with while
- ```python
    my_children = ["Olivia", "Alle", "Mark"]
    index = 0
    #When using a list len() counts the number of items
    while index < len(my_children):
        print(index+1,my_children[index])
        index += 1
## Loop using for
- ```python
    my_children = ["Olivia", "Alle", "Mark"]
    #child is the value of the current item in the iteration
    for child in my_children:
        print(child)

## Exercises
1. Using a while loop create a program that prints the values of your favorite movie stars.
    - have a number in front of the printed name.

2. Using a for loop, re-do the above exercise.
    - (hint) you still need to create a variable that is incrimented.

3. Create a program that will add the values of a list of numbers, and then print out the results.
    - (hint) You will need to create a variable to hold the current value.
    - Repeat with several different lists of numbers of different lengths.
```python
    # the list of numbers is [1,2,3]
    #output to console
    6