# Git (Version Control) Basics

## Objectives 
- Install / Setup Git
- Create github account
- Create First Git repository
- Exercise
## Terms
- *Repository/Repo* - `A group of files and folders that are stored in a VCS`
- *Version Control System / VCS* - `A system to store files, update files, collaborate, and undo mistakes in a repositories`

## Install / Setup Git

- Install git 
- Setup git
    ```bash
    git config --global user.name "Firstname Lastname"
    git config --global user.email myaddress@example.com
## Create Github Account
- https://github.com/

## Create First Git repository

We will create a git repository from the CodingLessons/classes folder.

1. ```bash
    cd ~/CodingLessons/classes
    git init    #Initilizes a git repo
    ls -lart   #You should see a .git folder
    git status  #shows the status of items
    git add .   #Starts tracking all of the files (. or *)
    git commit -m "first commit" #adds a commit with a message
2. Goto http://github.com login.
3. Create repository named "Digital Crafts Classes"
    - Make sure you do NOT create it with a readme.md
4. ```bash
    git remote add origin https://github.com/{github-username}/{repository-name}.git
    #You can find the url on the page you created in github
    git push -u origin master