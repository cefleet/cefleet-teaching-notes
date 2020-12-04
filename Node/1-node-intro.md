# Node Intro

## Objectives 
- What is node
- Installing node
- *Check for improprly installed node

## Terms
- *Runtime Environment* - `Is the 'space' that a piece of software is executed. It can refer everything including the hardware, but it can also be talking about the software that is executing another software such as node.`
##  What is node?
- Node is a javascript runtime environment  created to be used on a server, but has been since adpted to be used almost on any computer or device.
- It was created by Ryan Dahl, who has since left node and created another Js runtime called deno. 
- The main function of node is to allow javascript to be used in places that formally required require another language, such as a server. This enables a developer to only know one language to do front-end and backend development.

> More about node and a lot of additional study for node. https://www.youtube.com/playlist?list=PLlrxD0HtieHje-_287YJKhY8tDeSItwtg

## Installing node
> There are many wrong ways to install node where you will be limited in what you can do. If you installed node incorrectly you will struggle moving forward with some issues. *Check for Inproperly installed node

- The correct way to install node, in order to prevent major issues, is to use the Node Version Manager (nvm .. not to be confused with npm )
- ```bash
    # In Terminal
    curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.35.3/install.sh | "$SHELL"

    # Close Terminal
    exit
    #or just close the window
- ```bash
    # in newly opend terminal

    #installs node
    nvm install node

    node --version # v15.#.# or something like it
## *Check for Improperly installed node
- ```bash
    # installs a simple server golbally so it can be used everywhere
    npm install -g serve

    # If you get a permission Denied error in red you will need some help installing node correctly.