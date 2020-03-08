# Disease Progression Model web applications
## Code forked from [mrazvan22/brain-coloring-website](https://github.com/mrazvan22/brain-coloring-website)
## Thanks Raz!

Raz's website template is open-source and adapted from the grayscale template: https://startbootstrap.com/themes/grayscale/. It was published under the free, MIT license. 

## Installation

1. Install Flask

2. FIXME: Install your favourite [EuroPOND model(s)](http://europond.eu/software) using docker:

`sudo docker run -it europond/model-x`

Once the docker container finishes installation, it should automatically connect to the shell. Once inside docker, pull the latest changes if any:

    ``` cd /home/model-x/ ```
    
    ``` git pull origin master```


2. Run the website using flask:

`
 FLASK_APP=main.py FLASK_ENV=development FLASK_DEBUG=1 flask run
`

## Customisation

Main files to modify are:
* main.py
* templates/index.html

