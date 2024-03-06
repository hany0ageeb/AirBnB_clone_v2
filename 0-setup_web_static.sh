#!/usr/bin/env bash
# Bash script that sets up your web servers for the deployment of web_static
apt-get update
apt-get install nginx -y
if [ ! -d "/data" ]; then
	mkdir /data
fi
if [ ! -d "/data/web_static/" ]; then
	mkdir /data/web_static
fi
if [ ! -d "/data/web_static/releases/" ]; then
	mkdir /data/web_static/releases
fi
if [ ! -d "/data/web_static/shared/" ]; then
	mkdir /data/web_static/shared/
fi
if [ ! -d "/data/web_static/releases/test/" ]; then
	mkdir /data/web_static/releases/test/
fi
printf "<html>\n<head>\n<title>fake HTML file</title>\n</head>\n<body>\nHolberton School\n</body>\n<html>\n" > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu:ubuntu /data/
printf "server {\nlisten 80 default_server;\nlisten [::]:80 default_server;\nroot /var/www/html;\nserver_name _;\nlocation / {\n\ttry_files \$uri \$uri/ =404;\n}\nlocation /hbnb_static {\n\talias /data/web_static/current/;\n}\n}\n" > /etc/nginx/sites-enabled/default
service nginx restart
