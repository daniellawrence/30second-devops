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
	# service ssh start
	# ansible-playbook -i /ansible/inventory.ini /ansible/playbook.yaml
	# dpkg -l hello
	# cat /tmp/helloworld


Important files
------------------

*playbook.yaml*

This is the file that ansible is going to use to alter your system.
Its a very simple example of installing a package called *hello* and writing a
file into */tmp/helloworld*.

*inventory.ini*

This is the list of systems that the playbook can be applied too.
Howerver, It is more than a list of hosts as it can be used to configure information about
how we connect to the hosts. In this example we are using a local connection not an SSH connection.

Why does it take longer than 30 seconds to build the docker container
---------------------------------------------------------------------

ummm, the 30seconds counter is started after the docker container is built!

Did it work?
---------------

```
$ ansible-playbook -i /ansible/inventory.ini /ansible/playbook.yaml

PLAY [localhost] ************************************************************** 

GATHERING FACTS *************************************************************** 
ok: [localhost]

TASK: [Install hello package] ************************************************* 
changed: [localhost]

TASK: [Create /tmp/helloworld] ************************************************ 
changed: [localhost]

PLAY RECAP ******************************************************************** 
localhost                  : ok=3    changed=2    unreachable=0    failed=0   

root@4d3c44acb0ad:/# 
```
