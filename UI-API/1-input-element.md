# Input Element

## Objectives
- Input Element
- Attributes
- Type
- Label
- Exercises

## Input Element
- ```html
    <input />
## Attributes
- ```html
    <input 
        id="username" 
        class="special" 
        name="user-name"
        placeholder="Username"
    >
    <!-- All form elements need a unique name -->
## Type
- ```html
    <input type="password" name="password">
    <input type="email">
    <input type="radio"><!-- Huh? -->
> the type attribute has the ability to completly change the behavior of the input element and will be used to make several of the other element types.

## Label
- ```html
    <label for="username">User Name</label>
     <input 
        id="username" 
        name="user-name"
    />
    <!-- clicking on the label is the same as clicking on the element if the for is a valid id -->
    <label> User Name
        <input id="username" name="user-name">
    <label>
    <!-- this is another way to assign a label to an element-->
## Exercises
1. Create an input element with a label that will get focus when you click on the lable.
2. Create an input element that used a placeholder to tell the user what is expected.