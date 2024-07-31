# Splitting code into modules
## Objective
- Splitting code into multiple files
- Creating packages

## Terms
- *module* - `A module is a piece of code that is self contained and manages it own functionality. In python a module is almost always a separate file`
- *package* - `Python Packages are a way to organize and structure your Python code into reusable components. `

## Splitting code into multiple files

- ```python
    #./words.py
    wordsList = []
    def getWords():
        return wordsList
    
    def addWord(word):
        wordsList.extend([word])
- ```python
    #./main.py
    import words

    words.addWord("yes")
    words.addWord("no")

    print(words.getWords()) #['yes', 'no']
- ```python
    # alternative ./main.py
    from words import addWord, getWords

    addWord("maybe")
    print(getWords())

## Creating packages
Using our hero / unit example we can split the files into 
- ```python

    # classes/unit.py
    class Unit():
        def __init__(self, configData):
            self.name = configData['name']
            self.health = configData['health']

- ```python
    # classes/units/hero.py
    from classes.unit import Unit

    class Hero(Unit):
        def __init__(self,configData):
            super().__init__(configData)

        def yellAt(self, unit):
            print("I %s, say to thou %s. Prepare to die!" % (self.name, unit.name))
- ```python
    # classes/units/enemy.py
    from classes.unit import Unit

    class Enemy(Unit):
        def __init__(self, configData):
            super().__init__(configData)
        
        def spitAt(self, unit):
            print("I spit at you sir %s" % unit.name)

- ```python
    # main.py
    from classes.units.hero import Hero
    from classes.units.enemy import Enemy

    hero = Hero({"name":"awesome guy", "health":"100"})
    print(hero.name)
    enemy = Enemy({"name":"Really Bad Guy","health":"75"})

    hero.yellAt(enemy)
    enemy.spitAt(hero)

## Exercises
1. Going back a few lessons, using the car example. Split every sub class into it's own file and make a file structure system that follows the pattern given in the lesson. 
*There are several ways to accomplish this.
