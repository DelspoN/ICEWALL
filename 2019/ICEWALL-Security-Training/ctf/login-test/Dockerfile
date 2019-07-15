FROM       ubuntu:16.04
MAINTAINER delsponn@gmail.com

# Environment
ENV user=webuser

# add user && config
RUN useradd -m -d /home/$user/ -s /bin/bash $user
RUN echo "$user     hard    nproc   20" >> /etc/security/limits.conf

# update && install xinetd
RUN apt-get update
RUN apt-get install -y nginx php-fpm php-mysql

# Set MySQL account
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y mysql-server

# COPY
COPY ./default /etc/nginx/sites-available/default
COPY ./start.sh /start.sh
COPY ./set.sql /set.sql

# apply permissions
RUN chown -R root:$user /home/$user
RUN chmod -R 750 /home/$user
RUN chmod +x /start.sh

# EXPOSE
EXPOSE 80

# CMD
CMD ["/start.sh"]
