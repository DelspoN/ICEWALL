FROM       ubuntu:16.04
MAINTAINER delsponn@gmail.com

# Environment
ENV user=webuser

# add user && config
RUN useradd -m -d /home/$user/ -s /bin/bash $user
RUN echo "$user     hard    nproc   20" >> /etc/security/limits.conf

# update && install xinetd
RUN apt-get update
RUN apt-get install -y nginx php-fpm

# COPY
COPY ./default /etc/nginx/sites-available/default
COPY ./flag /flag
COPY ./start.sh /start.sh

# apply permissions
RUN chown -R root:$user /home/$user
RUN chmod -R 750 /home/$user
RUN chmod 444 /flag
RUN chmod +x /start.sh

# EXPOSE
EXPOSE 80

# CMD
CMD ["/start.sh"]
