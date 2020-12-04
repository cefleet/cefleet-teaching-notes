# HTTP module

## Objectives
- Demo
- Require Built in Module
- Create Server
- Start Server
- Send HTML Content
- Exercises

## Require Built in Modules

- ```js
    const http = require("http")
## Create Server
- ```js
    ...
    //We are not using req right now
    const server = http.createServer((req,res)=>{

        //set the status code to 200 before it sends
        res.statusCode = 200;

        //ends the response to the client
        //and sends the data in the argument
        res.end("Hello World")
    })
## Start Server
- ```js
    const http = require("http")
    const port = {XXXX}//any port number
    
    ... //the other content

    server.listen(port, ()=>{
        console.log(`Listening on port ${port}`)
    })
> server.listen does not close the program like most of our other porgrams written to this point. It will stay open until it is closed or crashes. 
## Send HTML Content

- ```js
    ...
    const htmlContent = `
        <!DOCTYPE html>
        <html>
            <head>
                <title>HTML Content from Node</title>
            </head>
            <body>
                <h1>This is a full HTML document!</h1>
                <ul>
                    <li>It's Valid!</li>
                    <li>It's From Node!</li>
                    <li>It's Just a String!</li>
                </ul>
                <script>
                    console.log("It's like magic")
                </script>
            </body>
        </html>
    `;
    const server = http.createServer((req,res)=>{
        res.statusCode = 200;
        res.end(htmlContent)
    })
    ...
## Exercises
1. Create a http server that will host a html document that has a title, a heading, and a list of your favorite foods.
    - Make the html document a valid html document.
    - Add a secret message in in the console using the script tag.