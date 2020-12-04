# Express Serve Files

## Objectives
- Serve files from a directory
- Using path
- Serve from multiple directories
- Modify a folder's url
- Including other routes
- Exercises

## Serve files from a directory
- ```js
    const express = require("express");
    const http = require("http");
    const app = express();
    const port = 4455;
  
    //using express built in middleware
    app.use(express.static("public"));

    const server = http.createServer(app)

    server.listen(port)

- ```html
    <!-- /public/index.html -->
    <!DOCTYPE html>
    <html>
        <head>
            <title>I am a html page</title>
            <link href="style.css" rel="stylesheet">
        </head>
        <body>
            <h1>Express is neat!</h1>
            <ul>
                <li>Routes</li>
                <li>Middleware</li>
                <li>Serve files</li>
                <li>Much More...</li>
            </ul>
            <script src="script.js"></script>
        </body>
    </html>
> script.js and style.css are in the "/public/" folder and have content.

> http://localhost:4455

> This is functionally the same as the serve global npm package.

# Using path
> Sometimes the path to the folder isn't directly a child of the folder the app was launched in. When that is the case you need to use path.

- ```js
    ... //
    const path = require("path")
    const port = 4455;

    app.use(express.static(path.join(__dirname, 'public')))
    ...//all the other stuff

## Serving from Multiple Directories

- ```js
    ...

    app.use(express.static(path.join(__dirname, 'scripts')))
    app.use(express.static(path.join(__dirname, 'html')))

    ...
> If a file's location is "/scripts/main.js" then you would access it at "http://localhost:4455/main.js"

> If a files location was "/html/about.html" you would access it at "http://localhost:4455/about.html"

> All of the files are served as if they are at root.

## Modify a folder's URL
> Remember that express.static is middleware and middleware allows for an optional route! It can be routed just like other routes.

- ```js
    app.use("/static",express.static(path.join(__dirname, '/public')))
> If a file's location "/public/index.html" the url would be "http://localhost:4422/static/index.html

## Including other routes
- ```js
    ...

    app.use("/static",express.static(path.join(__dirname, '/public')))

    app.get("/api", (req,res)=>{
        res.send({name:"api", version:'10'})
    })


## Exercises
1. Create an express app that hosts a script.js, style.css and index.html file from a server.
    - Have a valid index.html with some content that links the stylesheet and loads the script.
    - The index.html also needs to have an empty div with an id of "from-server".
    - Create a route for "api" and have it serve some random object or array.
    - Using fetch load the data from api into the "from-server" div.
    - (Bonus) Use DOM manipulation instead of innerHTML and make the content an unordered list in the page.