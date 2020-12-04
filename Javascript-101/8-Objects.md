# Other Data Types
## Objectives
- Creating Objects
- Accessing
- Modifying values
- Looping through an object
- Exercises


## Creating Objects
- ```js
    //empty object
    let myObj = {}

    //object with values
    let newObject = {
        name:"Clint",
        age:38,
        tall:false
    }

    //using new
    let another = new Object()
    console.log(another)

## Accessing Values
- ```js
    let aboutMe = {
        name:"Clint",
        age:38,
        tall:false
    }

    //like python
    console.log(aboutMe["name"])
    //keys must be strings ... technically
    // so they can be accessed via dot notation.
    console.log(aboutMe.name)
## Modifying values
- ```js
    ...//from above
    //changing a key
    aboutMe.name = 'Clint F'
    console.log(aboutMe)

    //adding new key
    aboutMe.gender = 'Male'
    console.log(aboutMe)

    //removeing a key
    delete aboutMe.tall
    console.log(aboutMe)
## Looping through an object
- ```js
    let aboutMe = {
        name:"Clint",
        age:38,
        tall:false
    }

    //for in loop
    for(attrib in aboutMe){
        console.log(attrib)
        console.log(aboutMe[attrib])
    }

    //technically this is better because of some quirkiness of js inheritance situations
    for(attrib in aboutMe){
        if(!aboutMe.hasOwnProperty(attrib)) continue;
        console.log(attrib)
        console.log(aboutMe[attrib])
    }

> Better ways to loop through objects will be discussed in es6

## Exercises
1. Create an object called 'spaceship'. 
    - give it the following keys with whatever values seems reasonable to you. speed,acceleration, passangers, fuel.
2. Using the spaceship object above add a payload key after the object has been created. (just give it a number)
3. Using the same object above, lower the amount of fuel by 1/3.
4. loop through the object and give a message to the console like the one below for every property in the object.
- ```js
     passangers : 100
     ...