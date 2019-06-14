FROM ansible_base:latest

RUN apt-get install -y net-tools

RUN curl https://releases.hashicorp.com/vault/1.1.0/vault_1.1.0_linux_amd64.zip > vault_1.1.0_linux_amd64.zip
RUN unzip vault_1.1.0_linux_amd64.zip -d vault
RUN rm vault_1.1.0_linux_amd64.zip
RUN echo 'export PATH=$PATH:/vault' >> /etc/profile
