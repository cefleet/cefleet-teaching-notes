# Array Map

## Objectives
- Simple usage
- undefined issue
- Common Usage

## Simple Usage
- ```js
    let letters = ["a","b","c","d"]
    let letterPlus = letters.map(function(letter){
        return letter+letter
    })
    console.log(letters)
    console.log(letterPlus)

    //another example
    let letterObj = letters.map(function(letter,idx){
        return {
            name:letter,
            index:idx,
            letterIdx : letter+idx
        }
    })

    console.log(letterObj)

> Map will always produce an array of the same length as the source array.

## undefined issue
- ```js
    let numbers = [6,1,3,4,3,5,5,10]
    //function has a conditional return
    let increased = numbers.map(function((num, idx){
        if(num > numbers[idx-1]) return num;
    })
    console.log(increased)

> Maps put the return of the callback function in the spot of the index of the source array in the new array. If it doesn't have a return it puts in undefined.

## Common Usage
- ```js
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
            age:9
        }
    ]

    //returns just names
    let justNames = family.map(function(member){
        return member.name
    })

    //you will almost always use arrow functions 
    //yea! implicit returns
    let justNames1 = family.map(member=>member.name)
- ```js
    //you should not update the array in the map function
    let updated = family.map((member)=>{
        member.surName = "Fleetwood"
        return member
    })
    console.log(updated)
    // accidently updating objects this can lead to bugs
    console.log(family)
- ```js
    //better way ... create a new object
    let updated = family.map((member)=>{
        let newMember = {}
        for(key in member){
            newMember[key] = member[key]
        }
        newMember.surName = 'Fleetwood'
        return newMember
    })
    console.log(updated)
    console.log(family)//no change

1. Create an array of vehicle objects.
    - each vehicle object needs to have keys of name, speed, passangers.
    - using map, create a list of names of the vehicles.

1. Create an array of at least 6 todo items with each todo having keys, id, todo, status.
    - Limit the status to "complete","in-progress","todo"
    - Using map create a list of different status.
    - using map of those status, make a list of status objects that has keys status, and items.
- ```js
    //final array should look something like this
    [
        {
            status:"complete",
            items:["Pick up yard", "clean bathroom"]
        },
        {
            status:"in-progress",
            items:['brush teeth']
        },
        {
            status:"todo",
            items:["feed kids", "vote"]
        }
    ]
