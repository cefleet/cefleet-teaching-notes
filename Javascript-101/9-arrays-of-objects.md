# Array of Objects
## Objectives
- arrays of objects
- Exercises

## Array Of Objects
- ```js
    let people = [
        {
            name:"Clint",
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

    //single item
    console.log(people[0].name+' is '+people[0].age+' years old')

    // loop through array
    people.forEach(function(person){
        console.log(person.name+' is '+person.age+' years old')
    })

## Exercises
1. Make an array of ship objects (at least 3). Each ship needs a name, topSpeed, acceleration, and cargo capacity.
    - console.log the name and top speed of the 2nd ship.
    - loop through the array and print out every stat in a key:value style.
    - (Bonus) sort the array by the ship with the fastest speed and console log it out.