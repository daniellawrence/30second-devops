FROM debian:latest

RUN apt update
RUN apt install -y fabric
RUN mkdir /fabric
ADD fabfile.py /fabric/fabfile.py
CMD /bin/bash
