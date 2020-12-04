# Box Model

## Objectives
- Explain the Box Model
- Exercises

## Explain the Box Model
>https://hackernoon.com/hn-images/1*2jZwpWH9XO_QllhEpyGqMA.png

- ```css
    /* top, right, bottom, left */
    div {
        padding:10px, 20px, 2px, 6px;
    }

    /* top & bottom, left & right */
    span {
        margin: 1em,3em;
    }

    /* all */
    .random-selector {
        padding:50px;
        margin:10px;
    }

    /* size, style, color */
    div:hover {
        border: 4px double red;
    }

    /* height and width */
    a {
        width:50%;
        height:30px;
    }

> Padding contains the background margin is outside of the background. Think of margin seperating the elements while padding makes the element bigger.

## Exercises
1. Create a document that has 3 different div.
    - using style tag or adding a stylesheet do the following.
        - Give the padding and border of the first div 10px and a background of red and border of 1px.
        - Give the second div a padding of 10px at the top and bottom and padding of 100px left and right. Give it a red border of any style or size.
        - Give the 3rd div 4 largely different sizes for padding and a random background color. Also give it a top margin of 100px but all of the other margins 4px.