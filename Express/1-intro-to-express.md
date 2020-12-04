# Intro to Express

## Objectives
- Express Demo
- Install Express
- Setup Express
- Exercise

## Express Demo


## Install Express
- ```bash
    # From a terminal inside of a folder where your class exercises are contained
    mkdir practice-express
    cd practice-express
    npm init

    npm install express

## Setup Express
- ```js
    //app.js
    const http = require("http")
    const express = require("express")

    /* 
        The app object is where  most of the express "magic" happens.
    */
    const app = express();
    const port = 4432

    /* 
        The app object is passed as the options argument.
        http.createSever allows the options object to be omitted so we 
        have not used it before. Instead we are ommiting the callback.
    */
    const server = http.createServer(app)

    server.listen(port, ()=>console.log(`listening on port ${port}`))
In Browser goto: 
- http://localhost:4432
- http://localhost:4432/test
- http://localhost:4432/index.html

> Unlike http module, it does not simply send whatever the callback said. It makes choices for you if you do not specify routes.

## Exercise
1. Create a server using express.
    - Just get it running do not worry about routes now.