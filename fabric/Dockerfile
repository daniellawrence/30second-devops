FROM ubuntu:14.04

RUN apt-get update
RUN apt-get install -y python python-pip
RUN apt-get install -y python-dev
RUN pip install fabric
RUN mkdir /fabric
ADD fabfile.py /fabric/fabfile.py
CMD /bin/bash
