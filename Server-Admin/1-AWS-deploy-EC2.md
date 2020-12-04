# AWS Deploy EC2

## Objecective
- Launch EC2 AWS server instance
- Log into Server
- Install node

## Launch EC2 AWS server
- From your Browser
    1. At dashboard seach for ec2 
    2. Click Launch Instance
    3. Search for Ubutnu
    4. Click on the select button to the right of 'Ubuntu server 20.04 LTS ...' (it should say "Free tier eligible")
    5. The free tier wonu should already be selected. if not select the t2.micro (says free tier eligible)
    6. Click review and launch (no need to configure)
    7. Click Launch
    8. In the popup set the dropdown to 'create new pair' and give the second field a name "aws-ec2", "my_server_key", "ec2_key" ...etc.
    9. Make sure you download pair
    10. Click Launch instance.
    11. Click View instance.
    12. Keep browser open.
- From your terminal
    1. find where the file was downloaded (most likely ~/Downloads)
    2. ```bash
            mkdir ~/keys
            mv ~/{folder where downloaded to}/{keyname} ~/keys/
            #example 
            #mv ~/Download/oct_2020.pem ~/keys/
            chmod 400 ~/keys/{keyname}
            #example
            #chmod 400 ~/keys/oct_2020.pem
    3. Keep the terminal open
- From the Browser
    1. Make sure the instance is checked and click action/connect.
    2. Make sure the 'ssh client' tab is open and copy the part that says "ssh -i ...."
- From the Terminal
    1. ```bash
        cd ~/keys/
    2. Right click paste into the terminal.
    3. type "yes" if prompted in the terminal.
    4. You should be in your server!

## Install Node
1. ```bash
    curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.37.0/install.sh | bash
2. ```bash
    exit
    ## this will exit your server
3. ```bash
    #Log back into server
    ssh -i {The command from above}#You can just push arrow up on the keyboard once
4. ```bash
    nvm #if it says a lot of things then you are good to do

    # Then
    nvm install node

    #next
    npm -g install serve
    npm -g install pm2
    
## deploy app
- In Server Terminal
    1. ```bash
        
        #Clone and install cors-anywhere
        git clone https://github.com/DigitalCraftsStudents/cors-anywhere.git
        cd cors-anywhere
        npm install

        # Use Pm2 to keep the program running
        pm2 start app.js --name "cors-anywhere"

        #show running processes
        pm2 list 
- In browser
    1. AWS EC2 on left panel click on security groups.
    2. Click "Create Security Group"
    3. Name : Webserver Ports Description : Ports open for webserver
    4. Click "Add Rule"
    5. Port range :8080, source :anywhere
    6. Click "create security group" 
    7. Goto instances click on actions -> security -> change security groups
    8. In search/dropdown find "Webserver Ports" and then click add.
    9. Click save.
    10. copy public Ipv4 DNS (ec2-XXX-XXX-XXX-XX.us-east-2.compute.amazonaws.com)
    11. new tab past then put :8080 at the end of the url.
    12. If you see the cors-anywhere page you are done.