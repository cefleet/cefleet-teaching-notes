# CSS position

## Objectives
- Position values
- top, right, bottom, left
- exercises

## Position Value
- ```html
    <!-- static position is default -->
    <style>
        .item {
            position:static;
        }
    </style>
    <div>
        <h1>Title</h1>
        <p class="item"> Statically positioned </p>
    </div>

- ```html
    <!-- relative position works like static, but can be moved with othe declerations -->
    <style>
        .item {
            position:relative;
        }
    </style>
    <div>
        <h1>Title</h1>
        <p class="item"> relativly positioned </p>
    </div>

- ```html
    <!-- absolute position completly takes the element out of the flow -->
    <style>
        .item {
            position:absolute;
        }
    </style>
    <div>
        <h1>Title</h1>
        <p class="item"> relativly positioned </p>
    </div>

- ```html
    <!-- fixed is like absolute but is based o nthe screen and not document position -->
    <style>
        .item {
            position:fixed;
        }
    </style>
    <div>
        <h1>Title</h1>
        <p class="item"> fixed positioned </p>
    </div>
- ```html
    <!-- fixed is like absolute but is based o nthe screen and not document position -->
    <style>
        .item {
            position:sticky;
        }
    </style>
    <div>
        <h1>Title</h1>
        <p class="item"> Sticky positioned </p>
    </div>

## Top, Right, Bottom, Left
- ```html
    <style>
        .item1 {
            position:relative;
            top:10px;
        }
        .item2 {
            position:absolute;
            right:10px;
            bottom:20px;
        } 
        .item3 {
            position:fixed;
            left:30px;
            top:20px;
        }
        .item4 {
            position:sticky;
            left:30px;
            top:20px;
        }   
    </style>
    <div>
        <h1>Title</h1>
        <p class="item1"> relativly positioned </p>
        <p class="item2"> absolute positioned </p>
        <p class="item3"> fixed positioned </p>
        <p class="item4"> sticky positioned </p>
    </div>

