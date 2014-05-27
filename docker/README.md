30 seconds intro to docker
==============================================

Quick start in learning docker

What will you learn
-----------------------

How to use docker to to install the hello package and create a file in /tmp
called helloworld


Getting started
-------------------

Compile/Build the Dockerfile into a new machine image

	$ docker build -t docker .

Start the machine

	$ docker run -it docker

Check the hello package and /tmp/helloworld is on the system.

	# dpkg -l hello
	# cat /tmp/helloworld


Important files
------------------

*Dockerfile*

This is the file the docker in order to create a new linux container.
