# Arrays

## Objectives
- Creating an Array
- Modifying an Array
- looping through array
- Exercises

## Creating an Array
- ```js
    //create empty array
    let myArr = [] 
- ```js
    //create array with items
    let myArr = ['a','b','c']

    //accessing via index
    console.log(myArr[1]) //b
## Modifying an Array
- ```js
    let myArr = ['a','b','c']

    //push adds to the end
    myArr.push('d')
    console.log(myArr)

    //removes the last item and returns the moved item
    let removed = myArr.pop()
    console.log(removed)
    console.log(myArr)

    //adds to the front of an array
    myArr.unshift('z')
    console.log(myArr)

    //add multiple
    myArr.unshift('x','y')
    console.log(myArr)

    //removes from the front
    let firstItem = myArr.shift()
    console.log(firstItem)
    console.log(myArr)

## Loop through Array

- ```js
    //old school way
    let myArr = ['a','b','c','d','e']
    for(let i = 0; i <  myArr.length; i++){
        console.log(myArr[i])
    }
    //while statment can be use similerly but is almost never used
- ```js
    //foreach
    let myArr = ['a','b','c','d','e']

    myArr.forEach(function(value){
        console.log(value)
        console.log(idx)
    })
    //all 3 arguments
    //current value, current idx, source array
    myArr.forEach(function(value,idx, arr){
        console.log(value, idx, arr)
    })

1. Create a list of letters at with at least 10 items.
    - print the 4th item.
    - concatinate the 6th and 3rd item and print the results.
    - add 4 more letters one at a time to the end of the array.
    - remove the first item of the array.
    - join all of the letters together and send the results to the console.
    - (bonus) sort the letters!
