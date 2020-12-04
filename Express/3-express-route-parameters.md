#Express Route Parameters

## Objectives
- Create routes with Simple Parameters
- accessing parameters
- Create routes with complex Parameters
- Exercises

## Creating routes with simple parameters

- ```js
    ...
    //psudo code examples
    app.get("/post/:id", sendPostWithId)
    //urls
    /* /posts/12345 */

    app.get("/api/v1/todo/:status", sendAllTodosWithStatus)
    //url 
    /* /api/v1/todo/completed */

    /* BAD IDEA unless you have a valid reason */
    app.get("/:id", getAnythingWithId)  
    //normally you would not do above

## Accessing params
- ```js
    //samples
    db = {
        posts:[
            {
                id:"001", 
                title:"Good Things", content:"Lorium ipsum"
            },
            {
                id:"002", 
                title:"Bad Things", content:"FooBar"
            }
        ],
        people:[
            {
                id:"p001", 
                name:"Clint"
            },
            {
                id:"p002", 
                name:"Anna"
            }
        ]
    }

    app.get("/api/post/:id", (req,res)=>{
        const {id} = req.params;
        /* same as above, but above is better
            const id = req.params.id
        */
        const foundPost = db.posts.find(post=>post.id == id)
        res.send(foundPost)
    })

    app.get("/api/:type", (req,res)=>{
        const {type} = req.params;
        res.send(db[type])
    })
> Notice what type of item is in the res.send argument! This tells us that express will convert data to type needed if possible.
## Create Routes with Complex Params

- ```js
    app.get("/api/:type/:id", (req,res)=>{
        const {type,id} = req.params;
        if(!db.hasOwnProperty(type)) return res.send(null)
        foundItem = db[type].find(item=>item.id = id);
        res.send({type,foundItem})
        //same as above
        //res.send({type:type, foundItem:foundItem})
    })

## Exercises
> You can use the people.json file in the Express/Data folder from the notes for this exercise.

> You can import a json File by using the require function.

```js
let people = require("./data/people.json")
```
1. Create a node/express application that has a "/" route that will host a simple html document.
> All other routes will be prepended with "/api". /api/{whatever}
2. In the application above, add an "people" route that will send all of the people to the browser as json.
3. Create a route that will filter people based on gender.
4. Create a route that will find a person by their e-mail.
5. (Bonus) Serve a javascript file on a route called "/script.js" that will be be loaded in the document on the webpage.
    - In this file, fetch one of your routes and load the content into the webpage dynamically.
