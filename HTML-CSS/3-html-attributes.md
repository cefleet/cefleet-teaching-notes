# HTML Attributes

## Objectives
- What is a html attribute?
- Common Attributes
- Exercises

## Terms
- *HTML Attribute* - `HTML attributes are special words inside of tags that can modifiy the tags behavior or help identify the tag.`

## What is a HTML atttribute?
- ```html
    <!-- The 'href' is the attribute -->
    <a href="http://google.com">Goto Google</a>
    <!-- 'src' is the attribute -->
    <img src="kittens.jpg" />
> Most attributes are to be used with a specific tag only. If added to tags that do not deal with that attribute they will be ignored.
- ```html
    <a href="http://google.com" id="first-link" class="nav-link" >
    Google</a>
    <!-- Each tag can have multiple attributes. Order does not matter. -->
## Common Attributes
- ```html
    <div id="main-content">Main Content</div>
    <!-- hyphen case is the standard, but not required, for id and class names -->
    <section class="side-content">
        Here is some side content
    </section>
>Only one instance of an id should be in any tag in the entire document. 

>Id and class MUST start with "_","-", or a letter. The browser will not error but some javascript functions will not work if you do not follow this convention.

>The standard for ids and class names are words seperated with dashes. dash-case or kebab-case 

> Reference to most attributes. 
https://www.w3schools.com/tags/ref_attributes.asp

## Exercises
1. Create a document that has a h1 and two different section tags.
    - The h1 should say "My Blog"
    - Each section tag should have a class named "blog-content".
    - Each section tag should also have an id. (post_1, post_2 respectivly)
    - Add a paragraph at the root of each section and give that paragraph some fake content.
    - Under the paragraph in each section add some divs that have the classname "comment" and put some fake content in each one.
