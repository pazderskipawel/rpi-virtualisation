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

## Main directories

### ansible

This repository contains Ansible playbooks and roles designed to automate the infrastructure setup and configuration of Raspberry Pi devices. 

#### ansible roles 

* alerts - alertmanager/prometheus/cadvisor - alerting services (wip)
* cockpit - gui for debian based servers for "easier" rpi management
* cypress - docker container for running automated tests (wip)
* dns - dnsmasq conrtainer - dns server for services
* docker - docker services, contains reusable tasks for other container roles
* firewall - ufw service
* haos - home assistant container
* n8n - n8n automation tool
* notes - 2 contaiiners - joplin server for synchrinising notes, excalidraw for creating hand written notes
* octoprint - managing 3d printer using raspberrypi
* reverse-proxy - traefik container, manages domains for each service
* samba - samba service for accessing choosed directories uising windows network drives
* vpn - wireguard vpn to access rpi outside local network

### services-n8n

This repository hosts the configuration and workflows for deploying n8n, a powerful open-source workflow automation tool.

### archive

Repository for all no longer used services, components. Maybe they'll be needed someday...

#### archived services

* haos_vm_old - Home assistant Virtual Machine (now using container instead of VM)
* klipper_old - 3d printer services (klipper/moonraker/fluidd) (now using octoprint)
* nginx - used mainly for reverse proxy (now using traefik)
* qemu - vm hypervisor services (not used for now)

## Project Goals

* Simplify Raspberry Pi infrastructure provisioning through Ansible automation.
* Enable local and reliable workflow automation using n8n.
* Reduce manual configuration and increase operational efficiency.

### Feel free to explore the repositories, contribute, and share your feedback!

## Changelog

* 18.12.2025 - rpi-automation - merged everything into one repository, started migrating to codeberg
* 17.12.2025 - ansible - Added DNS (dnsmasq container for managing traefik domains without need to use hosts file), Simplified CICD
* 14.12.2025 - ansible - Added (/returned to) traefik for all devices (was experimenting on custom url for each service but domains were better to maintain)
* 08.12.2025 - archive - Created Repository for no longer used services
* 06.12.2025 - ansible - Changed 3d printer software from klipper,moonraker,fluidd combo to octoprint
* 30.11.2025 - ansible - Added Zigbee bridge to Home Assistant
* 25.11.2025 - ansible - Added notes services - Joplin server (for notes synchronisation), exclaidraw (hand writing, painting)
* 20.11.2025 - ansible - Added HACS extention for Home Assistant container
* 17.11.2025 - ansible - Added cypress container for future automated tests
* 12.11.2025 - ansible - Added alerting services for future use (prometheus, alertmanager, cadvisor)
* 08.11.2025 - ansible - Migrated Home Assitant from VM to contenerised version 
* 03.11.2025 - n8n-workflows - added repository which stores n8n workflows
* 03.11.2025 - rpi-automation - moved repository to it's own github organisation for better maintanance of whole project, created prpject to better track of issues
* 03.11.2025 - ansible - Added n8n container and setup
* 30.10.2025 - ansible - Modified CI slightly
* 29.10.2025 - ansible - Added VPN container (wireguard)
* 27.10.2025 - ansible - Added firewall (ufw)
* 23.10.2025 - ansible - Added playbook which automatically completes onboarding setup for Home assistant
* 22.10.2025 - ansible - Added Samba container
* 18.10.2025 - ansible - Added Nginx container setup, and removed traefik form klipper
* 17.10.2025 - ansible - Created playbook for Home Assistant VM, Created playybooks for remote managing my 3d printer (klipper, moonraker, fluidd)
* 16.10.2025 - ansible - Added Cockpit UI for easier RaswpberryPi system management and added 3rd party extension for docker containers management, created issues for this repository
* 13.10.2025 - ansible - Created fiirst ansible roles for docker containers and quemu VMs with simple Github Actions CI
* 05.10.2025 - ansible - Created infra-ansible repository
