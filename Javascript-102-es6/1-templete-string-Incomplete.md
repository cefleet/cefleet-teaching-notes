# Template Strings

## Objectives
- Template String
- Advanced Functionality
- Exercises

## Template String
- ```js
    `
        string with
        breaks
        inside
    `
    //can span multiple lines. HTML output the literal spaces.
- ```js
    //templete strings (template literals)
    //like python fstrings but no f and only used with `
    let a = "Awesome"
    let b = "Super"
    console.log(`the letter a = ${a} and b is ${b}`)
## Advanced Functionality
- ```js
    let myName = "Clint"
    let output = `Is ${myName} longer than 6 ? ${myName.length>6 ? 'YES!': 'No'}`
    console.log(output)
    //Using ternery inside
- ```js
    let myArray = [{name:"Clint"}, {name:"Anna"}, {name:"Olivia"}]

    let output = `
    My Family names are :
    \n
    ${myArray.map(p=>p.name).join("\n")}
    And some others.
    ` 
    console.log(output)