# Express GET routes

## Objectives
- Create default GET route
- res.send
- Create Additional Routes
- Example
- Exercises

## Terms 
- *GET Method* - `The get method is one of the methods that a http request can be sent to a server. The GET method is the most common and the default method for browsers and fetch`

- *Catch All* - `Catch All or '*' is a way to match anything`

## Create Default GET route
- ```js
    //app.js
    ... //previous example

    http.createServer(app)

    /*
        Routes are created using
        app.{method} function.
    */
    app.get("*", (req,res)=>{
        console.log('A request has been recieved at the root of the app!')

        res.writeHead(200)
        res.end("Hello Express!")
    })
    /*
        Routes can have any number of arguments, but the first is the pattern to match 
    */

    ...
In browser goto:
- http://localhost:4423
- http://localhost:4432/index.html
- http://localhost:4432/foo
> The catchall will match to every get request. This is much like using http.createServer without adding any conditional statements.

## Res.send
> res.send is like res.end, but it combines the besy guess at status code, default headers, and content, and res.end all in one.

- ```js
    //app.js

    ... 
    app.get("*", (req,res)=>{
        res.send("Hello Express")
    })
    ...

## Create Additional Routes
- ```js
    //app.js

    ...
    app.get("/", (req,res)=>{
        res.send('<div>You are at Home Page</div>')
    })

    app.get("*", (req,res)=>{
        //With express you use res.status
        res.status(404)
        res.send("<h1>You have wandered into the 404 zone</h1>")
    })
    ...
> Order of being declared matters. The first route that matches is the one that express uses. If we declared the "*" first then non of the other routes would ever be honored.
- ```js
    ...
    const server = http.createServer(app)

    app.get("/about", (req,res)=>{
        res.send("<div>This is about</div>")
    })
    ...

## Example
- ```js
    const http = require("http");
    const fs = require("fs");

    //sometimes you will see it look like this
    const app = require("express")()
    /*
       ^^ same as above
        const express = require("express")
        const app = require("app")
    */

    const sendFavicon = (req,res)=>{
        fs.readFile("./favicon.ico",(err,data)=>{
            if(err) return res.send(err);
            res.send(data)
        } )
    }

    const _404Content = `
    <!DOCTYPE html>
    <html> 
        <head> 
            <title>An Error you have found</title>
        </head>
        <body>
            <h1>404</h1>
            <blockquote>"An Error you have found" - Yoda
            </blockquote>
        </body>
    </html>
    `;
    const send404  = (req,res)=>{
        res.status(404);
        res.send(_404Content)
    }

    //favicon route
    app.get("/favicon.ico", sendFavicon)
    
    //home route
    app.get("/", (req,res)=>{
        res.send("<h1>You are Home</h1>")
    })

    //404 route
    app.get("*", send404)

    const server = http.createServer(app);

    server.listen(3322)

## Exercises
1. Create an express app with a home, about, and a contact route.
    - The home route needs to be accpeted on "/", and "/home" but give the same content.
    - Have a base valid html for all of the routes to use, but add a h1 with the title "home", "about", "contact" in the body for each route.
    - add a way to send 404 to catch any request that do not match a route.
    - (Bonus) Add additional content.
    