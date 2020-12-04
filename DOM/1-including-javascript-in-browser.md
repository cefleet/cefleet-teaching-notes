# Including javascript in Browser

## Objectives
- launching local web server with python
- index.html
- including javascript file in document
- launching local web server with node

## Terms
- *Local Web Server* - `Some parts of javascript need a server to operate correctly. A local server is a web server that runs on your local computer in order to host these websites for testing and development.`
- *port* - ` In web terms, port is a numbered address that allows data traffic to flow. Ports must be opened and ready to recieve data if it can be used`
- *localhost* - `localhost is the local address for a development computer. It only points to the computer you are currently using. It is also written 127.0.0.1`

## Launching local web server with python

- ```bash
    python3 -m http.server xxxx
    # xxxx is the port number. It needs to be above 3000 by convention the default for local servers are often 8000 or 5000
- Open a browser and goto "http://localhost:XXXX" where XXXX is the port you opended.
- You should see a list of files. It shows a directory.

## index.html
> Web servers will "host" the location it is launched from.

> Web servers look for index.html in the directory it is launched from. If it cannot find an index.html it will host the files.

## Including Javascript files in documents
- ```html
    <!-- index.html -->
    <!DOCTYPE html>
    ...

            <script>
                //this is just for testing
                alert('Hello Browser')
            </script>
        </body>
    </html>

### Including a js file
- ```js
    //script.js
    alert('Look I am loaded')
    console.log('This is in the console.')    
- ```html
    <!-- index.html -->
    <!DOCTYPE html>
    ...

            <script src="script.js"></script>
        </body>
    </html>

## Lauching webserver with node
- (optional for now)
- ```bash
    npm install -g serve
    ...#lots of stuff happens
    cd ~/folder/you/want/to/server/from
    serve -p XXXX

## Exercise
1. create a full html document and serve it and view it from a browser.
2. Add some css and a script to that file and view it from a browser.
    - add an alert to the script file that says something.
    - add a console.log to the script file.