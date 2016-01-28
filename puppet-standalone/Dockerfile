FROM ubuntu:14.04

RUN apt-get update
RUN apt-get install -y ruby
RUN gem install --verbose puppet
RUN mkdir /puppet
ADD helloworld.pp /puppet/helloworld.pp

CMD /bin/bash
