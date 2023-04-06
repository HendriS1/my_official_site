# DJANGO PROJECT / MY_OFFICIAL_SITE
---
## INTRODUCTION
---
* The  goal of this project was for me to use the basics of Django to build a Django app that functions. This app called my_official_site has all the basics of a Django app. It is a website created for a fictional Band called Euphoric Nebula, it has a a Home page, Login page where the user can Login or if they do not have a profile they can create one and login to view all the events sceduled for this fictional band. The events page uses database-driven components. The user can only view the events if they have successfully logged in. This app also has a logout page for the user to log out with if they so to do so.
* I've also used Sphinx External Documentation to document the views.py and models.py files of this Django project. To access this open the index.html file inside your browser. index.html can be found at my_official_site/docs/_build/html.
* This project can be expanded on to create additional pages etc.
---
### Image of Events page.
![](Images/Screenshot%202023-04-06%20235340.png)
---
## WHY I BUILT THIS PROJECT
---
* I built this project to challenge myself with using Django. I wanted to Build a website that isn't just a one page static html file. This project challenged me to learn more about what Django has to offer and to have a deeper understanding of Django in a whole. I've also learned more about database-driven components in building this project and how to build hyperlinks and how to set up the mapping of these hyperlinks to take the user to diffirent pages.
---
## USAGE
---
### Installing and Avtivating Virtual Enviroment.
-Name your virtual enviroment as you wish.
- For this example we will call it (myenviroment)
#### Windows:
* python -m venv myenviroment
#### Unix/MacOs:
* python3 -m venv myenviroment
---
##### This will set up a virtual enviroment and create a folder named myenviroment
---
### Activating your Enviroment
#### Windows:
* myenviroment\Scripts\activate.bat
#### Unix/MacOs:
* source myenviroment/bin/activate 
---
##### Once this is done successfully you will see this in your command prompt:
---
#### Windows:
* (myenviroment) C:\Users\Your Name >
#### Unix/MacOs:
* (myenviroment) ... $
---
### Installing Packages and Django
* run pip install -r requirements.txt
---
## DOCKER HUB Quickstart
* Go to the following website for detailed instructions on how to get started with Docker Hub to be able to START THE DJANGO APP WITH DOCKER.
(http://docs.docker.com/docker-hub/quickstart/)
---
### Image of the Home page
![](Images/Screenshot%202023-04-06%20210827.png)
---
## STARTING DJANGO APP WITH DOCKER
---
* Go to (http://hub.docker.com/repository/docker/hendris1/my_official_site/tags?page=1&ordering=last_updated)
* Copy the pull command
* Paste the pull command in your command prompt and press enter
##### This will download the Docker Image from the internet
##### After this is done, type the following in the command prompt.
- docker run -d -p 8000:8000 "the docker image name/it is written with the pull command"
- After go to (http://127.0.0.1:8000)
##### Type the following to stop your image.
- docker stop "first 3 characters of docker image id"
---


