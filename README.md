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
