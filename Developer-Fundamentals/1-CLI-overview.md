# CLI Overview

## Objectives
- Launch Terminal
- Run Programs from Command Line
- Do Class Exercises

## Terms
- *Terminal / Command Line* - `The computer program that allows the user to run computer programs using text instead of a GUI`
- *GUI / Graphic User Interface* - `The User interface that uses graphics to click on pictures (icons) to run computer programs`

## Launch Terminal

## Run Programs
- ```bash 
    pwd
- ```bash
    ls
### Add Arguments
- ```bash
    ls -l
- ```bash
    ls -la
### Add Modifiers
- ```bash
    cd /
    ls
    pwd
- ```bash 
    cd ~
    pwd
- ```bash
    mkdir ~/DigitalCrafts
    cd DigitalCrafts
    pwd

### Additional Commands
```bash
    cd /
    pwd
    cd ./home
    pwd
    cd /home/{your_username}
    pwd
    cd ~/DigitalCrafts
    pwd
    cd ../
    pwd
    cd ~
    pwd
```

## Exercises

1. Create a file called "command-line.md" using the touch command.
   - ```bash
        touch {name_of_file}
2. Move the file just created from current directory to inside the DigitalCrafts folder using the mv command.
   - ```bash
        mv {name_of_file} {directory_to_move_file_to} 