# Functions

## Objectives
- Declaring a function
- Anonymous functions
- Exercises

## Terms
- *Anonymous Function* - `A function that does not have a declared name. The function can be assigned a variable or used as an argument in a function.`

## Declaring a function
- ```js
    //Not much different from python
    function doSomething(){
        console.log('I can do something')
    }
    doSomething()
- ```js
    // return value
    function doAnotherThing(){
        return 'I did something else'
    }
    let randNum = doAnotherThing()
- ```js
    // arguments
    function someArgs(myNumber, anotherNumber){
        return myNumber / anotherNumber
    }
    someArgs(2,4)
- ```js
    //argument missmatch
    function foo(bar1,bar2,bar3){
        if(!bar3) bar3 = 0
        //bar3 = bar3 || 0
        return bar1 + bar2 + bar3
    }
    foo(1,2)//no error

## Anonymous functions
- ```js
    //assigning it to a variable    
    const myFunc = function(someArg){
        console.log('Im anonymous', someArg)
    }
    myFunc('Do it')
- ```js
    //anonymous as an argument
    function hasArgumentFunction(argFunction){
        console.log('I have a function as an arg')
        argFunction()
    }

    hasArgumentFunction(function(){
        console.log('Ok this is ok')
    })
- ```js
    //how they are different
    //This Works
    callBeforeDeclared()

    function callBeforeDeclared(){
        console.log('Do something')
    }
- ```js
    //This doesn't work
    anonCalled() //error

    let anonCalled = function(){
        console.log('You cannot do this')
    }
## Exercises
1. Write a function that accepts 3 arguments and returns the value of all the items added together.

2. Write a function that has an anonymous function as the first argument and a number as the second argument.
    - the anonymous function needs to console.log something.
    - Have the first function count from 0 to the number that the second argument is.
    - After it is done counting have it call the anonymous function.
    - call the function again with a different function as the argument.