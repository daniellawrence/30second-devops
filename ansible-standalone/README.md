30 seconds intro to standalone ansible
===============================================

Quick start in learning ansible in a brand new environment.

What will you learn
-----------------------

A quick an dirty way to install the hello package and create a file in /tmp
called helloworld


Getting started
-------------------

	$ docker build -t ansible-standalone .
	$ docker run -it ansible-standalone
	# ansible-playbook -i /ansible/inventory.ini /ansible/playbook.yaml
	# dpkg -l hello
	# cat /tmp/helloworld


Important files
------------------

*playbook.yaml*

This is the file that ansible is going to use to alter your system.
Its a very simple example of installing a package called *hello* and writing a
file into */tmp/helloworld*.


Why does it take longer than 30 seconds to build the docker container
---------------------------------------------------------------------

ummm, the 30seconds counter is started after the docker container is built!

Did it work?
---------------

	
