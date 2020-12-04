# Arrow Functions

## Objectives
- Creating an arrow function
- Arrow Functions condensed
- Arrow Functions as an argument/callback
- Exercises

## Terms
- *implicit return* - `In javascript implicit return is when a value is returned from a function or operation without using the return keyword.`

## Creating an Arrow Function
- ```js
    //written different
    const myArrowFunc = (foo)=>{
        console.log(foo)
    }
    //called the same way
    myArrowFunc('got some data for ya')
- ```js
    //returning and arguments
    const returnStuff = (arg)=>{
        return 'stuff'+arg
    }
    console.log(returnStuff('something'))
## Arrow Function condensend
- ```js
    //single argument can be used with out ()
    const onlyOneArg = someArg => {
        console.log(someArg)
    }
    onlyOneArg('yup it works')
- ```js
    //implicit return
    const simple = ()=>'This string is returned' 
    console.log(simple())

    //more useful example
    const xTimesX = x=>x*x //implicit return
    let res = xTimesX(12)
    console.log(res)
## Arrow functions as an argument/callback

- ```js
    const doSomething = function(callback){
        console.log('I did something')
        callback()
    }

    doSomething(()=>{
        console.log('The function is finished and now it is my turn')
    })

    //condensed callback
    let myArr = ['a','b','c','d']
    myArr.forEach((letter,idx)=>console.log(letter, idx))
    
> https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Arrow_functions

## Exercises
1. Write an arrow function that accepts a number as an argument and multiplys that number by itself and returns the value.
2. Write an arrow function that has 2 arguments. Add the two arguments and console.log the results.
3. Write an array of names.
    - using forEach loop through the array and have the callbakc function be an arrow function that prints will print the index +1 and then the name.
- ```js
    //results
    let names = ["clint", "anna", "olivia"]
    ...//your code
    
    //results
    1. clint
    2. anna
    3. olival
