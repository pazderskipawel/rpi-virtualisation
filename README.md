# rpi-virtualisation

Create and manage virtual machines on a Raspberry Pi (RPi 5) using QEMU and libvirt.

## Overview

This repository documents and contains supporting material for running virtual machines on a Raspberry Pi 5 (8GB) with an attached SSD. The goal is to have a reproducible, automated environment for provisioning and managing VMs and their networking using infrastructure-as-code tools.

## Hardware

- Raspberry Pi 5 (8 GB)
- Official Raspberry Pi NVMe/M.2 SSD expansion board (official SSD HAT) — e.g. NVMe M.2 drive (256 GB)

## Software stack

- Raspberry Pi OS (or a Debian-based distribution for arm64)
- QEMU
- libvirt (libvirtd)
- Optional tooling (planned): Ansible, Terraform, CI/CD tooling

## Goals / Planned work

- Use Ansible for VM and host configuration management
- Use Terraform to declare and manage VM instances, networks, and storage
- Add CI/CD pipelines to validate and automate builds and deployments
- Document tuning and performance notes for KVM/QEMU on Raspberry Pi

## Prerequisites

On a fresh Raspberry Pi OS (64-bit) install, ensure you have:

- Sufficient disk space on the SSD
- A non-root user with sudo privileges
- A network connection (for package installs and optional remote management)

- If you're using the official Raspberry Pi SSD board, ensure the board and M.2 drive are properly seated and that any required firmware/kernel updates are applied. Some boards may need extra power or cooling under sustained load.