# Creating and adding Elements

## Objectives
- create element
- add element to parent
- Exercises
> Using the html from the last lesson for this as well
## Create element
- ```js
    let content = document.createElement("div")
    let bigList = document.createElement("ul")
    let someText = document.createElement("p")
    //These items are created but not added yet.

## Add Element to parent
- ```js
    let main = document.querySelector("main")

    let section = document.createElement("section")
    let sectionHeader = document.createElement("h2")
    section.append(sectionHeader)
    //Appends the section header. It is still not part of the DOM
    //section.appendChild was the older way

    main.append(section) //adds to main. It is now in the document.

    //append can also just use a string


## Exercises
1. Create a html document that only has a single div in the body that has an id of "main-content".
    - Add a ul with 5 li child items in the ul.
    - (Bonus) use a for loop to add the child li items.