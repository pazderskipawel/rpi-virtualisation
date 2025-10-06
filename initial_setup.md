# Initial setup: QEMU/KVM on Raspberry Pi

This document walks through the initial steps to install and validate QEMU/KVM and libvirt on a Raspberry Pi (RPi 5 or similar arm64 device). It covers package installation, service setup, basic verification

It's planned to move it to CICD to automate installation on Raspberries

## 1. Fully update the OS

```bash
sudo apt update && sudo apt full-upgrade -y
sudo reboot
```

Rebooting ensures any new kernel or firmware updates are active.

## 2. Verify architecture and KVM availability

Check the CPU architecture (should be `aarch64` for a 64-bit OS):

```bash
uname -m
# expected output: aarch64
```

Check for the KVM device node:

```bash
ls -l /dev/kvm
# If present, you'll see /dev/kvm; if not, KVM may not be enabled in the kernel or the kernel lacks KVM support
```

If `/dev/kvm` is missing, check dmesg and kernel modules:

```bash
dmesg | grep -i kvm
uname -a
# You may need a newer kernel or vendor kernel config that enables KVM on your board.
```

## 3. Install QEMU, libvirt and management tools

Install the common packages (Debian/Ubuntu example):

```bash
sudo apt install -y qemu-system-aarch64 qemu-utils libvirt-daemon-system libvirt-clients virtinst virt-manager bridge-utils cloud-image-utils
```
What these packages provide:
- `qemu-system-aarch64` / `qemu-utils`: QEMU emulator and helpers for aarch64 guests
- `libvirt-daemon-system` / `libvirt-clients`: libvirt daemon and CLI tools (`virsh`)
- `virtinst`: CLI helper to create VMs (`virt-install`)
- `virt-manager`: GUI VM manager (optional)
- `cloud-image-utils`: tools for preparing cloud images and working with cloud-init

## 4. Enable and start libvirt

```bash
sudo systemctl enable --now libvirtd
systemctl status libvirtd
```

## 5. Add your user to the libvirt group

So you can manage VMs without sudo:

```bash
sudo usermod -aG libvirt $USER
# Log out and log back in (or restart the SSH session) for group changes to take effect
```

Verify libvirt access:

```bash
virsh list --all
```

## 6. Validate the host for virtualization

Run the libvirt validation tool:

```bash
sudo virt-host-validate
```

The tool will report common issues (missing kernel modules, permissions, etc.).