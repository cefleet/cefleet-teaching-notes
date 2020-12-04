# Node Modules using FS

## Objectives
- How to load built in modules
- How to use node modules
- Exercises

## How to load built in modules
- ```js
    //This is psudo code ... there is not a module called module name
    const moduleName = require("moduleName")
> Node uses a module system called CommonJS. The 'require' function is used to load the module. 

> While Node can import modules in the es6 module way (like react) it has not become standard enough to try.
- ```js
    //real example
    const os = require("os")

    const http = require("http")

    const fs = require("fs")

    //many more
- ```js
    //works just like above. Just assign the name to something esle
    const o = require("os")
## How to use modules
> Link to documentation -> https://nodejs.org/api/
- ```js

    //the os module give info about the operating system that node is running on.
    const os = require("os")

    //Can be used inside of a function
    const getInfo = ()=>{
        let platform = os.platform()
        console.log(platform)
    
        let homeDir = os.homedir()
        console.log(homeDir)
    }

    console.log(os.hostname())
    getInfo() 
> All of the built in modules are an object that has several methods.

## Exercises
1. Create a node program that requires the os module.
    - Look through the os module documentation and print the following 3 pieces of information:
        - The amount of free memeory in the system. 
        - The network interfaces information.
        - The user information for the system.
    - Make a function that will retrieve all of the above pieces of information and return that information in an array.
    - Call that function and set the returned value to an variable and console.log the variable.