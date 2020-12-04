# Modifying HTML content

## Objectives
- append
- innerText
- createTextNode
- innerHTML
- Exercises
> Using the html from the last lesson for this as well
## Append
- ```js
    let main = document.querySelector("main")
    let p = document.createElement("p")
    p.append("This is the text in the paragraph")

    let p2 = document.createElement("p")
    p2.append("Some additional text")

    main.append(p, p2)

## innerText
- ```js
    let header = document.querySelection("h1")
    header.innerText = "Look a new title"

    let mainIdea = document.querySelector("#main-idea")
    mainIdea.innerText = "<div>Im going to be trixy here</div>"
    //Not what I was expecting

## createTextNode
- ```js
    let mainIdea = document.querySelector("#main-idea")
    let text = document.createTextNode("This is the new text")
    //this is a node
    mainIdea.append(text)

## InnerHTML
- ```js
    let wholeBody = document.body //yup you can do this
    wholeBody.innerHTML = `
    <div>
        <h1>Wow I have changed everything</h1>
        <ul>
            <li>Yes</li>
            <li>I</li>
            <li>Did</li>
    </div>
    `;
    //this is normally not prefered but can be used sometimes.

## Exercises
- 1. Create an empty html document that has nothing in the body.
    - Using any of the techniques above (execpt for innerHTML)
    - add a h1 with content as a title.
    - add a main element.
    - add a section inside of the main element.
    - add a h2 element with a section title inside of the section element.
    - add a p element inside of the element with some text.
    - add a list of items in the main element.
