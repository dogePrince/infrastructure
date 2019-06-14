enter to container:
docker run -it --rm -v $PWD:/vault_deployer ansible_base:latest bash

init environment:
source /etc/profile

ansible-playbook playbook.yaml
