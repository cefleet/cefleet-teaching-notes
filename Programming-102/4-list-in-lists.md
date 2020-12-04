# Lists in Lists

## Objectives
- List in List
- Accessing nested lists
- Looping through nested lists
- Exercises

## List in List
- ```python
    #List of first and last, names, age
    people = [["Clint","Fleetwood", 38], ["Anna", "Fleetwood", 37]]

    #List of coordinates x,y
    coordinates = [[10,10],[20,10],[10,20]]
- ```python
    #List can be written to be easier to read
    coordinates = [
        [10,10], #Can comment per line!
        [20,10],
        [10,20]
    ]
## Accessing nested list
- ```python
    people = [
        ["Clint","Fleetwood", 38], 
        ["Anna", "Fleetwood", 37]
    ]
    print(people[0]) #["Clint","Fleetwood", 38]
    print(people[0][0]) #Clint

    #assigning result of expression to variable
    age = print(people[1][2]) #37

    #You can modify the array in place the same way
    people[0][2] = 39 
    del people[1][2]
    print(people)
## Looping thorugh nested lists
- ```python
    people = [
        ["Clint","Fleetwood", 38], 
        ["Anna", "Fleetwood", 37],
        ["Peter", "Hollens", 34],
        ["Lindsey", "Sterling", 35]
    ]

    for person in people:
        print("First, Last, Age")
        for attribute in person:
            print(attribute)
- ```python
    coordinates = [[10,10], [20,10],[10,20]]

    for cord in coordinates:
        idx = 0
        print("Position:")
        for position in cord:
            p = "X"
            if idx == 1:
                p = "Y"
            print(f"{p}-{position}")
            idx += 1
## Exercises
1. Write a program that has a list of shopping lists that where each list is for a different food group.
    - Print each full list on a seperate line.
```python 
['Corn','Potatoes','Tomatoes']
['milk','eggs','cheese','yogurt']
['frozen pizza','popsicle']
```
2. Using the code from the previous exercise, have each grouping have a title with the number in the title and each item of the list have a number in front of the item.
    - (bonus) Have each of the titles of the main grouping be in a seperate list that gives the name to the heading.
```python
1. Veggies
    1. Corn
    2. Potatoes
    3. Tomatoes
2. Cold Items
    1. milk
    2. eggs
...etc
```
    