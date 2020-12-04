# HTTP module req Object

## Objectives
- Read the req object
- Read the query string
- sending content based on query
- Exercises

## Read the req object
- ```js
    const http = require("http")

    const server = http.createServer((req,res)=>{
        //A Huge Object with a lot of information
        console.log(req)        
        res.end()
    })
    server.listen(5566,()=>{
        console.log(`Running on Port ${5566}`)
    })
> In a browser view http://localhost:5566 

> Generally we only need the headers and the url
- ```js
    ...
    console.log(req.headers,req.url)
    ...
## Read the query string
- ```js
    const http = require("http");

    const server = http.createServer((req,res)=>{

        //constructing the url object
        const url = new URL(req.headers.host+req.url) 

        //the queryString is found in the url.searchParams object
        let searchObj = url.searchParams;
        console.log(searchObj)

        //forEach is a bit different
        url.searchParams.forEach((value,name) =>{
            console.log(value,name))
        })

        //if we know what we are looking for we can use get
        let page = url.searchParams.get("page")
        console.log(page)
        res.end()
    })

    server.listen(5566,()=>{
        console.log(`Running on Port ${5566}`)
    })

> http://localhost:5566?page=contact&foo=bar&fooFoo=barBar

> The previous way was much eaiser and you will see it in many examples. url.parse(the_url_string). However it has been depreciated by node and should not be used.

## Sending content based on query 
- ```js
    ...
    const server = http.createServer((req,res)=>{
        
        res.setStatus = 200;

        //constructing the url object
        const url = new URL(req.headers.host+req.url) 

        //if we know what we are looking for we can use get

        let page = url.searchParams.get("page")
        let count = url.searchParams.get("count")

        let content = ""
        switch(page){
            case "about":
                content += `<h1>This is about!<h1>`;
                break;
            case "contact":
                content += `<h1>This is contact</h1>`;
                break;
            default:
                content += `<h1>This is Home</h1>`;
        }
        content += `<div>The Count is ${count || 0}</div>`

        res.write(content)
        res.end()
    })
    ...
> http://localhost:5566?page=contact&count=345

## Exercises
(Feel free to use the demo or example above as a guide)
1. Make a node application that will supply html content based on the page parameter in the query string using the http module.(This is almost exactly the last example from this lesson)
    - (bonus) Make the response send full valid html document without writing the top and bottom sections more than once. (IE make re-usable code)
    - (Extra Bonus) Add additional content based on any additional parameters in the quesy string.
