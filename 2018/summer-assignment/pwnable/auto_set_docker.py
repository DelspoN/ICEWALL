import subprocess

Dockerfile = """
FROM       ubuntu:16.04
MAINTAINER delsponn@gmail.com

# Environment
ENV user={prob}

# add user && config
RUN useradd -m -d /home/$user/ -s /bin/bash $user
RUN echo "$user     hard    nproc   20" >> /etc/security/limits.conf

# update && install xinetd
RUN apt-get update
RUN apt-get install -y xinetd python

# run 32-bit binary
RUN apt-get install libc6-i386

# COPY
COPY ./{prob} /home/$user/{prob}
COPY ./flag /home/$user/flag
COPY ./xinetd_conf /etc/xinetd.d/xinetd_conf

# apply permissions
RUN chown -R root:$user /home/$user
RUN chmod -R 750 /home/$user
RUN chmod 440 /home/$user/flag

# EXPOSE
EXPOSE {port}

# CMD
CMD ["/usr/sbin/xinetd", "-d"]
"""

xinetd_conf ="""
service {prob}
{
    disable = no
    socket_type = stream
    protocol    = tcp
    wait        = no
    user        = {prob}
    bind        = 0.0.0.0
    server      = /home/{prob}/{prob}
    type        = UNLISTED
    port        = {port}
}
"""

dockerrun = """
#!/bin/sh

docker run --name {prob} -dt -p {port}:{port} {prob}
"""

dockerbuild = """
#!/bin/sh

docker build -t {prob} .
"""

for i in range(3):
	prob = "pwn%d" % i
	port = str(1000 + i)
	path = "./" + prob
	with open(path + "/Dockerfile", "w") as f:
		f.write(Dockerfile.replace("{prob}", prob).replace("{port}", port))
	
        with open(path + "/xinetd_conf", "w") as f:
                f.write(xinetd_conf.replace("{prob}", prob).replace("{port}", port))

        with open(path + "/dockerrun.sh", "w") as f:
                f.write(dockerrun.replace("{prob}", prob).replace("{port}", port))

        with open(path + "/dockerbuild.sh", "w") as f:
                f.write(dockerbuild.replace("{prob}", prob).replace("{port}", port))

	print subprocess.check_output(["chmod","775",path+"/dockerbuild.sh"])
        print subprocess.check_output(["chmod","775",path+"/dockerrun.sh"])
