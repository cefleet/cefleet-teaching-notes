# Variables

## Objectives
- var
- let
- const
- conventions
- Extras
- Exercises

## var
- ```javascript
  
    var a;//declare before assigning
    a = 10;//assigning a declared variable
    var b = 10; //declaring and assigning
    b = 23; //re-assign variable
    /* var allows you to re-declare a variable inside of a function. This can and will lead to bugs and should no longer be used */
## let
- ```js
    let = a;
    let a = "Something" //ending simi-colon not required...
    a = 1
    /* let does not allow you to redeclare inside of a function. It should be used in place of var*/
## const
- ```js
    const a = 'someintin'
    a = 'something esle'//error cannot re-assign const.

## Conventions
- ```js
    let camelCaseWin = 'Camel Case for the win'
## Extras
- ```js
    //declare multiple
    let a,b,c
    a = 1;
    b = 2;
    c = 3;

    //declaring and assigning multiple
    let e,f=10,g=12
    //e is undefined f is 10 g is 12

## Exercises
1. Write a program that declares 3 variables (dont use var).
    - assign those variable a number in any order.
2. Write a program that declares a const and gives it a value.
3. Write a program that declares and asigns a string to 3 variables on one line.

    