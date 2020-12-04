# Public API

## Objectives
- What is a public API
- Using Params Query Strings
- Getting Data via ajax
- Issues
- Exercises

## What is a public API
> A public api is an api that is facing out of the internal organization. It is not nessearly free or avalible to anybody.

> Git list of public api : https://github.com/public-apis/public-apis

- ```bash
    # Star Wars Data
    https://www.swapi.tech/api/
   
    # Random User
    https://randomuser.me/api/

## Using Params and Query Strings
- ```bash
    #list all planets
    https://www.swapi.tech/api/planets/
    #Give data about planet 1
    https://www.swapi.tech/api/planets/1
    # Get vehicle # 4
    https://www.swapi.tech/api/vehicles/4

    #get 10 random users
    https://randomuser.me/api/?results=10
    #get 5 random males
    https://randomuser.me/api/?gender=male&results=5
    #Jmest names, gender and picture of 20 females
    https://randomuser.me/api/?inc=gender,name,picture&gender=female&results=20

# Getting Data via Ajax
- ```js
    import {ajax} from "./modules/ajax.js" //From previous

    ajax("https://www.swapi.tech/api/planets/1",(results)=>{
        //The data should be JSON!!!
        let data = JSON.parse(results)
        console.log(data)
        //Now I can handle the data however i need to.
    })

## Issues

### CORS
> Due to security and browser issues that we can discus in detail later, you can end up with a cors error. We can come up with other ways of dealing with it, but for now just put the following in front of the url.

> Below may be broken ???
> https://cors-anywhere.herokuapp.com/

- ```js
    /* config.js */
    export const corsFix = "https://cors-anywhere.herokuapp.com/"
- ```js
    /* any other files */
    import {ajax} from "./modules/ajax.js"
    import {corsFix} from "config.js"

    let callback = (res)=>console.log(JSON.parse(res))

    ajax(corsFix+'https://randomuser.me/api/?results=10', callback)
### Too many requests
> If you make too many request from the same IP address or api key, the server may see it as spam. It can then reject the request. 

> One solution is to make sure that data is always requested when a page changes or refreshes.

> If your app search an api via search bar limit how quickly a user can search.

> There are caching techniques that can be use to limit the amount of request sent to the service.

### 404
> Sometimes the service is simply down. You need to come up with solutions to handle this.

## Just some interesting APIs

> https://robohash.org/

> https://avatars.dicebear.com/

> https://thispersondoesnotexist.com/

## Exercise
1. Using an api make a mini app that will fetch data and make "cards" from that data fetched.
    - using ajax get data (random or specified) from an api in a group.
    - For each one of these items recieved create a card with data collected from the API.
    - Make the cards removable. (Think of an x on the top corner or a remove button)
    - Add CSS to make it responsive
    - Add additional features you find interesting.
