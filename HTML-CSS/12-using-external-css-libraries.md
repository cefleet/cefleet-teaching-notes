# Using External CSS Libraries

## Objectives
- How To use Library/Framework
- How to read docs
- Examples
- Exercises

## Terms
- *Library* - `In software developement a library is a bit of code that is used to preform specific tasks.`
- *Framework* - `In software development a Framework is software that provides a default functionality and it's own standardization for a project.`
- *CDN* - `Content Delivery Network is a way to host software on the internet to be usable by the public`

## How to use a CSS Library / framework

- ```html
    <head>
    ...
    <!-- downloaded -->
    <link rel="stylesheet" href="/library-folder/library.css">
    <!-- "/library-folder/library.css" would be replaced with the folder and file name -->
    ...

- ```html
    <!-- cdn -->
    <link rel="stylesheet" href="https://cdn-network.com/library-name/library-file.css">
    <!-- again the href will be changed with the library's cdn -->

- ```html
    <!-- framework with javascript -->
    <link rel="stylesheet" href="https://cdn-network.com/library-name/library-file.css">
    <script src="https://cdn-network.com/library-name/library-file.js">

- ```html
    <!-- adding custom css along with library or framework -->
    <link rel="stylesheet" href="https://cdn-network.com/library-name/library-file.css">
    <link rel="stylesheet" href="/styles/my-styles.css">
## How To read the docs
> RETU - Read, Explorer, Try/Test, Understand
- Quickly read over the website or readme if it has one to see if you can even use the library. Get a cursery view of how the library works.
- Explore the various things the library does. Find some things that can help your project.
- Test out a few things. Make sure the docs work the way the library says it does. Make a sample file and just do some of the things the docs say.
- Before diving fully into library and dedicating a lot of time with it, look over the code on github and see if you can understand how it works. It is not required to fully understand it (especially with large frameworks) but it is always best to understand tools your are using.

## Examples

### Libraries
- http://kazzkiq.github.io/balloon.css/
- https://bttn.surge.sh/
- http://necolas.github.io/normalize.css/
- https://github.com/kognise/water.css

### Frameworks
- https://getbootstrap.com/
- https://bulma.io/
- https://purecss.io/
- https://materializecss.com/

## Exercises
1. Make a very very small website using one of the libraries above.
    - Use some of the features for the library

2. Make another small website using a layout system for one of the frameworks mentioned above.
    - Add one of the components to your site that you can find in the documentation.
