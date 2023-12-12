# CSS Flexbox

## Objectives
 - Using Flexbox
 - Simple examples
 - Exercises

## Using Flexbox
- ```html
    <style>
        .container {
            display:flex;
        }
    </style>

    <div class="container">
        <div> Item 1</div>
        <div> Item 2</div>
        <div> Item 3</div>
        <div> Item 4</div>
    </div>

## Simple Examples
- ```html
    <!-- non-flexbox way -->
    <!-- have to keep changing the size, not really responsive -->
    <style>
        .container {
            width:400px;
        }
        .container div{
            width:50px;
            display: inline-block;
            padding:10px;
            border:1px solid;
            margin:6px;
            text-align:center;
        }
    </style>
    <!-- using the div with the 4 items -->
- ```html
    <!-- flexbox way -->
    <style>
        .container {
            width:400px;
            display:flex;
        }
        .container div{
            width:100%;
            padding:10px;
            border:1px solid;
            margin:6px;
            text-align:center;
        }
    </style>
- ```html
    <!-- flex justify-content can change the positions -->
    <style>    
     .container {
            width:400px;
            display:flex;
            justify-content: space-between;
            
        }
        .container div{
            width:40px;
            padding:10px;
            border:1px solid;
            margin:6px;
            text-align:center;
        }
    </style>
- ```html
    <!-- flex wrap is really helpful for responsivenes -->
    <style>
        .container {
            width:400px;
            display:flex;
            flex-wrap: wrap;
        }
        .container div{
            width:120px;
            padding:10px;
            border:1px solid;
            margin:6px;
            text-align:center;
        }
    </style>
    <div class="container">
        <div> 
            <p>Item 1</p>
            <p>
                Non veniam tempor esse Lorem amet 
                Lorem incididunt duis mollit dolor aute 
                ad adipisicing duis.
            </p>
        </div>
    ...
    </div>
