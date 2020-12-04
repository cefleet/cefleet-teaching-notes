# Conditions

## Objectives
- if, else, else if
- ternary
- single line
- switch
- Exercises

## if, else, else if
- ```js
    let a = 10, b = 20, c = 30
    //if statement
    if(a == 10){
        console.log('a is 10')//not print
    }
    //if else statement
    if(a == 16){
        console.log('a is 16')
    } else {
        console.log('a is not 16')
    }

    //if else with multiple conditions
    if(a == 10 && b == 10){
        console.log('both statements are true')
    } else {
        console.log('at least one of the statements is not true')
    }

    //if else if else
    if(a < 10){
        console.log('a is less than 10')
    } else if (a < 20) {
        console.log('a is less than 20')
    } else {
        console.log('a is larger than 20')
    }

    //nested if statements (please dont..like this)
    if(a == 10){
        if(b == 20){
            if(c == 30){
                console.log('nesting to the third!')
            }
        }
    }

    //nested if statements with nested else
    if(a == 10){
        if(b == 20){
            if(c != 30){
                console.log('I new c wasnt 30')
            } else {
                console.log('c must be 30')
            }
        }
    }

## Ternary
- ```js
    let a = 10

    a == 10 ? 'yes!' : 'no' //yes!
    
    //assign from the expression
    let b = a == 20 ? 'yes!' : 'no'
    console.log(b) //no

## Single Line
- ```js
    let i = 10;
    //if you need to only do one thing this is 
    //is an elegant solution
    if(i > 5) console.log('do single thing')

## Switch    

- ```js
    let a = 10

    switch (a) {
        case 20:
            console.log('a is 20')
            break;
        case 15:
            console.log('a is 15')
            break;
        case 10:
            console.log('a is 10')
            break;
        default:
            console.log("I really don't know")
    }

    let number = 12 //random input from user
    let output = null
    switch(true){ //doing this compares to see if each expression is true
        case (number < 3):
            output = 'low'
            break;
        case (number < 7):
            output = 'med'
            break;
        case (number < 14):
            output = 'high'
            break;
        default:
            output = 'very high'
    }
    console.log(output)

## Exercise
1. Write a program that will declare a variable named "value". 
    - Have an if, if else, else statement that compares that value.
2. using ternary.
    - compare if one number is greater than another. 
    - set the value of a variable named 'result' to 'higher' if the first number is higher and 'lower' if the first number is lower.
3. Using switch.
    - set a variable named  'temp' and give it a value between -20 & 110.
    - Have cases for sub 0, 30, 50, 75, 80, 90, and above.
    - Have a hex color for each level going from blue to red.
    - print out the color that represents the range.
```js
    /* results */
    let temp = 50;
    let color = null;
    ... //your code
    console.log(color) //#cdff74 (kinda light green)