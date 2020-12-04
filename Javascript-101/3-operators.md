# Operators

## Objectives
- assignment
- comparison
- logical
- Exercises

## Assignment
- ```js
    let a = 10 //assigns
    a += 10 //adds-assigns
    a -= 2 //subtract-assigns
    a % 2 //modulus
    a++ //adds 1 assigns
    a-- //subtracts 1 assigns

## Comparison
- ```js
    let a = 10
    a == 11 //false
    a == 10 //true
    a == '10' // true ?
  
    a === 10 //true
    a === '10'//false

    a != 11 //true
    a != '10' // false
  
    a !== 10 //false
    a !== '10' //true

    a > 11 //false
    a > 10 //false
    a > 2 //true

    a < 10 //false
    a < 2 //false
    a < 11 //true

    a<=10 //true
    a <= '10' //true
    
    a >= 10 //true
    a >= '10' //false

    a == 'string type'//false no error
    a != 'any other type' //true no error
    a > 'something else' //false

## logical
- ```js
    let a = 10, b = 20, c = 30
    //And
    a == 10 && b == 20 // true
    a == 10 && b == 'not 20' //false
    a == 10 && b == 20 && c == 30 // true
    //Or
    a == 10 || b == 'not 20' // true
    a == 'not 10' || b == 'not 20'//false
    a != 'not 10' || b == 'not 20' //true

    //combining or and
    a == 10 || b == 20 && c == 'not 30' //true?
    /*  
        wrapping two expressions 
        in a parenthesis makes 
        it a single expression
    */
    (a == 10 || b == 20) && c == 'not 30' //false

    //Not
    !(a == 10) //false
    !(a == 11) // true
    !(a != 10) // true

1. Review these operators and test out several different combinations for yourself.