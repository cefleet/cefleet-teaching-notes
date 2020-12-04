# Full Valid HTML Documents
## Objectives
- How to start a valid html document
- Special Elements

## How To start a valid html document
- ```html
    <!DOCTYPE html>
    <html>
        <head>
            <title>Title in Toolbar
        </head>
        <body>
            <div>
                The body is everything that the web browser renders.
            </div>
        </body>
    </html>
> Browsers will fill in the gaps if you leave some of these parts out. It is best to create valid html pages to begin with.

## Special Elements

- ```html
    ...
    <head>
        <title>Adds a title to toolbar</title>
        <meta name="description" content="Shows up in a search engine description...normally">
        <!-- there are a lot other meta tag attributes -->
        <link rel="stylesheet" href="style.css">
        <link rel="icon" href="favicon.ico">
        <style>
            /*
                Can add css here!
            */
        </style>
        <script>
            //I can add Javascript here!
        </script>
        <script src="scripts.js">
    </head>
    ...
>We will talk more able link,style, and script later. 

> Addition information about meta
https://developer.mozilla.org/en-US/docs/Web/HTML/Element/meta/name

## Exercises
1. Create a small fully valid html document.
    - Add a description meta tag with a description of the website. 