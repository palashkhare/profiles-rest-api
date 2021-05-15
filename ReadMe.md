# API project

GIT commands:
git init
git add .
git commit -am "comment"

git push origin master ... (from git home page)

Vagrant commands
To create a vagarant template file in project folder
Vagrant init ubuntu/bionic64    {bionic64 is ubuntu image}
..Update themplate file..
To build image as per template
Vagrant up
To log into Vagrant image
Vagrant ssh
To exit
exit

Django
django-admin startproject djangoapi
manage.py startapp profiles
customize user model
manage.py makemigration 'appname'
manage.py migrate

create models - django orm
create views
create serializers  
