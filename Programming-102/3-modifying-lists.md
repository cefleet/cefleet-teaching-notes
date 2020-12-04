# Modifying Lists

## Objectives
- Appending values
- Concatenating lists
- Extending lists
- Assign value by index
- Deleting by index

## Terms
- *Method* - `In python(and other languages) a method is a function that a datatype can run from it's own instance`

## Appending Values
- ```python 
    my_pets = ["Daisy", "Molly", "Shadow"]
    my_pets.append("Rainbow") #using append method
    print(my_pets) #You can simply print an array

## Concatenating Lists
- ```python
    my_dogs = ["Daisy", "Molly"]
    my_cats = ["Shadow", "Rainbow"]
    my_pets = my_dogs + my_cats
    print(my_pets) #combines both
    print(my_dogs) #doesn't change the original list

- ```python
    combined_literal = [1,2,3] + ['a','b','c']
    print(combined_literal)

## Extending Lists
- ```python
    my_pets = [] #empty list
    my_dogs = ["Daisy", "Molly"]
    my_cats = ["Shadow", "Rainbow"]
    my_pets.extend(my_dogs) 
    #extend method modifies the array
    print(my_pets)
    my_pets.extend(my_cats)
    print(my_pets)

## Assign Value by index
- ```python
    my_pets = ["Daisy", "Molly", "Shader", "Rainbow"]
    my_pets[2] = "Shadow"
    print(my_pets)#now its Shadow at index 2

## Deleting Value by index
- ```python
    my_pets = ["Daisy", "Molly", "Shadow", "Rainbow"]
    del my_pets[3]
    print(my_pets)#now rainbow is gone

## Exercises
1. Write a program that has a list of names. 
    - Add two new names to that list.
    - Print the results.
2. Write a program that has 5 names in a list.
    - Replace the items at index 2 and 4 with "Foo" and "Bar" respectively.
3. Write a program that has a list of 5 names.
    - Loop through the array printing the item at index 0 and then removing that item from the array until there are no items in the array.
    - (hint) This will use a while loop.