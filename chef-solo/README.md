30 seconds intro to standalone puppet
==============================================

Quick start in learning chef-solo within a docker container.

What will you learn
-----------------------

A quick an dirty way to install the hello package and create a file in /tmp
called helloworld


Getting started
-------------------

    $ docker build -t chef-solo .
    $ docker run -it chef-solo bash
    # chef-solo
	# dpkg -l hello
	# cat /tmp/helloworld


 Important files
------------------

*default.rb*

This is the file that chef-solo is going to use to alter your system.
Its a very simple example of installing a package called *hello* and writing a
file into */tmp/helloworld*.


Why does it take longer than 30 seconds to build the docker container
---------------------------------------------------------------------

ummm, the 30seconds counter is started after the docker container is built!


How do I make simple changes while learning chef ?
--------------------------------------------------

You can just edit the `/chef/cookbooks/helloworld/recipes/default.rb` file 
for now, while inside the docker container.

Where are the Key files?
------------------------

* /etc/chef/solo.rb
* /chef/cookbooks/helloworld/recipes/default.rb
* /chef/node.json

Did it work?
------------

    # chef-solo
    Starting Chef Client, version 11.12.4
    Compiling Cookbooks...
    Converging 1 resources
    Recipe: helloworld::default
      * file[/tmp/helloworld.txt] action create
        - create new file /tmp/helloworld.txt
        - update content in file /tmp/helloworld.txt from none to dffd60
            --- /tmp/helloworld.txt	2014-05-19 14:31:41.663134765 +0000
            +++ /tmp/.helloworld.txt20140519-10-1prltu5	2014-05-19 14:31:41.663134765 +0000
            @@ -1 +1,2 @@
            +Hello, World!
        - change mode from '' to '0544'
        - change owner from '' to 'root'
        - change group from '' to 'root'
      * package[hello] action install
        - install version 2.8-4 of package hello
     Running handlers:
     Running handlers complete
     Chef Client finished, 1/1 resources updated in 1.442621537 seconds
