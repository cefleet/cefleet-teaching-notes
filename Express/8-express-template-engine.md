# Express Template Engine

## Objectives
- Template Demo
- Setup Templates
- Render Templates
- Exercise

## Setup Templates
- ```bash
    # In Terminal
    npm install express-es6-template-engine
- ```js
    const http = require('http');

    const port = 5432;

    const express = require('express');
    const app = express();

    const es6Renderer = require('express-es6-template-engine');

    //This declares that the 'es6Renderer' function handles *.html files.
    app.engine('html', es6Renderer);

    //This sets the place to find views as the template folder.
    app.set('views', 'templates');
    //This tells app to combine the above two items when using res.render
    app.set('view engine', 'html');

    const server = http.createServer(app);

    app.get("/", (req,res)=>{
        /*
        With templates we use res.render instead of res.send.
        This tells the engine to find main.html in the templates folder and render it.
        */
        res.render("main")
    })

    server.listen(port)
> Folder /templates/ has a file named main.html

## Exercise
1. Create an express app that has 3 html files. Home, About, Contact.
    - Have these html files be used by the template engine.
    - Each html file needs to have a link to all the other pages.
    - Using routes, when a browser goes to any of the urls the pages will render based on the url.
        - example: http://localhost:XXXX/about will render the "about.html" page.
    - (Bonus) - Using params and a "/pages" route, have only one route for all of the html pages.
