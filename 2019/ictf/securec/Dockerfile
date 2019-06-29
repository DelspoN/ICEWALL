FROM       ubuntu:18.04
MAINTAINER delsponn@gmail.com

# Environment
ENV user=securec

# add user && config
RUN useradd -m -d /home/$user/ -s /bin/bash $user
RUN echo "$user     hard    nproc   20" >> /etc/security/limits.conf
RUN mkdir /home/$user/tmp

# update && install xinetd
RUN apt-get update
RUN apt-get install -y xinetd python gcc-5-arm-linux-gnueabi qemu-user-static

# COPY
COPY ./run.py /home/$user/run.py
COPY ./perfect /home/$user/perfect
COPY ./xinetd_conf /etc/xinetd.d/xinetd_conf

RUN cp -r /usr/arm-linux-gnueabi/lib /home/$user
RUN cp /usr/bin/qemu-arm-static /home/$user

# apply permissions
RUN chown -R root:$user /home/$user
RUN chmod -R 750 /home/$user
RUN chmod 770 /home/$user/tmp

# EXPOSE
EXPOSE 1000

# CMD
CMD ["/usr/sbin/xinetd", "-d"]
