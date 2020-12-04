# Function return value

## Objectives
- return value from function
- explicit vs implicit return
- using function returns in arguments
- exercises

# Terms
- *return* - `In programming terms, returning is the value that a function sends out of the result of calling the function.`

## Return value from function
- ```python
    def add_numbers(a,b):
        result = a+b
        return result #sends result out
    
    add_numbers(1,2) #Where did it go?

    # assign the result of the return to the variable
    new_number = add_numbers(1,2)
    print(new_number)
- ```python
    #directly returning something more complex
    def make_dictionary(first, last, phone, zip):
        return {
            "first_name":first,
            "last_name":last,
            "phone_number":phone,
            "zip_code":zip
        }

    clint_data = make_dictionary("Clint", "Fleetwood", "555-555-5555", "30076")

    print(clint_data["zip_code"])
- ```python
    #Do something a bit more complex
    def make_grid(size):
        row = 0
        col = 0
        grid = {}
        while row <= size:
            col = 0
            while col <= size:
                grid[str(col)+'-'+str(row)] = {
                    "row":row,
                    "col":col
                }
                col +=1
            row += 1
        return grid
    
    grid5 = make_grid(5)
    print(grid5['4-3'])
## explicit vs implicit return
- ```python
    #explicit return
    def add_numbers_and_return(a,b):
        print(a+b)
        return a+b # written return is explicit

    result = add_numbers_and_return(2,3)
    print(result) #5

    #implicit return
    def add_numbers(a,b):
        print(a+b)
    
    result = add_number(2,3)
    print(result) #None which is a datatype
> No return is the same as 'return None'. In python a function always return something, even if that something is None.
## using function returns in arguments
- ```python
    length = len([2,3,4]) 
    #len is a python native function that returns the length of an list
    print(length)

    #same results
    print(len([1,3,4]))
    #The return value can be directly used as an argument
- ```python
    def add_numbers(a,b):
        return a+b
    
    result = add_numbers(2, add_numbers(3,4))
    print(result)
## Exercises
1. Write a program that has a function with two parameters. 
    - return the concatinated value of the two parameters.
    - print the results.

2. Write a program that has a function named total_count that expects a list of strings as it argument when the function is called.
    - Have the returned value be a dictionary with the keys 'list_length' and 'total_chars'.
    - The list_length value needs to be the length of the list and the total_chars needs to be the total count of characters of all of the items in the array.
    - Call the function 3 times with 3 different lists.
    - (hint) len is usable on lists and strings.
```python
    #expected output
    totals = total_count(['I', 'Am', 'Awesome'])
    print(totals) #{list_length:3, total_chars:10}
    