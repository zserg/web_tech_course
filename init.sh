#!/bin/bash
git config --global user.email "zsergt3@gmail.com"    
git config --global user.name "zserg"              

sudo ln -s /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/test.conf
sudo rm  /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart

sudo ln -s /home/box/web/etc/wsgi /etc/gunicorn.d/wsgi
sudo ln -s /home/box/web/etc/django /etc/gunicorn.d/django
sudo /etc/init.d/gunicorn restart

