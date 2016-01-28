FROM ubuntu:14.04

RUn apt-get update
RUN apt-get install -y python-pip python-dev openssh-server
RUN pip install ansible

RUN ssh-keygen -t rsa -N "" -f /root/.ssh/id_rsa
RUN cp /root/.ssh/id_rsa.pub /root/.ssh/authorized_keys

RUN mkdir /ansible
ADD playbook.yaml /ansible/playbook.yaml
ADD inventory.ini /ansible/inventory.ini

CMD bash
