docker build . -t ansible_base

docker run -it --rm -v $PWD:/xxx ansible_base bash

source /etc/profile
export VAULT_ADDR=https://example.com
vault login -method=ldap username=yourname
vault read

export VAULT_ADDR=https://vault.aws.autodesk.com
