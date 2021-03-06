FROM ubuntu:latest
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y apache2 \
    apache2-dev \
    mysql-client \
    mysql-server \
    python3 \
    python3-dev \
    python3-pip 

COPY ./app/requirements.txt /var/www/FlaskApp/app/requirements.txt
RUN pip3 install -r /var/www/FlaskApp/app/requirements.txt

COPY ./FlaskApp.conf /etc/apache2/sites-available/FlaskApp.conf
RUN mod_wsgi-express module-config >> /etc/apache2/mods-available/wsgi.load

RUN a2enmod wsgi
RUN a2ensite FlaskApp

COPY ./FlaskApp.wsgi /var/www/FlaskApp/FlaskApp.wsgi
COPY ./app /var/www/FlaskApp/app/

RUN a2dissite 000-default.conf
RUN a2ensite FlaskApp.conf

EXPOSE 80
CMD apachectl -D FOREGROUND