30second-serverspec
========================

Getting started with serverspec... FAST!

*What is server-spec*

With <http://serverspec.org/>, you can write RSpec tests for checking your servers are configured correctly.

How to use
-------------

Build the docker container

	$ docker build -t serverspec .

Start the contain and check the status/spec of the current system.

	$ docker run -it serverspec bash
	# cd /serverspec
	# rake spec
	...
	rspec ./spec/localhost/httpd_spec.rb:4 # Package "nginx" should be installed
	rspec ./spec/localhost/httpd_spec.rb:8 # Service "nginx" should be enabled
	rspec ./spec/localhost/httpd_spec.rb:9 # Service "nginx" should be running
	rspec ./spec/localhost/httpd_spec.rb:13 # Port "80" should be listening
	rspec ./spec/localhost/httpd_spec.rb:17 # File "/etc/nginx/sites-enabled/default" should be file
	rspec ./spec/localhost/httpd_spec.rb:18 # File "/etc/nginx/sites-enabled/default" should contain "server_name localhost"

As you can see there are a few errors that serverspec has found on the system.

Install nginx and start the service.

    # apt-get install -y nginx
	# service nginx start


Once completed we can check the status of the server again with server spec

    # rake spec
	/usr/bin/ruby1.9.1 -S rspec spec/localhost/httpd_spec.rb
	......
	Finished in 0.22004 seconds
	6 examples, 0 failures

Explore the solution
-------------------------

Lets kill nginx and re-run serverspec

    # pkill nginx
	# rake spec
	rspec ./spec/localhost/httpd_spec.rb:9 # Service "nginx" should be running
	rspec ./spec/localhost/httpd_spec.rb:13 # Port "80" should be listening

Awesome :)

