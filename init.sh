#!/usr/bin/env bash
#sudo /bin/ln -sf /home/box/web/etc/gunicorn.conf  /etc/gunicorn.d/test
#sudo /etc/init.d/gunicorn restart
sudo /bin/ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/test.conf
sudo /etc/init.d/nginx restart
gunicorn -b 0.0.0.0:8080 web.hello:application -D
