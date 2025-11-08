# rpi-virtualisation

Create and manage virtual machines and containers on a Raspberry Pi (RPi 5)


## Overview

This repository documents and contains supporting material for running virtual machines on a Raspberry Pi 5 (8GB) with an attached SSD. The goal is to have a reproducible, automated environment for provisioning and managing VMs and their networking using infrastructure-as-code tools.

## Current Hardware

- Raspberry Pi 5 (8 GB)
- Official Raspberry Pi NVMe/M.2 SSD expansion board (official SSD HAT) — e.g. NVMe M.2 drive (256 GB)

## Software stack

- Raspberry Pi OS (or a Debian-based distribution for arm64)
- Ansible, Docker
- GitHub Actions runner (optional, for running simple pipeline)

## Planned architecture
Github Projcet for this repo - [LINK](https://github.com/users/pazderskipawel/projects/1) 

## Current architecture
GITHUB ACTIONS:
  - CICD:
    - checks out code
    - runs playbook which runs docker and qemu
  - [![Deploy app to Pi](https://github.com/rpi-automation/rpi-automation-infra-ansible/actions/workflows/deploy_to_pi.yml/badge.svg?branch=main)](https://github.com/rpi-automation/rpi-automation-infra-ansible/actions/workflows/deploy_to_pi.yml)
  
RPI:
  - ANSIBLE (managing raspberry itself):

    Roles tasks:
    - raspberry:
      - updates apt packages
    - qemu:
      - Prepares and starts qemu, libvrt
      - shared task to create new vm
      - shared task to create vm network
    - docker:
      - installs and runs docker and docker compose
    - nginx: 
      - runs docker container with network mode: host to controll networking
      - shared task to add new service config file to nginx
    - klipper (managing 3d printer form RPI):
      - playbook to run docker copose from file with services managing 3d-printer (klipper/mooraker/fliudd)
      - config file for nginx (applied using shared nginx task)
    - [cockpit](https://cockpit-project.org/applications) (Web-based interface for managing servers):
      - UI app to manage server config, containers and vms
      - config file for nginx (applied using shared nginx task)
    - home assistant container
      - runs container with haos and copies configs
    - home assistant vm - old
      - playbook which downloads image and runs qemu tasks to create vm and network
      - file with network configuration for vm
    - samba - allows creating network disk mount to specific files in pi
    - vpn - remote access to rpi using WireGuard
    - ufw - firewall to block unused ports

## Current netwokring
```
WireGuard VPN -> rpi_ipv6:51820 -> remote access for anything below


PC              Raspberry Pi
rpi_ip:8080 --> nginx --> localhost:8081 --> docker --> :80 on fluidd container

rpi_ip:9090 --> localhost:9090 --> cockpit service

rpi_ip:8123 --> :8123 on haos container

samba directories:
\\rpi_ip\directory_name --> :445 --> smb.conf --> /directory_name in docker container --> /shared_directory

\\rpi_ip\gcodes -> /actions-runner/files/printer_data/gcodes

\\rpi_ip\wireguard -> /actions-runner/files/wg-peers (directory containing only config files for peer)
```