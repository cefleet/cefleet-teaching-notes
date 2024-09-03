# Git Basics
## Objectives
- Launch a terminal in codespaces
- Save work to github
- Add teacher as colaborator to repository

# Terms
- *Repository* - `In computer programming terms, a repository is a place to store code.`
- *Git* - `A repository engine that helps the devlopers work with code in teams`
- *colaborator* - `A colaborator is a person who can interact with the repository`
- *Terminal / Command Line* - `The computer program that allows the user to run computer programs using text instead of buttons and forms`

## Launch a terminal in code spaces
> In Codespaces a terminal is normally already up. It is at the bottom and has your username behind a '@'.

- If the terminal is not visible: click on the hamburger menu in the top left and select view-> terminal.

- You now have launched the terminal

## Save work to github
- In the terminal type
```bash
    git status
```
- press enter, You will see some files and folders in red.

- In the terminal type
```bash
git add *
```

- press enter, you will see all of those things in green now. (You will also see the contents of the folder so the list will be longer.)

- In the terminal type 
```bash
git commit -m "Adding files to git"
```
- press enter and you will see some info about things added. It will tell you how many files have been changed.

- *Important* - The -m "Whatever text is here" is the message about what the commit is doing. It is required, but you can say anything inbetween the double quotes.

- In the terminal type
```bash
    git push
```
- Press enter and you will see more information. 

- Congrats you have pushed your code to the repository.

>As a student, you should save your work to github every time you are done with the work and are stepping away from the computer. However when you get a job that may not be the best idea for various reasons.

Simplified adding work to github
```bash
    git add *
    git commit -m "Made some changes"
    git push
```

## Adding teacher as colaborator 

### Viewing a repository
- In a web browser, open a new tab and go to www.github.com
- You should be logged in already, but if not log in.
- Click on your profile picture and select "Your repositories"
- Click on the name of the repository
- You should see the files from codespaces!

### Adding colaborator
- Click on the settings link at the top with a gear
- Click on the colaborators link on the left.
- Click on the green button that says "Add People"
- type in "cefleet" and select the user that say clint fleetwood
> This give me permission to see and also to write to your repository. You can give other students access, but without modifying the settings they can write to your repository and possible mess something up.

