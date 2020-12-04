# Radio Element

## Objectives
- Sytnax and Purpose
- Using radio Group
- checked
- Exercise

## Syntax and Purpose
- ```html
    <label for="myRadio">Radio</label>
    <input id="myRadio" type="radio">
> Radio buttons are not toggleable without javascript. Instead they are designed to select one item from a group.

## Using radio group
- ```html
    <div class="radio">
        <label for="cars">Cars
            <input id="cars" name="transport" value="cars" type="radio">
        </label>
        <label for="trains">Trains
            <input id="trains" name="transport" value="trains" type="radio">
        </label>
        <label for="planes">Planes
            <input id="planes" name="transport" value="planes" type="radio">
        </label>
    </div>
> With radio buttons, any radio element in the form that has the same name will switch from element to the one that is selected.
- ```html
    <!-- dont do this unless you have a specific reason to do so -->
    <div>
        <label for="cars">Cars
            <input id="cars" name="transport" value="cars" type="radio">
        </label>
    </div>
    <div>
        <input placeholder="Random stuff">
    </div>
    <label for="trains">Trains
        <input id="trains" name="transport" value="trains" type="radio">
    </label>
## Checked
- ```html
    <div class="radio">
        <label for="cars">Cars
            <input id="cars" checked name="transport" value="cars" type="radio">
        </label>
        <label for="trains">Trains
            <input id="trains" name="transport" value="trains" type="radio">
        </label>
        <label for="planes">Planes
            <input id="planes" name="transport" value="planes" type="radio">
        </label>
    </div>

- ```html
    <div class="radio">
        <label for="cars">Cars
            <input id="cars" checked name="transport" value="cars" type="radio">
        </label>
        <label for="trains">Trains
            <input id="trains" name="transport" value="trains" type="radio">
        </label>
        <label for="planes">Planes
            <input id="planes" checked name="transport" value="planes" type="radio">
        </label>
    </div>
    <!-- only the last one is actually checked -->
## Exercises
1. Create a radio group of at least 3 elements that will only have one element selectable at a time.
    - Using css, style the radio group.