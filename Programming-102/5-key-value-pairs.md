# Key Value Pairs

## Objectives
- What is a key/value pair?
- accessing values from dictionaries
- updating values in dictionaries
- loop through dictionaries
- List of dictionaries
- Exercises

## Terms
- *Dictionary* - `In python, a dictionary is a data type that is a grouping of data that uses keys to point to a value. Some languages have data types that are similer called things like maps, structs, or objects.`
- *Key* - `In programming, a key is string, int, or one of a varity of data types that will allow the developer to access a value.`

## What is a key/value pair?
- ```python
    # Key value pairs in python are dictionaries
    movie = {
        "name":"Star Wars",
        "episode":4,
        "year":"1977"
    }
- ```python
    #Dictionaries can have multipe data types as values
    movie = {
        "name":"Star Wars",
        "episode":4,
        "year":"1977",
        "villans":["Vader", "Tarkin"],
        "heros":["Luke","Leia", "Han", "Obi-Won"]
    }

## Accesing key/value pair
- ```python
    movie = {
        "name":"Star Wars",
        "episode":4,
        "year":"1977",
        "villans":["Vader", "Tarkin"],
        "heros":["Luke","Leia", "Han", "Obi-Won"]
    }
    #print from dictionary
    print(move["name"]) 
    #assign to variable
    episode_num = movie["episode"]

    #accessing a value from an array in the dictionary
    print(movie["heros"][1]) #Leia

    # the key can be a variable
    search = "villans"
    print(movie[search])

- ```python
    #check for existance
    if "ships" in movie:
        print(movie["ships"])
    else:
        print("We need to add ships")
    
    # if not
    if "ships" not in movie:
        print("We need to add ships")

- ```python
    #adding to the current string
    movie["name"] = movie["name"]+" - A new Hope"

    #Adding a new item
    movie["ships"] = ["Falcon", "Star Destroyer", "Death Star"]

    #Adding to an element inside of an list
    movie["heros"].append("Chewbacca")

## Loop through dictionary
- ```python
    for key in movie:
        print(key) #Just prints the keys
    
    for key in movie:
        print(movie[key]) #the key is a variable

>There are other ways to loop through dictionaries that we will cover later.

# List of dictionaries
- ```python
    movies = [
        {
            "name":"Star Wars - A new Hope",
            "episode":4,
            "year":"1977"
        },
        {
            "name":"Star Wars - The Empire Strikes Back",
            "episode":5,
            "year":"1980"
        },
        {
            "name":"Star Wars - Return of the Jedi",
            "episode":6,
            "year":"1983"
        }
    ]
    #get item from list
    print(movies[0]["name"])

    #loop through list of dictionaries
    for movie in movies:
        print("%s was episode %s and release in %s" % (movie["name"], movie["episode"], movie["year"]))
## Exercises
1. Create a program that starts with an empty dictionary.
    - Add 3 different key value pairs to the empty dictionary. 
2. Create a program with a dictionary called person.
    - The person dictionary needs to have the keys, first_name, last_name, age, hair_color.
    - Print each one of these key/values pairs without directly using the key's name as a string by using a for loop.
    - After each key value pair, print out a sentence using each one of the keys. 
    ```
        Hello Clint Fleetwood. Since you are 38 years old you are too old to ride this ride, but you do have nice brown hair.
3. Create a program that has a list of dictionaries of people, with each dictionary including name, phone, email.
    - For each dictionary print the items in the dictionary. 