# Modifying HTML styles inline

## Objectives
- Change the look of an element
- Multiple styles at one time

## Terms
- *style* - `A style is what controls the apperence and position of an element`

>Styling elements this way is not the best practices and leads to problems. This is just to show how styling works.

## Change the look of an element
- ```html
    <div style="color:red">
        The content would be red
        <span> red also! </span>
    </div>

    <ul style="background:blue">
        <li style="font-weight:bold">Yes</li>
        <li style="text-decoration:underline">No</li>
        <li style="background:red">Maybe</li>
    </ul>
> The parent style will change the child elements as well unless the child has a style that changes it.

## multiple styles at once
- ```html
    <div style="color:red;font-weight:bold;">
        Bold and Red
    </div>

    <div style="cursor:pointer;color:purple;text-decoration:underline">
    Wow look at all dem styles.
    </div>

> Attribute references (look at the keyword index) https://developer.mozilla.org/en-US/docs/Web/CSS/Reference

## Exercises
1. No exercise. I do not want you to practice writing styles this way.