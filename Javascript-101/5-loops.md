# Loops

## Objectives
- while loops
- for loops
- break
- continue
- Exercises

## While Loops
- ```js
    let i = 1;

    while(i < 10){
        console.log(i)
        i++
    }
    console.log(i)

    while(i > 0){
        console.log(i)
        //you could do anything here
        i--
    }
    //Infinate loops in the browser will cause the world to end. 
    //Friends don't let friends infinate loop in the browser
## for loops

- ```js
    //initial value; condition; incrimenter 
    for(let i = 0; i < 10; i++){
        console.log(i)
    }

    //optional leave out initial value
    let i = 1
    for(; i<20; i++){
        console.log(i)
    }

## break
- ```js
    let i = 0;
    while(i < 10){
        if(i > 5) break;//breaks the loop
        console.log(i)
        i++
    }
- ```js
    //leaving out the condition ..infintate loop
    for(let i = 0;;i++){
        if(i > 10) {
            break;
        }
        console.log(i)
    }
## continue
- ```js
    for(let i = 0;i<20;i++){
        if(!(i % 2)) continue;
        console.log(i)
    }
- ```js
    //infinite loop warning!
    let i = 0;
    while(i < 10){
        if(i % 2 == 0) continue;//why infinite loop?
        console.log(i)
        i++
    }

## Exercises
1. Using a while loop add numbers from 1 to 10.
2. Using a for loop, count from a number of your choice to another number.
3. Using a for loop, start with a number and then divide and replace that number by each number from 6 to 2.
```js
n = 300 //you choose a number
... // your code
console.log(n) 
//something like 0.000496031746031746
```
4. Using either type of loop add all of the numbers not divisible by 2 and 3 from 0 to a number of your choice.