# NPM

## Objectives
- npm init
- package.json
- adding package from npm
- node_modules and .gitignore
- clone, install
- Exercises

## Terms
- *NPM* - `Node package manager. Is the official repository of node packages that are not a core part of node.`

## NPM init
- ```bash
    # In a terminal in a new folder for a new project
    npm init
> npm init will make a folder ready to be used with npm.

## Package.json
> npm init creates a file called package.json.

> https://docs.npmjs.com/cli/v6/configuring-npm/package-json

### Make a start script
- ```json
    /* package.json */
    ...
    "scripts" {
        "test":"echo \"Error: no test specified\" && exit 1",
        "start":"node app.js"
    }
    ...
- ```js
    /* app.js */
    console.log("I can run with start!")
- ```bash
    #terminal
    npm start

### Make Another Script
- ```json
     ...
    "scripts" {
        "test":"echo \"Error: no test specified\" && exit 1",
        "start":"node app.js",
        "foo":"node bar.js"
    }
    ...
- ```js
    /* bar.js */
    console.log("I am the foo script. Yup")
- ```bash
    # terminal
    npm run foo
> The start script does not need 'run', other scripts do.

## Adding a package
- ```bash
    #terminal
    npm install uuid
> Look at package.json in dependencies

> Look at a new folder called "node_modules"

> https://www.npmjs.com/package/uuid

Most packages have a page that looks like the one above.
- ```js
    /* random.js */
    const uuid = require("uuid")

    console.log(uuid.v4())
- ```js
    /* random.js */
    //named destructuring
    const {v4:uuidv4} = require("uuid")
    console.log(uuidv4())

- ```js
    /* app.js */
    const uuid = require("uuid")
    const todos = []
    
    //add todo item to arra
    const addTODO = (todo)=>{
        //Creates the todo, add an id, converts any date format to date object
        todos.push({
            ...todo,
            dueDate:new Date(todo.dueDate),
            id:uuid.v4()
        })

    }

    addTODO({action:"Clean Car", dueDate:"11/30/2020"});
    addTODO({action:"Eat Turkey", dueDate:"11/26/2020"});
    console.log(todos)
## Node modules and .gitignore
> node_modules can be several hundered megabytes. If you are going to push a project to github YOU MUST add an entry for node_modules in a .gitignore file.

- ```bash
    # .gitignore file in folder with node_modules
    node_modules
    .DS_Store
    config.js

> Make SURE you are in the folder that you want to install the package in before you run npm install. Otherwise you will end up with random node_modules all over the place.

## clone, install 

> Sometimes you will need to clone another persons repository that is not in npm database. You will need to clone, then install it to load all of the dependencies. 
- ```bash
    # Terminal in a folder you want to install the project
    git clone https://github.com/DigitalCraftsStudents/Serve-With-Proxy

    cd Serve-With-Proxy

    npm install

    node run
    #You will get some errors because you need to modify config for this specific package.
> Npm install will install all of the items in the dependency section of the "package.json" file.

## Exercises
1. Building on the previous example. Send a random UUID to the user at the bottom of the page. Say something like "You secrete code is : XXXX-XXXX-XXXXXX-XXXX"
    - Using inline styles (and a package from npm) make the background and color for the h1 element a random color each time a user visits the site.
        - https://www.npmjs.com/package/randomcolor (or others)
    - making sure to use .gitignore so node_modules are not added, create a repository, initilize the repository and submit your project to git hub.
    - (hint) Without git init, npm install will install node_modules but not package.json
    - Have another student or dir try to clone and run your project.