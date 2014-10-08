django-taster-blog
==================

Trying Django and Google App Engine

Install
-------

    git clone git@github.com:bugthing/django-taster-blog.git
    mkdir tmp
    cd tmp/
    git clone https://github.com/django-nonrel/django
    git clone https://github.com/django-nonrel/djangoappengine
    git clone https://github.com/django-nonrel/djangotoolbox.git
    git clone https://github.com/django-nonrel/django-dbindexer.git
    hg clone https://bitbucket.org/twanschik/django-autoload
    mv django/django ../django-taster-blog/
    mv djangoappengine/djangoappengine ../django-taster-blog/
    mv djangotoolbox/djangotoolbox ../django-taster-blog/
    mv django-autoload/autoload ../django-taster-blog/
    mv django-dbindexer/dbindexer ../django-taster-blog/
    mv django-autoload/autoload ../django-taster-blog/
    cd ../django-taster-blog
    rm -rf ../tmp

Setup
-----

Create a login:

    python manage.py createsuperuser


Ensure the app works by running the tests:

    python manage.py test blog

Run
---

Get dev server up like so:

    python manage.py runserver

Then visit:

    http://127.0.0.1:8000/

Deploy
------

Send it up to the Google App Engine:

    python manage.py deploy

Create a login in GAE:

    python manage.py remote createsuperuser

