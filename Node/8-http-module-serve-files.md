# HTTP serve Files

## Objectives
- Serve Files as for server
- Exercises

## Serve Files as HTML
> Continueing from previous lesson We will just add serving different files by name and loading template files.
- ```js
    //Adding the ability to serve favicon.ico
    const http = require("http");
    const fs = require("fs")
    const port = 5454

    // server favicon function

    const server = http.createServer((req,res)=>{

        if(req.url == `/favicon.ico`){

            return fs.readFile("./favicon.ico", (err,data) => {
                if (err) {
                    res.writeHead(404);
                    return res.end(JSON.stringify(err));
                }
                res.writeHead(200);
                res.end(data) //IMPORTANT res.end is inside this callback.
            })
        }

        const url = new URL(req.headers.host+req.url)
        

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

    server.listen(port,()=>{
        console.log(`Running on Port ${port}`)
    })
- ```js
    //You can move the file to a function
    const http = require("http");
    const fs = require("fs")
    const port = 5454
    
    const serveFavicon = (res)=>{
        fs.readFile("./favicon.ico", (err,data) => {
            if (err) {
                res.writeHead(404);
                return res.end(JSON.stringify(err));
            }
            res.writeHead(200);
            res.end(data)
        })
    }

    const server = http.createServer((req,res)=>{
        if(req.url == `/favicon.ico`) return serveFavicon(res)
        const url = new URL(req.headers.host+req.url)
        
        ... // the rest is the same
> This is mostly a sample for a simple project where you want to be able to host a few files individually by name. If you are going to be hosting several files or a folder of images there are better solutions we will explore in the future.

## Exercises
1. Use the example from the last lesson and add the ability to host a favicon.
    - Create a CSS file. 
    - Host that css file using the same method as we did for the favicon and include it in the app at the beginning of the content.