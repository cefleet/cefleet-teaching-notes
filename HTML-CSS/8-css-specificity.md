# Specificity 

## Objectives
- Understand Inheritance
- Using Specificty
- Using combinators
- Exercises

## Terms
- *Inheritance* - `In css terms, Inheritance is how elements are styled when not directly selected. The inheritance order is parent -> User Angent (Browser default) -> Selected via selector`
- *Specificity* - `In CSS, specificity refers to how specific the selector is. If there is more than one selector that can impact an element, declerations from less specfic will be overwritten by more specific. Specificy goes in the order tag->class->psudo-class->id.`

## Understanding Inheritance
- ```html
        <style>
            /* Sets the font family */
            body {
                font-family: Arial, Helvetica, sans-serif;
            } 
            /* sets background for all 'a's */           
            a {
                text-decoration: none;
            }
            /* sets the font-famly for all 'div's */
            div {
                font-family: 'Courier New', Courier, monospace;
            }
            /* makes nav-links bold */
            .nav-link {
                font-weight:bold;
            }  
            /* makes active class silver and underline */  
            .active {
                background:silver;
            }
        </style>
        <h2>Star Wars Links</h2>
        <div id="navbar">
            <a href="#" class="nav-link">Yoda Facts</a>
            <a href="#" class="nav-link">Han Facts</a>
            <a href="#" class="nav-link active">Jar Jar Facts</a>
        </div>
## Using Specificity
- ```html
    <style>
    ...
    /* psudo class is more specific than class */
    .nav-link:first-child {
        background:green;
        text-decoration:underline;
    }
    ...
    </style>

## Using Combinators
- ```html
    <style>
    ...
    /* coma seperates individual selectors */
    h2, h3 {
        background:#efefef;
        border-bottom:3px solid;
    }
    /* spaces indicate parent -> child */
    .main-content .active {
        background:red;
        border: 1px solid #000;
    }
    /* no spaces means has both I all a elements with active class */
    a.active {
        color:green;
        font-weight:bold;
    }

    ...
    </style>
    <body>
    ...
        <div id="content">
            <h3>Mesa Jar Jar Binks</h3>
            <p class="active">mesa your humble servant!</p>
            <p>Yousa should follow me now, okeeday?</p>
        </div>
    </body>
> More details https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Selectors

## Exercises
1. Create a html document that is a todo list. It needs to have a h1, and a unordered list of things todo and two section elements with content inside describing the active todo item.
    - One of the items in the list needs to have active class.
    - At least one other item in the list needs to have a completed class.
    - One of the sections should have the class active.
    - Create a stylesheet or using the style tag to style the document.
    - All active items need to have a border, completed items need to be striked through, each list item needs to have a background color.
    - Every item on the page should be arial font-type execpt for the h1.
    - all of the sections need to be bold.