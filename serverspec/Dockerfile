FROM ubuntu:14.04

RUN apt-get update
RUN apt-get install -y ruby ruby-dev
RUN gem install --verbose serverspec rake
ADD serverspec /serverspec
ADD fix-it.sh /usr/bin/fix-it.sh
