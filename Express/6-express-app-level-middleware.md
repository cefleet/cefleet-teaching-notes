# App level middleware

## Objectives
- App level based middleware
- Middleware order
- Exercises

## App Level Middleware
- ```js
    const setMagicId = (req,res, next)=>{
        req.magicId = Math.random()
        console.log(req.magicId)
        next()
    }

    app.use(setMagicId)

    app.get("/", (req,res)=>{
        res.send(`
            You are at root and your magicId is:
            ${req.magicId}
        `)
    });

    app.get("/api", (req,res)=>{
        console.log(`
            You are at api but you have a magic id of : ${req.magicId}
        `)
    })
> app.use has an optional route that can be used before the function.
- ```js
    app.use("/api",setMagicId)

    ...

    app.get("/api/users", (req,res)=>{
        console.log(req.magicId)
        res.send("Some magic")
    })
> "/" would not get a magic number, but every route that starts with "/api" would.

## Middleware Order
- ```js
    app.use((req,res,next)=>{
        console.log('first')
        next()
    })

    const thirdMw = (req,res, next)=>{
        console.log("third")
        next()
    }

    app.use((req,res,next)=>{
        console.log("second")
        next()
    })

    app.get("/", thirdMw, (req,res)=>{
        res.send()
    })

- ```bash
    first
    second
    third
- The order goes like as such:
    1. application wide middleware first.
    2. In order that added was added using app.use
    3. order in which middleware is added in the route.

## Exercises
1. Using the example from last lesson.
    - Create middleware that will log the ip address from any request.(you may have to look this up)
    - Create middleware that will give a random id to any api request.
    - (bonus) make the id from above a uuid.