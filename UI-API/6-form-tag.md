# Form Tag

## Objectives
- form element
- query string
- method
- action
- Exercises

## Terms
- *query string* - `Additional key value pairs in a url that javascript or a backend server can intepret and use to cause different functionality. The first key value starts with a ? and any additional starts with &`
- *Request Methods* - `The request methods are part of the http request that tell the server how to recieve the content.`

## Form Element
- ```html
    <form id="login">
        <!-- form elements -->
    </form>
- ```html
    <!-- button in form -->
    <form id="login">
        <!-- form elements -->
        <button> Login </button>
    </form>
- ```html
    <!-- submit button outside of form -->
    <form id="login">
        <!-- form elements -->
    </form>
    <button form="login">Login</button>
## query string
- ```html
    <form id="login">
        <input name="username" id="username" placeholder="username" />
        <input name="password" type="password" id="password" />
        <button form="login">Login</button>
    </form>
- ```bash
    #Enter information and press login and look at the url
    http://localhost:xxxx/folder/?username=cefleet&password=ImAmazing
> From the ? on is called the query string
- ```js
    /*script in tag or attached to the html doc*/

    console.log(window.location.search)//hard to parse this string

    let urlParams = new URLSearchParams(window.location.search);
    
    //loop through
    for(key of urlParams.keys()){
        console.log(key, urlParams.get(key))
    }
    //get specific
    let username = urlParams.get("username")

## Method
- ```html
    <form id="login" method="get" >
        ...items
    </form>
    <!-- get methods send request parameters in the url -->

    <form id="login" method="post" >
        ...items
    </form>
    <!-- post methods have request parameters sent in the body -->
## Action
- ```html
    <!-- action is a url -->
    <form id="login" action="login.html">
        ...
    </form>
> Action will almost always be sent to a resource on the server.
- ```html
    <!-- no action needed -->
    <form id="login">
        ...
    </form>
- ```js
    //form above
    let loginForm = document.querySelector("#login")
    loginForm.addEventListener("submit",(evt)=>{
        evt.preventDefault()
        console.log('I can do something else with the form!')
        console.log(evt.target.elements)//HTMLFormControlCollection
        //if it has a name or id you can do this
        console.log(evt.target.elements['login'])
        //also you can spread it into an array and loop it
        let results = [...evt.target.elements].filter(el=>el.name).map(el=>({name:el.name, value:el.value}))
        console.log(results)

    })

## Exercise
1. Create a form with 5 different elements of your choice.
    - Using javascript console.log the results from the request.
2. Recreate the form above using only javascript and DOM.(no writing html)
    - Have this new form be handled on the same page but never send results to the url.(listen for evt and prevent default)
    - Append the results of the form to the page in a seperate div when the form is submitted.
    - on submit reset the values of the form.