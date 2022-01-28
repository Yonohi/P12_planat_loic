Important

Créer sa base de donnée postgresql
Aller dans Pgadmin,
Créer un nouvel utilisateur avec Login/Group roles en lui donnant les permissions adaptées,
Créer une nouvelle base de données via Database en spécifiant un nom et un password,
puis dans notre fichier settings (dans notre projet)
intégrer les noms et mot de passe dans DATABASES

faire python3 manage.py makemigrations <nomapp> (pour les 2)
puis migrate
ensuite createsuperuser
