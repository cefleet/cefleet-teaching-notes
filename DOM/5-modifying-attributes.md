# Modifying Attributes

## Objectives
- Adding /modifying Attributes
- Using setAttribute
- Exercises

> Using the same html as before
## Adding/Modifying Attributes
- ```js
    let main = document.querySelector("main")
    main.id = "main-item"
    console.log(main)
    
    let a = document.createElement("a")
    a.innerText = "This is an awesome link"
    a.href = "http://www.google.com"
    main.append(a)
- ```js
    //Set Attribute
    let picture = document.createElement("img")
    picture.setAttribute("src","https://www.imagesource.com/wp-content/uploads/2019/06/Rio.jpg")
    picture.setAttribute("alt", "Pretty picture of rio")
    main.append(picture)
## Exercises
1. Create a html document that has an empty body.
    - Create an array of objects with keys url, text, id and values that match.
    - ```js
        //something like
        let myList = [{url:"http://www.google.com", id:"google-link", text:"Goto Google yo!"} ...etc]
    - Loop through the array and make an unordered list of links.
    

