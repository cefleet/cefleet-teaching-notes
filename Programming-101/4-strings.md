# Strings

## Objectives
- Different types of strings
- Combining strings
- Special characters
- Exercises

## Terms
- *Literal* - `A value that is not a variables.`
- *Concatenate* - `Joining two or more items together.`

## Different Types of Strings
- ```python
    'Look a String!'
- ```python
    "Look another string!?"
- ```python
    '''
        Hey this string
        can span
        mutiple lines?
    '''
- ```python
    """
        This one
        can too!
    """

## Combining Strings

- ```python
    "hello"+"world"         

    "hello"+" "+"world"     

    "hello "+"world" 
- ```python
    message = "hello"
    print(message+" "+"world")
    #The variable is the 'type' of the assigned value
- ```python
    message = "Hello Word"
    name = "Clint"

    #f-string syntax
    combined = f"I want to say {message} to {name}"
    print(combined)
- ```python
    name = "Clint Fleetwood"
    #interpolation syntax
    print("Hello %s, it is nice to meet you", % name)

    first_name = "Clint"
    last_name = "Fleetwood"
 
    print('Hello %s %s, it is nice to meet you' % (first_name,last_name))

## Special Characters
- ```python
    #escape string
    haiku = "Haikus are easy.\nBut sometimes they don't make sense.\nRefrigerator."
    print(haiku)
    #using single quote in string
    tabbed = "Look\tI'm tabbed"
    print(tabbed)
    #using double quote in string
    sarcastic = 'I "really love" talking politics'
    print(sarcastic) 

## Exercises
1. Create a program that prints out the combination of two different strings.
2. Print out a haiku that spans across multiple lines using only a single string.
3. Create a program that prints the following 3 times: 
- ```
    Hello [person], 
    I hope that your [today] is going well. 
    I'm personally really [emotion].
- Where [person], [today], [emotion] are variables and using 3 different syntaxes. 
- ```
    Hello Clint,
    I hope that your Thursday is going well.
    I'm personally really well.