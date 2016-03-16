#!/usr/bin/env bash
sudo /etc/init.d/apache2 stop
sudo /bin/ln -sf /home/box/web/etc/gunicorn-local.conf  /etc/gunicorn.d/test
sudo /bin/ln -sf /home/box/web/etc/ask.gunicorn-local.conf  /etc/gunicorn.d/ask
sudo /etc/init.d/gunicorn restart

sudo /bin/ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/test.conf
sudo /etc/init.d/nginx restart
