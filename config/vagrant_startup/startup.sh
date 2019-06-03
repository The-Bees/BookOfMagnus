#!/usr/bin/env bash

# Link vagrant src code to user
sudo ln -s /vagrant/src/ /home/vagrant/src

# apt-get update
sudo apt-get update
# install python-pip
sudo apt-get install --upgrade -y \
    python-pip

# pip install virtualenv
sudo pip install virtualenv

# set up virtualenv
virtualenv -p python3 venv
source venv/bin/activate

pip install -r /vagrant/config/requirements.txt
