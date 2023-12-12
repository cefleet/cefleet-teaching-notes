# Spread Operator

## Objectives
- Spread syntax for arrays
- Spread syntax for objects
- Common usages

## Spread syntax for arrays
- ```js
    //syntax
    [...iteratableArray, value, value, moreIteratableArray]

    //spread at the begining
    let array1 = [1,2,3]
    let array2  = [...array1,4,5]
    console.log(array2)

    //spread anywhere
    let array3 = [...array1, 100,200, ...array2]

## spread syntax for objects
- ```js
    //syntax
    {...iteratableObject, key1:value1, key2:value2}

    let me = {firstName:"Clint",lastName:"Fleetwood", email:"clint@dclintfletwood.com"}

    let newPerson = {age:39, ...me}
    console.log(newPerson)

## Common Usages
- ```js
    //Math Functions
    let number = [10,20,30]
    console.log(Math.max(...numbers)) // spread the numbers as arguments

- ```js
    //updating objects (Very Important for React)
    let family = [
      {
          name:"clint",
          age:38
      },
      {
          name:"Anna",
          age:37
      },
      {
          name:"Olivia",
          age:11
      },
      {
          name:"Alle",
          age:9
      },
      {
          name:"Mark",
          age:7
      }
    ]
    const update = member=>({...member, surName:"Fleetwood"})
    let updatedFamily = family.map(update)
    //results
    console.log(updatedFamily)
    console.log(family)

- ```js
    // in place alternative to be more functional style

    //remove via filter
    let updated = [...family.filter(p=>p.name != 'Mark')] 

    //update a single item from the list as filtered
    let oliviaMarried = {
        name:"Olivia",
        surname:"Musk",
        age:24
    }

    //cool but it's at the end
    let updated = [...family.filter(p=>p.name != 'Olivia'), oliviaMarried]
    
    //using sort to keep the same order
    let updated = [...family.filter(p=>p.name != 'Olivia'), oliviaMarried]
    .sort((a,b)=>b.age - a.age)
    /* The Above Pattern you will see again...Take Time to learn it*/

> More Examples https://medium.com/coding-at-dawn/how-to-use-the-spread-operator-in-javascript-b9e4a8b06fab

## Exercises
1. Create an array of letters and create an array of numbers.
    - Using the spread operator create an array of the values of the letters first then the numbers.
    - Make another array with the numbers first.

2. Using the spread operator when possible do the following:
    - Create a new array adding at least 2 more cars.
    - From that new array return another array removing any cars made before 2018.
    - Create a new array with a 2010 ford focus added to the begining.
    - Create a new array of the cars sorted by date without changing the original cars array.
- ```js
    //use this array to start with
    const cars = [
        {
            make:"Chevy",
            model:"Corvette",
            year:2019
        },
        {
            make:"Ford",
            model:"Mustang",
            year:2018
        },
        {
            make:"Tesla",
            model:"Model 3",
            year:2020
        },
        {
            make:"GMC",
            model:"h2",
            year:2010
        }
    ]

