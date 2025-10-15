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

## Current architecture
GITHUB ACTIONS:
  - CICD:
    - checks out code
    - runs playbook which runs docker and qemu
  - [![Deploy app to Pi](https://github.com/pazderskipawel/rpi-virtualisation/actions/workflows/deploy_to_pi.yml/badge.svg?branch=main)](https://github.com/pazderskipawel/rpi-virtualisation/actions/workflows/deploy_to_pi.yml)
  
RPI:
  - ANSIBLE (managing raspberry itself):
    - raspberry:
      - updates apt
    - qemu:
      - Prepares and starts qemu, libvrt
    - docker:
      - installs and runs docker and docker compose
    - klipper:
      - runs docker copose with services managing 3d-printer
  - DOCKER:
    - compose file for managing 3d printer 
## Planned architecture
RPI:
- ANSIBLE: 
  - haos
    - setup and run Home Assistant OS VM
    - default task for managing existing VMs
- DOCKER:
  - some kind of ui for managing VMs and containers (Ansible Semaphore probably)
  - VPN to be able to connect to RPI remotelly (WireGuard probably)
  - SMB or FTP server