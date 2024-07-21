# Python Standard Libraries

## Objective
- Use Standard libraries
- Download libraries using pip
- using downloaded libraries

## Terms
- *import, importing* - `In programming languages importing means to include libraries or files that are nt declared in the same file`
- *json* - `JSON is javascript object notation, it is a standardized way of writing data that looks much like a javascript object or python dictionary`

## Standard Library

- ```python
    import math #Using the import statement at the top

    math.ceil(23.5) #24
    math.ceil(0.2) #1

- ```python
    import random 
    import os
    import json #Multiple imports at a time.

    random.randrange(12) # some random number between 0 1
    random.randrange(10, 20) #some random number between 10-19

    os.getcwd() #Prints the current working directory
    os.uname() #prints out random info about the system

    myJSONString = json.dumps({"name":"clint", "age":42, "skills":None}) #'{"name": "clint", "age": 42, "skills": null}' //its a string ans None = null

    jsonString = '{"pets":["daisy","molly","rainbow","shadow"], "petTypes":["good","bad"], "results":"Dogs good, cats bad"}'
    dictionaryFromJson = json.loads(jsonString)

    type(dictionaryFromJson) #<class 'dict'>
> There are hundreds of standard imports that can be imported https://docs.python.org/3/library/

## Download using pip
In a Terminal
- ```bash
    pip install emoji
- ```python
    import emoji
    print(emoji.emojize(":thumbs_up:")) # Look an emoji!

- ```python
    from emoji import emojize #only uses the method you want
    print(emojize(":heart:"))
## Exercises
1. Using standard library print out the number of seconds as an integer since the Epoch (December 31 1969), aka Unix time, rounded up to the nearest second. * Searching in the standard library page for "Unix time" should help you.
    - Extra credit get a random time between now and the epoch and print that date in a human readable format. (skip if this is taking to long to figure out.)
2. Write a very small story using emojis colored text using the colorama library from pip. 
    - acceptance criteria:
        - correctly use the import
        - no vulgar, rude, or inappropriate text or emojis. 
        - Emoji list can be found here https://www.webfx.com/tools/emoji-cheat-sheet/

