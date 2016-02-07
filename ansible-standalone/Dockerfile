FROM debian:latest

RUn apt update
RUN apt install -y openssh-server
RUN apt install -y ansible

RUN ssh-keygen -t rsa -N "" -f /root/.ssh/id_rsa
RUN cp /root/.ssh/id_rsa.pub /root/.ssh/authorized_keys

RUN mkdir /ansible
ADD playbook.yaml /ansible/playbook.yaml
ADD inventory.ini /ansible/inventory.ini

CMD bash
