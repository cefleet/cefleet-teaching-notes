# Splitting code into modules
## Objective
- Splitting code into multiple files
- Creating packages

## Terms
- *module* - `A module is a piece of code that is self contained and manages it own functionality. In python a module is almost always a separate file"

## Splitting code into multiple files

- ```python
    #./words.py
    wordsList = []
    def getWords():
        return wordsList
    
    def addWord(word):
        wordsList.extend([word])

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
//TODO multiple folders
