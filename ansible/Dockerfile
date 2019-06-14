FROM ubuntu:latest

RUN apt-get update -qq
RUN apt-get install -y ansible
RUN apt-get install -y git
RUN apt-get install -y python-pip
RUN apt-get install -y curl
RUN apt-get install -y unzip
RUN apt-get install -y sshpass

RUN curl https://releases.hashicorp.com/vault/1.1.0/vault_1.1.0_linux_amd64.zip > vault_1.1.0_linux_amd64.zip
RUN unzip vault_1.1.0_linux_amd64.zip -d vault
RUN rm vault_1.1.0_linux_amd64.zip
RUN echo 'export PATH=$PATH:/vault' >> /etc/profile

RUN pip install hvac
RUN pip install hvac[parser]
RUN pip install pywinrm
