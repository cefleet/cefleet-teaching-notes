# PM2 Serve Bash
## Objectives
- pm2 start node app
- pm2 start bash

## Pm2 start node app
- ```bash
    #assumes you have cloned and installed a node application

    node app.js # or whatever name it has

> Goto sites and see if it works.

> Hint make sure the port is open in security group if you are using aws.

- ```bash
    # Use pm2 to keep your site running even when you close the terminal
    cd {site folder}

    pm2 app.js --name {site name}

    #test with 
    pm2 list

## pm2 start bash
- We can host a static non-node site 
> The #! /bin/bash is not a comment. It is part of the bash file
- ```sh
    # host.sh (inside folder with site)
    nano host.sh
> nano is a text editor for the server
- ```sh
    #! /bin/bash
    serve -p XXXX
> When done press ctrl-o (oh not zero) then ctrl-x
- ```bash
    # From terminal
    chmod 0777 host.sh

    pm2 start host.sh --name {name_of_site}