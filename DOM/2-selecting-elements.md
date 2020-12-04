# Selecting Elements

## Objectives
- getElementsByTagName
- getElementsByClassName
- getElementById
- querySelector
- querySelectorAll
- Exercises

## Terms 
- *DOM* - `Data Object Model, it is how javascript view the html page. Every element is part of an object that is a tree type structure and has parents and children.`
- *document object* - `In the dom the document object is the root / parent object of the entire document`
- *HTMLCollection* - `Is a list of elements that is returned from the document.getElementsByTagName/ClassName It cannot be looped over via forEach`
- *NodeList* - `Is similar to a HTMLCollection, but it can be looped through with forEach`

> This lesson will use the following html document.

- ```html
    <!DOCTYPE html>
    </html>
        <head> 
            <title>Test Selectors</title>
        </head>
        <body>
            <h1>This is a title</h1>
            <main>
                <div id="main-idea" class="concept">
                    Some Main idea
                </div>
                <p class="child-idea">
                    Child Idea 1
                </p>
                <p class="child-idea">
                    Child Idea 2
                </p>
                <p class="child-idea">
                    Child Idea 3
                </p>
            </main>
        </body>
    </html>

## getElementsByTagName
- ```js
    let paragraphs = document.getElementsByTagName("p")
    console.log(paragraphs)
    console.dir(paragraphs)
## getElementsByClassName
- ```js
    let paragraphs = document.getElementsByClassName("child-idea")
    console.log(paragraphs)
## getElementById
- ```js
    let main = document.getElementById("main-idea")
    console.log(main)
## querySelector
- ```js
    let heading = document.querySelector("h1") //tag
    console.log(heading)
    let main = document.querySelector("#main-idea") // id
    let idea = document.querySelector(".child-idea") // class
    let notHere = document.querySelector("#not-here") //not in document
> querySelector always gets one item or null if nothing is found. If there is more than one item it only finds the first item.

## querySelectorAll
- ```js
    let ideas = document.querySelectorAll(".child-idea")
    console.log(ideas)
    console.dir(ideas)
    ideas.forEach(function(idea){
        console.log(idea)
    })

## Exercises
1. Create a html document that has a header, a few divs with a sub-content class and, and some items with an id.
    - practice selecting different items using all of the techniques covered in this less.
    