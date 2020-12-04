# Modifying Styles

## Objectives
- Setting the whole style attribute
- Modifying a single style attribute
- Exercises
> Using same document as before
## Setting the whole style attribute
- ```js
    //set the style attribute
    let header = document.querySelector("h1")
    header.style = "border-bottom:1px solid;"
- ```js
    //changing several styles
    let header = document.querySelector("h1")
    header.style = "border-bottom:1px solid; text-align:right; color:#446699;"
- ```js
    //seting several different items
    let ideas = document.querySelectorAll(".child-idea")
    let styleString = "background:red;font-size:2em;font-weight:bold;"
    ideas.forEach(function(idea, idx){
        idea.style = styleString
    })
- ```js
    //writting the style attribute completely overides any styles written inline
    let header = document.querySelector("h1")
    header.style = "border-bottom:1px solid;"

    header.style = "color:green" //no underline

# Modifying a single style attribute
- ```js
    let header = document.querySelector("h1")
    header.style.color = 'green'
    header.style.border = "1px solid"
    //only overwites the attributes it changes
- ```js
    //how to modify '-' words?
    let header = document.querySelector("h1")
    header.style.font-size = "4em" //ERROR

    //correct
    header.style.fontSize = "4em"
    header.style.borderBottom = "2px dashed"
    header.style.fontFamily = "sans-serif"

## Exercises
1. Create a document that has a h1, a ul with 3 items, and a p element.
    - Add content to all of the items via dom manipulation.
    - Add styles to all of the items using the techniques shown above.