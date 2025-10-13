#!/bin/bash

cd /home/rpi/actions_repos/rpi-virtualisation/rpi-virtualisation/

sudo apt-get update && sudo apt-get upgrade -y

sudo apt-get install -y ansible

if command -v ansible &> /dev/null; then
    ansible --version
else
    exit 1
fi