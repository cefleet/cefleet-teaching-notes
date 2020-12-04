# File System Module

## Objectives
- Importing File System (fs)
- Reading a file
- Reading a file without a callback 
- Exercises

## Import File System
- ```js
    //fs is the File System 
    const fs = require("fs")
## Reading a file
- ```js
    //usage PSUDO Code
    fs.readFile("/path/to/file", callbackFn)
> Node is built on callbacks and asynchronous execution. This prevents the whole system being "blocked".
- ```js
    //real example
    const fs = require("fs")

    fs.readFile("test.txt",(err, data)=>{
        if(err) throw err;
        console.log(data)
        //<Buffer xx xx xx xx ...> WTF?
    })     
    //this example is literaly from the docs
> we haven't covered "throw". This code basically says "If there is an error reading the file, let the system know and shout out the error"

> The default behavior is for the file to set data to a buffer. Just think if a buffer as the way the computer reads the data. We cannot read a buffer most of the time so we need decode the buffer.
- ```js
    const fs = require("fs")
    //assumes there is a test.txt file in the same folder as this file.
    fs.readFile("test.txt", "utf8",(err, data)=>{
        if(err) throw err;
        console.log(data)
    })
>If the second argument is a string, it is expecting it to be a type of encoding. (for us its 'utf8').

> Don't worry too much about it. Just whenver you need to read a file, set the second argument as 'utf8' and you will be fine.
- ```js
    //assums there is a file that has valid json
    fs.readFile("data.json",'utf8',(err, data)=>{
        if(err) throw err;
        console.log(JSON.parse(data))
    })

## Reading a file without a callback
>!!! This is a blocking piece of code. Should not be used execpt for loading initial data as the program launches.
- ```js
    let data = fs.readFileSync("data.json",'utf8')
    let dataArr = JSON.parse(data)
    //Do stuff with dataArr
## Exercises
1. Create a node app that will read the contents of a text file and console.log the content.
2. Create a json file called "data.json" with the following content.
    - ```js
        [{"name":"Clint", "age":29}, {"name":"Anna", "age":27}, {"name":"Olivia", "age":11}]
     - For each person console.log("{name} is {age} years old!" where name and age are the keys name and age respectivly. 