# minikube-playground

## Setup (Minikube on Ubuntu 18.04)
```
sudo apt-get update
sudo apt-get install -y docker.io
sudo apt-get update
sudo apt-get install -y apt-transport-https ca-certificates curl software-properties-common
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo add-apt-repository "deb https://download.docker.com/linux/$(. /etc/os-release; echo "$ID") $(lsb_release -cs) stable"
sudo apt-get update
sudo apt-get install docker-ce=18.06.0~ce~3-0~ubuntu
curl -Lo minikube https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64 && chmod +x minikube && sudo mv minikube /usr/local/bin/
```

## Usage
```
sudo minikube start --vm-driver none

sudo chown -R ${USER} ${HOME}/.kube
sudo chgrp -R ${USER} ${HOME}/.kube
sudo chown -R ${USER} ${HOME}/.minikube
sudo chgrp -R ${USER} ${HOME}/.minikube

kubectl proxy --address=0.0.0.0 --accept-hosts='.*'
minikube dashboard
```


## Help
```
# get secret token
export K8S_TOKEN=$(kubectl describe secret $(kubectl get secrets | grep default | awk '{print $1}' | tail -n 1 | awk '{print $1}') | tail -n 1 | awk '{print $2}')
```
