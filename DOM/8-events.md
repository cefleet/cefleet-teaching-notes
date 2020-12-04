# Events

## Objectives
- Event Object
- Setting html attribute
- Event Target
- What NOT to do ever...ever

## Event Object
- ```js
    //Created Event Object
    let myEvent = new Event("random")
    console.log(myEvent)
    //its an object like everything else

- ```js
    //the attribute is the event 'type' with on in front of it.
    window.onresize = function(evt){
        console.log(evt) // the event object is passed!
        //do more things!
    }

## Setting HTML attribute
- ```js
    let clicked = 0
    let button = document.querySelector("#more-info")
    button.onclick = function(evt){
        clicked++;
        button.innerText = clicked
    }

- ```js
    //JUst for fun
    let color = 254
    let body = document.querySelector("body")
    //again the browser passes the event to the function
    body.onscroll = function(e){
        body.style.background = `rgb(${color}, ${color}, ${color})`
        color--
        color = color < 0 ? 0:color
    }
    //color gets darker as your scroll

- ```js
    //asynchronous
    let profilePic = document.createElement("img")
    profilePic.onload = function(evt){
        console.log('picture src is downloaded Now I can add it')        
        document.body.append(profilePic)
    }
    console.log('trying to load the image')
    profilePic.src = "https://www.desktopbackground.org/download/1920x1200/2015/12/13/1056660_top-large-hd-wallpapers-landscape-wallpapers_1920x1200_h.jpg"

## Event Target
- ```js
    //event target
    let button = document.querySelector("#more-info")
    button.onclick = function(event){
        console.log(event.target)
    }
- ```js
    //no need to set a variable
    document.querySelector("#more-info").onclick = function(evt){
        console.log(evt.target)
        evt.target.classList.toggle("primary")
    }
- ```js
    //using a single function on multiple items
    let ideas = document.querySelectorAll(".child-idea")
    const toggleBackground = function(evt){
        evt.target.classList.toggle("primary")
    }
    ideas.forEach(function(idea){
        idea.onclick = toggleBackground
    })

## What NOT to do ever...ever
- ```html
    <!-- seriously don't do it... I'm not kidding -->
    <button onclick="stupidFunction()">Do not Ever Do this</button>

    <script>
        const stupidFunction = function(){
            console.log('By doing this, I have committed to the worst possible practices and really should be in a constant state of shame')
        }
    </script>

## Exercises
1. Create a document that has a button. 
    - Have that button change background color when you click on it.
2. Have a list of items with a title and additional info for each item.
    - When you click on the title have the additional info toggle. (Hint look at mdn Node.nextSibling or Node.parent.childNodes)
- ```html
    <!-- example html modify as much as you wish -->
    ...
    <ul>
        <li>
            <div class="title">Title 1</div>
            <div class="additional">...lots of text</div>
        </li>
        <li>
            <div class="title">Title 1</div>
            <div class="additional">...lots of text</div>
        </li>
        <li>
            <div class="title">Title 1</div>
            <div class="additional">...lots of text</div>
        </li>
    </ul>