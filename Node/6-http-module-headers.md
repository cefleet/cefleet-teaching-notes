# HTTP Headers

## Objectives
- What are http headers
- Adding headers to response
- Content-Type Header
- Cors Headers
- Exercises

# What are http headers
> https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers

- HTTP headers are used to pass information to and from the client (browser) and the server.
- Much of the time headers are not really a large concern and are handled by the framework you are working with, but it is important to understand what is going on with them.
- The most common ones we deal with as developers are "Content-Type", "Authentication", "Access-Control-Allow-Origin". (We will go over Authentication later)

## Adding headers to response
- ```js
    const http = require("http")
    const server = http.createServer((req,res)=>{
        res.statusCode = 200;
        
        res.setHeader("X-Foo-Header", "RandomData/Random");
        res.setHeader("X-My-Header-Not-Real", "MoreRandom")
        res.end("Sent. Check the network!")
    })

    server.listen(5566,()=>{
        console.log(`Running on Port ${5566}`)
    })
- ```js
    ...
    const server = http.createServer((req,res)=>{
    //You can combine the status and set headers as an object with res.writeHead
        res.writeHead(200, {
            "X-Foo-Header":"RandomData/Random",
            "X-My-Header-Not-Real":"MoreRandom"
        })
        res.end("Sent. Check the network!")
    })
    ...
## Content-Type Header
- ```js
    const http = require("http")
    const server = http.createServer((req,res)=>{
        res.writeHead(200, {
            "Content-Type":"text/html"
        })
        //You can write to the response before sending/ending
        res.write("<div>This is a div</div>")
        res.end()
    })

    server.listen(5566,()=>{
        console.log(`Running on Port ${5566}`)
    })
- ```js
    ...
    //tells browser not to interpret html
    res.writeHead(200, {
        "Content-Type":"text/plain"
    })
    ...
- ```js
    //Send JSON data Explicitly
    const ships = [
        {
            name:"x-wing",
            type:"fighter"
        },
        {
            name:"tie-fighter",
            type:"fighter"
        },
        {
            name:"y-wing",
            type:"bomber"
        }
    ];
    ...
        res.writeHead(200, {
            "Content-Type":"application/json"
        })
        res.write(JSON.stringify(ships))
    ...
## Cors Headers
> When you attempt to retrieve data from a server that is not the same domain as the current domain (IE fetch to another server) You have to handle CORS issues.
- ```js
    // Node on one port
    const http = require("http")
    const server = http.createServer((req,res)=>{
       res.writeHead(200, {
            "Content-Type":"application/json"
        })
        res.write('["a","b","c"]')
        res.end()
    })
    server.listen(5566,()=>{
        console.log(`Running on Port ${5566}`)
    })
- ```html
    <!-- HTML content served on port 8888-->
    <!DOCTYPE html>
    <html lang="en">
    ...    
    <script>
        fetch("http://localhost:5566")
        .then(res=>res.json())
        .then(data=>console.log(data))
        .catch(err=>console.log(err))
    </script>
    </body>
    </html>
> Because of CORS specifications, this will produce a CORS error.
 The Server needs to be able to tell the browser that content is expected to be viewed on another domain.
- ```js
    res.writeHead(200, {
        "Content-Type":"application/json",
        "Access-Control-Allow-Origin":"http://localhost:8888"
        //I can access the site from localhost:8888, but nowwhere else
    })
> This is useful if you have a front-end app being served from a different port than the backend app or api
 - ```js
    res.writeHead(200, {
        "Content-Type":"application/json",
        "Access-Control-Allow-Origin":"*"
        //I can access the site from anywhere
    })
> This is useful of you want to make a public API.
## Exercises
1. Create a node application that has an array of objects of people with at least 3 people with the keys "firstName", "lastName", "email".
    - Using http, serve that object as json.
    - Set headers in such a way that you will not have cors issues if you access the content from anywhere.
    - (Bonus) make a very simple site, host it using serve on a port other than the api, and fetch from your newly created api.(you can use the script tag)
    - (Super Bonus) Using DOM functions (document.createElement()..etc) add a list of the people to your website.