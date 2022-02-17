# P12_planat_loic
<p align="center" style="background-color:#48C5EA">
<a href="https://user.oc-static.com/upload/2020/09/22/16007804386673_P10.png" class="oc-imageLink oc-imageLink--disabled"><img src="https://user.oc-static.com/upload/2020/09/22/16007804386673_P10.png" alt="Logo Epic Events"></a>
</p>
<center> <h2>OpenClassrooms Project</h2> </center>

## Description

Project Django using Django REST Framework and the database Postgresql.  
The goal is to have a CRM where users could see clients, contracts and Events with different permissions.
***
## Requirements
Python 3 : https://www.python.org/downloads/

Postgresql : https://www.postgresql.org/download/

POSTMAN : https://www.postman.com
***
## Creation of the database Postgresql

In Pgadmin you have to create a new user in Login/Group (can change according to version)   
After that, create a new database with a name, a password and a name of owner (the user you have created before).  
***
## Installation

In the terminal, move to the directory where you want to install the repository with the command line:
`cd <pathdirectory>`

Clone the remote repository: 
`git clone https://github.com/Yonohi/P12_planat_loic.git`

Go into the new folder:
`cd P12_planat_loic`

In the folder settings.py which is in /P12_planat_loic.git/EpicEvents/EpicEvents/  
change the content of DATABASES by :  
```
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "<name_of_your_db>",
        "USER": "<username>",
        "PASSWORD": "<password>",
        "HOST": "localhost",
        "PORT": "5432",
    }
}
```

Create the environment:
`python3 -m venv env`

Activate the environment:

* On Unix and macOS:
`source env/bin/activate`

* On Windows:
`env\Scripts\activate.bat`

Now, install packages from requirements.txt
`pip install -r requirements.txt`

Go into the folder named LITReview
`cd EpicEvents`

Now you have to apply migrations with
`python3 manage.py migrate`

Run in local
`python3 manage.py runserver`

Now you can test with POSTMAN the collection P12_EpicEvents.

For more information about endpoints: https://documenter.getpostman.com/view/16930251/UVkiSdwL

***
## Need a superuser?
You have to go to the project folder and type
```
python3 manage.py createsuperuser
```
Now give your username, mail and password, and it's done. The admin page is reachable.
```
http://127.0.0.1:8000/admin/
```
***
## Conclusion
Very interesting project, create groups and allow permissions by the admin zone was fun. I learnt more about Django Rest and how to use specific database.
***
## Author
Loïc Planat