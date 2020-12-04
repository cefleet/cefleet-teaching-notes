# CSS Basics
## Objectives
- CSS format
- CSS selector types
- Adding CSS to Page
- exercises

## Terms
- *CSS* - `Cascading Style Sheet is the correct way to change the apperence of elements on a webpage. The cascading effect allows the developer to write less code for a greater impact`
- *Rule (or Ruleset)* - `In CSS a rule is a grouping of declarations that work together to modify the apperence of the selected item`
- *Selector* - `The part of the css Rule that determines which items will be affected by the rule`
- *Declaration* - `The property/value(s) pair in a css rule. There can be many declarations in a Rule`

## CSS Format
- ```css
    /* CSS comment*/

    /* Rule (or ruleset) breakdown */
    selector 						   
    { /* Declaration Block Start  */
        property1:value1; /* <- Declaration */
        property2:value2 value2a value2b; 	
    }/* Declaration Block End    */

## CSS Selector Types
- ```css
    /* Tag Selector */
    a {
        font-weight:bold;
        background:blue;
    }

    div {text-decoration:underline; color:rbg(10,20,30)}

    /* Class Selector */
    .content-item {
        color:#2df;
        background:#efefef;
    }
    .nav-link {
        text-decoration:underline;
    }
    /* ID selectors */
    #main-content {
        color:red
    }
    /* While you CAN style by id it is considered a very very bad practice. Ids are for selecting and identifying with javascript.*/

    /* Psudo Selector*/
    h1:hover {
        background-color:darkturquoise;
    }

    .nav-item:first-child {
        text-decoration:underline;
    }

## Adding css to page
- ```html
    <!-- using style tag -->
    <head>
        ...
        <style>
            div {
                font-size:16em;
            }
            a {
                text-decoration:none;
            }
        </style>
        ...
    </head>
- ```html
    <!-- linking a local file -->
    <link href="awesome-style.css" rel="stylesheet" type="text/css">
    <!--linking a file from the web -->
    <link href="https://cdn.sstatic.net/clc/styles/clc.min.css" rel="stylesheet" type="text/css">

## Exercises
1. Create a html page with a h1 element, a div with class main-content, and a footer with at least 2 links.
    - create a stylesheet called style.css and style the h1 element, the main content class, and the hover of the links.