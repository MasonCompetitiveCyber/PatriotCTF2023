FROM ubuntu:latest

ENV DEBIAN_FRONTEND=noninteractive

LABEL maintainer="sauman"

LABEL name="check"

RUN apt update -y \
    && apt install php -y \
    && apt install apache2 -y \
    && apt install supervisor -y


# Switch working environment
WORKDIR /var/www/html

# COPY challenge
COPY challenge .

# Changing Ownership
RUN chown -R www-data: /var/www/html

# Setup apache2 
COPY config/checker.conf /etc/apache2/sites-available


RUN service apache2 start \
    && a2dissite 000-default \
    && a2ensite checker 

EXPOSE 80

CMD ["/usr/sbin/apache2ctl","-DFOREGROUND"]
