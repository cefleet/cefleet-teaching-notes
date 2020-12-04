# Select Element

## Objectives
- Select
- Option
- optgroup
- Exercises

## Select
- ```html
    <label for="favorite-food">Favorite Food</label>
    <select name="favorite-food" id="favorite-food"></select>
## Option
- ```html
    <label for="favorite-food">Favorite Food</label>
    <select name="favorite-food" id="favorite-food">
        <option value="pizza">Pizza (Ninja Turtles)</option>
        <option value="mushrooms">Shrooms (Mario)</option>
        <option value="doughnut"> Doughnuts (Homer)</option>
    </select>
- ```html
    <!-- have null value for initial -->
    <label for="favorite-food">Favorite Food</label>
    <select name="favorite-food" id="favorite-food">
        <option value="">---Please Select a Food ---</option>
        <option value="pizza">Pizza (Ninja Turtles)</option>
        <!-- Selected will be the default -->
        <option selected value="mushrooms">Shrooms (Mario)</option>
        <option value="doughnut"> Doughnuts (Homer)</option>
    </select>

## optgroup
- ```html
    <label for="favorite-food">Favorite Food</label>
    <select name="favorite-food" id="favorite-food">
        <option value="">---Please Select a Food ---</option>
        <optgroup label="Italian">
            <option value="pizza">Pizza (Ninja Turtles)</option>
            <!-- Selected will be the default -->
            <option selected value="mushrooms">Shrooms (Mario)</option>
        </optgroup>
        <optgroup label="Sweets">
            <option value="doughnut"> Doughnuts (Homer)</option>
        </optgroup>
    </select>

## Exercises
1. Create a select element that has at least 3 diffrent options.
2. Add 2 more elements to the dropdown using javascript.