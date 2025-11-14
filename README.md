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
  
RPI services:

- WireGuard VPN (HOST)
  rpi_ipv6:51820 -> remote access for anything below

- Nginx (DOCKER)(used for reverse proxy if needed)

- 3D Printer management (DOCKER COMPOSE)
  - Klipper (printer firmware)
  - Moonraker (API for klipper)
  - Fluidd (web interface)

    rpi_ip:8080 --> nginx (reverse proxy) --> localhost:8081 --> docker --> :80 on fluidd container

- Cockpit service (HOST) (GUI for managing raspberry pi)

  rpi_ip:9090 --> localhost:9090 --> cockpit service

- Home assistant (DOCKER)

  rpi_ip:8123 --> :8123 on haos container

- N8N (DOCKER) automation service

  rpi_ip:5678 --> :5678 on n8n container

- Alerting services (DOCKER COMPOSE):
  - Prometheus: 

    rpi_ip:9091 --> :9090 on prometheus container

  - alertmanager:

    rpi_ip:9093 --> :9093 on alertmanager container

  - CAdvisor:

    rpi_ip:8082 --> :8080 on cadvisor container

- Samba (HOST) - create and manage network disk for windows

  current directories:
  - \\rpi_ip\directory_name --> :445 --> smb.conf --> /directory_name in docker container --> /shared_directory

  - \\rpi_ip\gcodes -> /actions-runner/files/printer_data/gcodes

  - \\rpi_ip\wireguard -> /actions-runner/files/wg-peers (directory containing only config files for peer)