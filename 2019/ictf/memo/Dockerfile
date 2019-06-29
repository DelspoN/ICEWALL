FROM ubuntu:18.04
RUN apt update
RUN apt install xinetd -y
RUN apt install libc6-dev-i386 -y
RUN useradd -mU memo
COPY ./home /home/memo
COPY ./xinetd /etc/xinetd.d/memo
RUN chmod 750 /home/memo /home/memo/memo
RUN chmod 440 /home/memo/flag
RUN chown -R root:memo /home/memo
CMD ["/usr/sbin/xinetd","-dontfork"]
