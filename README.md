# DBMS Project

## Setup

- Install python
- Install django
```
pip install django
OR
sudo pacman -S python-django
```

### Install dependencies
```
pip install -r requirements.txt
OR
sudo pacman -S python-pipenv
```

### Setting up Virtual Env (important)
Required Reading: https://realpython.com/pipenv-guide/
```sh
#spawn the virtual env
pipenv shell

# install all the required dependencies
pipenv install --dev    
```


### Some stuff
- Creating apps for the project 
```
./manage.py startapp app_name
```