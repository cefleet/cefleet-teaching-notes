# Express Post Routes

## Objectives
- Postman Demo
- Making Post Routes
- Post body
- Recieving input from form
- Receiving json

## Terms 
- *POST* - `POST is a http method that unlike get methods, alows data to be sent in the 'body' of the request. Otherwise is it very similer to get`

## Postman Demo
> https://www.postman.com/

## Making Post Routes

- ```js
    ... // all of the basic setup

    //Post route
    app.post("/", (req,res)=>{
        console.log('A post has been accepted!');
        res.send({status:"Accepted"})
    });

    app.get("/", (req,res)=>{
        console.log("A get request has been recieved");
        res.send("<h1>Get Response</h1>")
    })

## Post Body
- ```js
    ...// all of the basic setup

    //These two lines convert form data
    //and json data to an object on req.body
    app.use(express.urlencoded({extended:true}))
    app.use(express.json())

    app.post("/", (req,res)=>{
        console.log('A post has been accepted!');

        //req.body is now ALWAYS an object.
        //it may be an empty object though.
        console.log(req.body);
        res.send(req.body)
    });

## Recieving input from form
- ```js
    ...// all the above stuff
    let emailList = []

    const htmlform = `
        <form method="POST" action="/addEmail">
            <input id="email" name="email" placeholder="Email" />
            <input id="age" name="age" placeholder="Age" />
            <button type="submit">Add Email</button>
        </form>
    `;

    app.get("/", (req,res)=>{
        res.send(htmlform)
    });

    app.post("/addEmail", (req,res)=>{
        const {email, age} = req.body;
        const id = Math.random();

        emailList.push({email, age, id})
        res.send({status:"sucess", id})
    })

    ...// rest of the stuff
> Using form submit the user's browser will be redirected to the response of the post. This is almost never the desired outcome.

- ```js
    app.post("/addEmail",(req,res)=>{
        const {email, age} = req.body;
        const id = Math.random();
        emailList.push({email, age, id})
        res.redirect(`/accepted/${id}`)
    })

    //redirected from addEmail
    app.get("/accepted/:id", (req,res)=>{
        //req and res are new objects
        const {id} = req.params;
        console.log(id, emailList)
        const {email} = emailList.find(email=>Number(email.id) === Number(id));
    
        res.send(`<div>Welcome ${email} Your id is ${id}</div> <a href="/">Go Home</a>`)
    });

## Recieving input from fetch
- ```js

    ...//additional

    const htmlform = `
        <form>
            <input id="email" name="email" placeholder="Email" />
            <input id="age" name="age" placeholder="Age" />
            <button type="submit">Add Email</button>
        </form>
        <div id="results"></div>
        <script src="script.js"></script>
    `;

    app.get("/", (req,res)=>{
        res.send(htmlform)
    });

    app.post("/addEmail",(req,res)=>{
        const {email, age} = req.body;
        const id = Math.random();
        const added = {email, age, id}
        emailList.push(added)
        res.send(added)
    })

- ```js
    /* script.js */
    const form = document.querySelector("form");

    const handleResponse = (response)=>{
        form.reset()
        let resDiv = document.querySelector("#results");
        resDiv.innerHTML = "";
        resDiv.append(`Welcome ${response.email} your id is ${response.id}`)
    }

    const handle

    form.addEventListener("submit", (evt)=>{
        const {target} = evt;
        evt.preventDefault();
        const formData = new FormData(target).entries()
        let body = {};
        for(let [key,value] of formData){
            body[key] = value
        }
        fetch("/addEmail", {
            method:"post",
            body:JSON.stringify(body),
            headers:{
                "Content-type":"application/json"
            }
        })
        .then(res=>res.json())
        .then(handleResponse)                
    })