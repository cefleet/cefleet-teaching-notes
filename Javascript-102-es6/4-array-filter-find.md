# Array Filter and Find

## Objectives
- Use Filter
- filter map
- Use Find
- Exercises

## Use Filter
- ```js

    let numbers = [5,3,-10,3,-21,78,-54,-1,8]
    let positive = numbers.filter(num=>num > 0)
    console.log(positive)
> filter always returns an array and for each item if the function returns true, that item is added to the new array.
- ```js
    let numbers = [5,3,-10,3,-21,78,-54,-1,8]
    bigNumbers = numbers.filter(num=>num > 100)
    console.log(bigNumbers) //[] empty array

- ```js
    //common usage
    let ships = [
        {
            type:"freighter",
            name:"falcon"
        },
        {
            type:"fighter",
            name:"xwing"
        },
        {
            type:"bomber",
            name:"ywing"
        },
        {
            type:"fighter",
            name:"tie-fighter"
        }
    ]

    let fighters = ships.filter(ship=>ship.type == "fighter")
> filter is not designed to modify the item as it is added. It is designed to simply filter out items from the array.

## Filter -> Map
- ```js
    //ships from above
    let figherNames = ships.filter(ship=>ship.type == "fighter").map(ship=>ship.name)

    //sometimes look like this... but is the same thing
    let figherNames = ships
    .filter(ship=>ship.type == "fighter")
    .map(ship=>ship.name)

## Find
- ```js
    let numbers = ["a","b","c"]
    let a = numbers.find(num=>num == "a")
    let d = numbers.find(num=>num == "d")
    console.log(a,d)
> find ALWAYS returns 1 item or undefined

- ```js
    let numbers = [1,2,3,4,5,6,7,8]
    let more = numbers.find(num=>num > 5)
> If there is more than one item it only returns the first item.

1. Create an array of at least 6 todo items with each todo having keys, id, todo, status, deadline (timestamp).
    - Make at least one date before today.
    - Limit the status to "complete","in-progress","todo"
    - Using filter, create an array of only the complete items.
    - Using find, get the soonest todo item that has a status of "todo".
    - using filter get an array of all of the past due items.