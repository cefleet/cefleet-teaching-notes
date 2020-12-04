# Checkbox

## Objectives
- Checkbox syntax and purpose
- checked
- value
- Multiple items
- Exercises

## Checkbox syntax and purpose
- ```html
    <input type="checkbox" id="agree" name="agree">
    <label for="agree">Agree To terms?</label>
> Checkboxes are designed to be toggleable by repeatedly clicking on an element.

> If unchecked, when submitted no data is sent. If it is checked the value of name is set to on "agree=on" in the request.
## value
- ```html
    <label> I like dogs! <input type="checkbox" name="thoughts-on-dogs" value="dogsFTW"></label>
> If checked it would send 'thoughts-on-dogs=dogsFTW'
## Checked
- ```html
    <input checked type="checkbox" id="agree" name="agree">
    <label for="agree">Agree To terms?</label>
> html boolean do not have a value="false". Instead just the word being there indicates the value is true and the the absense of the word means it is false.

## Multiple Items
- ```html
        <div class="checkbox-group">
            <label> Cars 
                <input value="cars" name="transport" type="checkbox">
            </label>
            <label> Trains 
                <input value="trains"  name="transport" type="checkbox">
            </label>
            <label> Planes 
                <input value="planes" name="transport" type="checkbox">
            </label>
        </div>
> All elements have the same name and each checked items sends to the server the name=value. So if cars and planes are checked the server would be sent "transport=cars&transport=planes"
## Exercises
1. Create a checkbox with a label that asks a user if they agree to the terms.
2. Create a checkbox group that has at least 4 checkboxes.
    - It should send multiple items with the same key but different values.
    - (Bonus) - Style using css
