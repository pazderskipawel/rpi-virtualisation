#!/usr/bin/env bash

SCRIPT_NAME=$(basename "$0")
EXPECTED_LINE='config file = /home/rpi/actions_repos/rpi-virtualisation/rpi-virtualisation/ansible/ansible.cfg'

usage() {
    cat <<EOF
Usage: $SCRIPT_NAME [check|install]

check   - Verify Ansible is installed and reports expected config file
install - Install Ansible globally via apt
EOF
}

check_installed() {
    if ! command -v ansible >/dev/null 2>&1; then
        echo "Ansible binary not found"
        return 2
    fi

    if ansible --version 2>&1 | grep -qF "$EXPECTED_LINE"; then
        echo "Ansible reports expected config file"
        return 0
    else
        echo "Ansible does not report the expected config file"
        return 3
    fi
}

do_install() {
    echo "Installing Ansible via apt"
    sudo apt-get update && sudo apt-get upgrade -y
    sudo apt-get install -y ansible

    if command -v ansible >/dev/null 2>&1; then
        echo "Ansible installed successfully"
        ansible --version
        return 0
    else
        echo "Ansible installation failed" >&2
        return 1
    fi
}

if [[ $# -ne 1 ]]; then
    usage
    exit 64
fi

case "$1" in
    check) check_installed ;;
    install) do_install ;;
    -h|--help) usage ;;
    *)
        echo "Unknown command: $1" >&2
        usage
        exit 64
        ;;
esac
