FROM ubuntu:14.04

MAINTAINER Daniel Lawrence <dannyla@linux.com>

RUN apt-get install -y wget
RUN wget https://opscode-omnibus-packages.s3.amazonaws.com/ubuntu/13.04/x86_64/chef_11.12.4-1_amd64.deb
RUN dpkg -i chef_11.12.4-1_amd64.deb
RUN mkdir -p /chef/cookbooks/helloworld/recipes/ /etc/chef

ADD default.rb /chef/cookbooks/helloworld/recipes/default.rb
ADD node.json /chef/node.json
ADD solo.rb /etc/chef/solo.rb
ADD README.md /README.md