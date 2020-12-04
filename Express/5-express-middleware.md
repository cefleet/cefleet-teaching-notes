# Express Middleware

## Objectives
- What is middleware
- route level middleware
- Middleware can send the response
- Exercises

## What is middleware
 - Besides routes, middleware is the main attraction to express. 
 - It is essentially just any code that can be executed between a request comming in and the response being sent out.

- ```js
    //sample middleware function
    const sendAllData = (req,res)=>{
        res.send(data)
    }
> What does the above look like? Any route callback IS middleware in express. It just happens to be the final middleware so it doesn't need / have the final argument.

- ```js
    //middleware with the next function
    const timeLogger = (req,res, next)=>{
        let requestTime = new Date()
        console.log("A request came in at "+requestTime)

        req.reqestTime = requestTime
        next()
    }
> If the middleware doesn't send/end the request then it needs to call the next function.

> The next function is set as an argument by express but delcared/created by the developer. Example below.

## Route Level Middleware
- ```js
    const timeLogger = (req,res, next)=>{
        let requestTime = new Date()
        console.log("A request came in at "+requestTime)

        req.requestTime = requestTime
        next()
    }

    //Middleware is just any function after the route
    app.get("/", timeLogger, (req,res)=>{
        console.log(req.requestTime)
        res.send(data)
    })
- ```js
    //You can have multiple middleware and declare middleware on the fly
    const addOneToCount = (req,res,next)=>{
        req.count = req.count ? req.count+1 : 1;
        next()
    }

    app.get("/", 
        (req,res,next)=>{
            console.log("I am number 1")
            next()
        },
        addOneToCount,
        addOneToCount,
        addOneToCount,
        (req,res)=>{
            console.log(`addOneToCount was called : ${req.count} times`)
            res.json(req.count) //using res.json because sending a number with res.send errors
        }
    )


## Middleware can send the response
- ```js
    const checkId = (req,res,next)=>{
        if(req.params.id.length <= 4) return res.send("ID are at least 5 long.")
        next()
    }

    app.get("/api/people/:id", checkId, (req,res)=>{
        console.log('Id is long enough')
        res.send("I can send the person here")
    })


## Exercises
- ```js
    {people:[], places:[], things:[]}
    //you can use the above object.
1. Create an app that has 3 routes. "/", "/api", "/api/:type".
    - Create middleware for the "/" route that will console.log the current time.
    - Create middleware for the "/api/:type" that will check and see if the type is in the object. If it is not end the request. Otherwise continue on.