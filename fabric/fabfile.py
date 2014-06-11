#!/usr/bin/env python
# ----------------------
from fabric.api import task, local


def install_hello():
    " Install the hello package on the system "
    local("apt-get install -y hello")


def helloworld_file():
    " Create a file /tmp/helloworld that greets the world"
    local("echo 'Hello World!' > /tmp/helloworld")


@task
def hello():
    "Install hello package and create helloworld file"
    install_hello()
    helloworld_file()
