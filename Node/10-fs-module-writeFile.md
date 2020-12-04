# FS Module Write 

## Objectives
- Write content to a file
- Adding content to a file
- Exercises
## Write Content to a file
- ```js
    const fs = require("fs")

    fs.writeFile("file.txt", "Hello Node!", 'utf8', (err)=>{
        if (err) throw err;
        console.log('The file has been saved')
    })
> !! It is important to know that this is writting to the location that node is running from. Even if the request comes from an outside source such as a browser.
- ```js
    const fs = require("fs")

    let ships = [
        {
            type:"Freighter",
            speed:"medium",
            cargo:"large",
            payload:"low"
        },{
            type:"Fighter",
            speed:"fast",
            cargo:"none",
            payload:"medium"
        },{
            type:"Bomber",
            speed:"slow",
            cargo:"none",
            payload:"high"
        }
    ]

    fs.writeFile("ship-data.json", JSON.stringify(ships), 'utf8', (err)=>{
        if (err) throw err;
        console.log("The JSON file has been written")
    })
> 'fs.writeFile' will always overwrites the entire document.

## Adding content to a file
> There is a fs.appendFile method. It has limited used for our purposes so it will not be discused.

- ```js
    //we already have ship-data.json
    let ships = JSON.parse(fs.readFileSync("ship-data.json" ))

    const addShip = (newShip)=>{
        ships.push(newShip)
        fs.writeFile(
            "ship-data.json", 
            JSON.stringify(newShip),
            (err)=>{
                if (err) throw err;
                console.log("New Ship data saved")
            }
        )
    }

    addShip({type:"speeder",speed:"Fast", cargo:"none", payload:"none"})

## Exercises
1. Create an node program that will write a paragraph to a file named paragraph.txt
2. Create a node program that will convert an array of at least 3 objects (cars) that each have the keys name, speed, year to a json string and write it to a file called "cars.json".
    - later in the program add two more cars to the file.
3. (Bonus individual or as a class) Using the previous exercise, create a visit logger that will save the clients ip address (req.connection.remoteAddress) to an object along with a timestamp of when the last time the client visited the site.
    - Save this object to a json file whenever a client visits.
    - Add a statement like "You visited this site MM/DD/YYYY" at the end of the response data.