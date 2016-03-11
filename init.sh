#!/usr/bin/env bash
if [ -f /etc/nginx/sites-enabled/default ]; then 
    sudo rm /etc/nginx/sites-enabled/default
fi
sudo /bin/ln -sf /home/box/web/etc/gunicorn.conf  /etc/gunicorn.d/test
sudo /bin/ln -sf /home/box/web/ask/ask.gunicorn.conf  /etc/gunicorn.d/ask
sudo /etc/init.d/gunicorn restart

#cd /home/box/web
#gunicorn -b 0.0.0.0:8080 web.hello:application -D

sudo /bin/ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/test.conf
sudo /etc/init.d/nginx restart
