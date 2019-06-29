FROM ubuntu:xenial
RUN apt update
RUN apt -y upgrade
RUN DEBIAN_FRONTEND=noninteractive apt -y install apache2 libapache2-mod-php5 php5-mysql php5-gd php-pear php-apc php5-curl php5-ldap curl lynx-cur mysql-server
EXPOSE 80
