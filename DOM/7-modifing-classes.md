# Modifying Classes

## Objectives
- adding classes
- removing classes
- toggling classes
- replace
- check for class
- Exercises

> Use the HTML / CSS below
- ```html
    <!DOCTYPE html>
    </html>
        <head> 
            <title>Test Selectors</title>
            <style>
                .hidden {
                    display:none;
                }
                .btn {
                    text-align:center;
                    padding:10px 20px;
                    border-radius:16px;
                    font-weight:bold;
                    border:1px solid #eeffee;
                    background:#eeffee;
                }

                .primary {
                    background:#6bc4ff;        
                }

                .highlighted {
                    background:#ddd;
                    padding:10px;
                }
            </style>
        </head>
        <body>
            <h1>This is a title</h1>
            <main>
                <div id="main-idea" class="highlighted">
                    Some Main idea
                    <span id="more-info">More Info</span>
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
            <footer>This is my footer.</footer>
        <script src="script.js"></script>
        </body>
    </html>


## Adding Classes
- ```js
    //add class
    let footer = document.querySelector("footer");
    footer.classList.add("highlighted")

    //add multiple clases
    let myButton = document.querySelector("#more-info")
    myButton.classList.add("btn", "primary")
## Removing Classes
- ```js
    //remove class
    let mainIdea = document.querySelector("#main-idea");
    mainIdea.classList.remove("highlighted")

    //remove class not present.. no error
    mainIdea.classList.remove("foo-bar")

## Toggle Classes
- ```js
    let myButton = document.querySelector("#more-info")
    let myInterval = setInterval(function(){
        myButton.classList.toggle("hidden")
    }, 300)
    //please do not have a blinking like this in your site.
## Replace Class
- ```js
    //Replace Class
    let footer = document.querySelector("footer");
    footer.classList.replace("highlighted","primary")

    //Replace Class non existant class does nothing
    footer.classList.replace("foo-bar", "primary")
## Check for Class
- ```js
    let res = footer.classList.contains("foo-bar")
    console.log(res)

## Exercises
1. Create a document with several different elements with ids, and tag types.
    - Add a stylesheet or add a style tag inside the head of the document.
    - Using querySelector and classList add, remove, toggle, replace various different classes.