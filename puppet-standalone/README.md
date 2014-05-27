30 seconds intro to standalone puppet
==============================================

Quick start in learning puppet in a brand new environment.

What will you learn
-----------------------

A quick an dirty way to install the hello package and create a file in /tmp
called helloworld


Getting started
-------------------

	$ docker build -t puppet-standalone .
	$ docker run -it puppet-standalone
	# puppet apply /puppet/helloworld.pp
	# dpkg -l hello
	# cat /tmp/helloworld


Important files
------------------

*helloworld.pp*

This is the file that puppet is going to use to alter your system.
Its a very simple example of installing a package called *hello* and writing a
file into */tmp/helloworld*.


Why does it take longer than 30 seconds to build the docker container
---------------------------------------------------------------------

ummm, the 30seconds counter is started after the docker container is built!

Did it work?
---------------

	# puppet apply helloworld.pp 
	Notice: Compiled catalog for c25bcca4dc19.home.gateway in environment production in 0.25 seconds
	Notice: /Stage[main]/Main/File[/tmp/helloworld]/ensure: defined content as '{md5}xxx'
	Notice: /Stage[main]/Main/Package[hello]/ensure: ensure changed 'purged' to 'present'
	Notice: Finished catalog run in 11.10 seconds
	
