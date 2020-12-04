# Event Listeners

## Objectives
- Adding Event Listeners
- Removing Event Listeners
- Dispatching Custom Events
- Exercises

## Adding Event Listeners
- ```js
    const func1 = function(){
        console.log('function1 was fired')
    }
    const func2 = function(){
        console.log('function2 was fired')
    }
    let button = document.querySelector("#more-info")
    button.onclick = func1
    //add another
    button.onclick = func2
    //only function 2 is fired but i want both!
- ```js
    ...//same as above but add this
    button.addEventListener("click", func1)
    button.addEventListener("click", func2)
    
- ```js
    console.log('Gonna load the DOM')
    window.addEventListener("DOMContentLoaded", function(evt){
        console.log('THE DOM HAS BEEN LOADED!')
    })

## Removing Event listeners
- ```js
    const someFunc = function(evt){
        console.log('Fire this event')
    }

    button.addEventListener("click", someFunc)
    button.removeEventListener("click", someFunc)
- ```js
    let scrollAmount = 0
    const scrollFunc = function(){
        console.log(scrollAmount)
        scrollAmount++;
        if(scrollAmount > 30){
            window.removeEventListener('scroll', scrollFunc)
        }
    }

    window.addEventListener('scroll', scrollFunc)

- ```js
    ...//same button
    const func1 = function(evt){
        console.log('I need to be fired only once')
        //remove the listener
        evt.target.removeEventListener("click",func1)
    }
    const func2 = function(){
        console.log('function2 was fired, and can be over and over')
    }

    button.addEventListener("click", func1)
    button.addEventListener("click", func2)

- ```js
    //Cannot remove listener created on the fly.
    button.addEventListener("click", function(){
        console.log('This cannot be removed')
    })

    window.addEventListener("scroll", function(){
        //even though this looks the same, it is a different function
        button.removeEventListener('click',
        function(){
            console.log('This cannot be removed')
        })
    })

## Dispatching Custom Events
- ```js
    //Not used extensivly on day-to-day
    // but it is interesting and can be useful in 
    // unique circumstances
    window.addEventListener("jump", function(){
        let newDiv = document.createElement("div")
        newDiv.append("Chris Cross gonna make you Jump, Jump!")
        document.body.append(newDiv)
    })

    let myInterval = setInterval(function(){
        window.dispatchEvent(new Event("jump"))
    }, 3000)

## Exercise
1. Using event listeners:
    - Add an event listener to a button and have the text of a button increase every time it is pushed.
    - When the button is clicked 10 times. Change the color of the button and remove the event listener.
    - (bonus) do this without using a variable.
2. Create a div with WAY too much text, but limit the size of the div and allow the div to scroll using css.(hint lookup scrolling in css on mdn)
    - When the text scrolls to the top make the background more blue
    - when the text scrolls to the bottom make the background more red.