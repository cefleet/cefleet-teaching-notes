# Express Query String

## Objectives
- Access Query String
- Use Query string
- Use Query String with routes
- Exercises

## Access Query String
- ```js

    ... // all of the other things to setup express
    app.get("/", (req,res)=>{
        console.log(req.query);
    })
    ...
Results with URLs:
- http://localhost:XXXX - "{}"
- http://localhost:XXXX?apiid=randomid - "{ apiid: 'randomid' }"
- http://localhost:XXXX?name=clint&age=39 - "{ name: 'clint', age: '39' }"

## Use Query String
- ```js
    db = {
        posts:[
            {
                id:"001", 
                title:"Good Things", 
                content:"Lorium ipsum"
            },
            {
                id:"002", 
                title:"Bad Things", 
                content:"FooBar"
            }
        ],
        people:[
            {
                id:"p001", 
                name:"Clint",
                age:39
            },
            {
                id:"p002", 
                name:"Anna",
                age:37
            }
        ]
    }
    
    app.get("/api", (req,res)=>{
        //looks for type && ignores all others
        if(req.query.type) return res.send(db[req.query.type])

        //if no type just send the whole db
        res.send(db)
    })
- ```js
    //more refined but kinda ugly
    app.get("/api", (req,res)=>{
        if(req.query.type == "people") {
            if(req.query.name){
                return res.send(db.people.find(p=>p.name == req.query.name))
            }
            return res.send(db.people)
        } else if(req.query.type == "posts"){
            if(req.query.id){
                return res.send(db.posts.find(p=>p.id == req.query.id))
            }
            return res.send(db.posts)
        }
        res.send(db)
    })

## Use Query String with Routes

- ```js
    //looks better and works better
    app.get("/api/people", (req,res)=>{
        const {name, id} = req.query
        if(id) return res.send(db.people.find(p=>p.id == id));
        if(name) return res.send(db.people.find(p=>p.name == name));
        res.send(db.people)
    })

    app.get("/api/posts", (req,res)=>{
        const { id} = req.query        
        if(id) return res.send(db.posts.find(p=>p.id == id));
        res.send(db.posts)
    })

## Exercises
1. Create an object of two arrays. One is an array of cars where each car has a year, make, and model. And the other array is of drivers where each driver has a name, age, wrecks.
- ```js
    //sample
    db = {
        cars:[
            {year:2020, make:"Ford", model:"Mustang"},
            ...//additional
        ],
        drivers:[
            {age:39, name:"Clint", wrecks:20},
            ...//additional
        ]
    }
2. Using app.get params and query strings, make an api than can do the following:
    - Get all cars made before a given year
    - Get all cars made after a given year
    - Get all cars made during a year
    - Get all cars by their make
    - Get a driver by their name
    - Get all drivers over or at a specific age
    - Get all drivers under or at a specific age
    - Get all drivers based on wrecks
    - (Bonus) make several combinations as efficently written as you can.
    - (Bonus) Make a route that will Get a random car and driver and pair them together
