Iniciar o projeto Django

```
python -m venv venv
. venv/bin/activate
pip install django
django-admin startproject project .
```
# starting apps
python manage.py startapp <user>

# Dabase Migrate
python manage.py makemigrations
python manage.py migrate

# Superuser
python manage.py createsuperuser
pythno manage.py changepassword USERNAME

Configurar o git

```
git config --global user.name 'Seu nome'
git config --global user.email 'seu_email@gmail.com'
git config --global init.defaultBranch main
# Configure o .gitignore
git init
git add .
git commit -m 'Mensagem'
git remote add origin URL_DO_GIT
```
