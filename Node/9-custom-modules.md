# Custom Modules

## Objectives
- Modules Advantages
- Exporting Single Item
- Exporting Multiple Items
- Real Usage
- Exercises

## Module Advantages
- The same advantages for custom modules on the front-end apply to node.
    - Eaiser to read
    - Easier to seperate concerns
    - Easier to collaborate
    - Easier to re-use code
- Your work is imported in the same way built in modules

## Exporting Single Item
- ```js
    /* modules/CoolFunction.js */

    const CoolFunction = ()=>{
        console.log('This is a cool Function')
    }

    //The whole export is a single function
    module.exports = CoolFunction
- ```js
    /* config.js */
    const config = {
        api:"somerandomkey",
        superSecret:"AnotherSecret"
    }

    module.exports = config
- ```js
    /* Another file */
    const config = require("./config");
    const CoolFunction = require("./modules/CoolFunction");
    
    CoolFunction()
    console.log(config)
## Exporting Multiple Items
- ```js
    /* /modules/functions.js */

    const function1 = ()=>{
        console.log('function1 is being called')
    }

    const function2 = ()=>{
        console.log('function2 is being called')
    }

    //Module exports is an object by default.
    //You can simply assign a key to a function
    module.exports.function1 = function1;
    module.exports.function2 = function2;
- ```js
    // This is functional the same as above
    module.exports = {function1,function2}
- ```js
    /* another file */
    const functions = require("/modules/functions")
    functions.function1()
    functions.function2()
- ```js
    //since it is an object you can destructure the content
    const {function1, function2} = require("./modules/functions")

## Real Usage
- ```js
    /* serveFavicon.js */
    //next is a callback
    const fs = require("fs");
    const serveFavicon = (req, res, next) =>{
        fs.readFile("./favicon.ico", (err,data) => {
            if (err) {
                res.writeHead(404);
                return res.end(JSON.stringify(err));
            }
            res.write(data)
            next(req,res)
        })
    }
- ```js
    /* setContent.js */

    module.exports.setContent = (page)=>{
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
        return content;
    }

- ```js
    /* app.js */
    const http = require("http")
    const serveFavicon = require("./serveFavicon")
    const setContent = require("./setContent")
    const port = 4433

    const server = http.createServer(req,res)=>{
        const url = new URL(req.headers.host+req.url)
       
        //handling favicon
        if(url.pathname == `${port}/favicon.ico`){
            return serveFavicon(req, res, (req,res)=>{
                console.log('Im gonna send this favicon')
                res.end()
            })
        }

        let page = url.searchParams.get("page")
        let content = setContent(page)
        res.write(content)
        res.end()
    }

    server.listen(port,()=>{
        console.log(`Running on Port ${port}`)
    })
## Exercises
1. Using the previous example turn everything that can be a module into a module.
    - Do not forget to make sure to include the needed arguments in the functions.
    - Even callbacks can be modules!