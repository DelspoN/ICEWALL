FROM ubuntu:18.04
RUN apt update
RUN apt install xinetd -y
RUN apt install libc6-dev-i386 -y
RUN useradd -mU format
COPY ./home /home/format
COPY ./xinetd /etc/xinetd.d/format
RUN chmod 750 /home/format /home/format/format
RUN chown -R root:format /home/format

RUN chmod 777 /home/format/flag
CMD ["/usr/sbin/xinetd","-dontfork"]
