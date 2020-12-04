# HTML Nested Tags

## Objectives
- Nest HTML tags
- Some tags need nesting
- Gotchas
- Exercise

## Nest HTML tags

- ```HTML
    <!-- simple nesting -->
    <div>
        <p>
            I am some content
        </p>
        <p>
            I am more content
        </p>
    </div>
- ```html
    <!-- Deep level nesting -->
    <div>
        <section>
            <p>
                Things are good today. 
                <span>
                    Really Good!
                </span>
            </p>
        </section>
    </div>
- ```html
    <!-- space and tabs do not matter -->
    <div><p> I love <span> spaned </span> content</p> </div>
## Some tags need to be nested
- ```html
    <ul>
        <li> Peas</li>
        <li>Carrots </li>
        <li>Potatoes </li>
    </ul>

    <table>
        <tr>
            <td> Peas</td>
            <td> Carrots</td>
            <td> Potatoes</td>
        </tr>
        <tr>
            <td>Ice Cream</td>
            <td>Pancakes</td>
            <td>Baklava</td>
        </tr>
    </table>

## gotchas
<!-- This is a big, common error -->
- ```html
    <!-- opening and closing tags mixed up -->
    <div>
        <p>
            <span>
            Some content to use
        </p>
            </span>
    </div>
- ```html
    <!-- bad practices -->
    <!-- Using hr to draw line is not symantic -->
    <hr />
    <hr />
    <hr />

    <b>B is bold. IT is not symantic but is a style. HTML is not supposed to use style</b>
    <i> Like B I means itallic. HTML is not supposed to represent style.</i>
## Exercises
1. Create a document that has a div with 3 sections nested inside.

2. Create a document that has an unorded list with at least 4 list items.

3. Create a document that has a div and then a header, then a div and then a footer element.
    - Have the header have a h1 tag that acts as the title of the document.
    - Have the div have at least 1 link and one image nested inside.
    - have the footer have at least one span inside.
    
