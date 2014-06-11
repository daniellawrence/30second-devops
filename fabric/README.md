30 seconds intro to fabric
==============================================

Quick start in learning fabric in a brand new environment.

What will you learn
-----------------------

A quick an dirty way to install the hello package and create a file in /tmp
called helloworld


Getting started
-------------------

	$ docker build -t fabric .
	$ docker run -it fabric
	# cd /fabric
	# fab hello
	# dpkg -l hello
	# cat /tmp/helloworld


Important files
------------------

*fabric.py*

This file contains 3 functions, 2 hidden functions
- one to install the package
- one to create the text file
It also contains wrapper function that is exposed to the user that will
call the other two functions.


Why does it take longer than 30 seconds to build the docker container
---------------------------------------------------------------------

ummm, the 30seconds counter is started after the docker container is built!

Did it work?
---------------

    # fab hello
	[localhost] local: apt-get install -y hello
	Reading package lists... Done
	Building dependency tree       
	Reading state information... Done
	The following NEW packages will be installed:
	hello
	0 upgraded, 1 newly installed, 0 to remove and 0 not upgraded.
	Need to get 28.1 kB of archives.
	After this operation, 111 kB of additional disk space will be used.
	Get:1 http://archive.ubuntu.com/ubuntu/ trusty/main hello amd64 2.8-4 [28.1 kB]
	Fetched 28.1 kB in 5s (4835 B/s)
	Selecting previously unselected package hello.
	(Reading database ... 18323 files and directories currently installed.)
	Preparing to unpack .../archives/hello_2.8-4_amd64.deb ...
	Unpacking hello (2.8-4) ...
	Setting up hello (2.8-4) ...
	[localhost] local: echo 'Hello World!' > /tmp/helloworld
	Done.
