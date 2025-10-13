#!/usr/bin/bash
SCRIPT_NAME=$(basename "$0")
EXPECTED_LINE='config file = /home/rpi/actions_repos/rpi-virtualisation/rpi-virtualisation/ansible/ansible.cfg'

usage() {
    cat <<EOF
$SCRIPT_NAME [check|install]

check   - verify ansible is installed and reports expected config file
install - install ansible globally via apt
EOF
}

check_installed() {
    if ! command -v ansible >/dev/null 2>&1; then
        echo "ansible binary not found"
        return 2
    else 
        if ansible --version 2>&1 | grep -Fxq "$EXPECTED_LINE"; then
            echo "ansible reports expected config file"
            return 0
        else
            echo "ansible does not report the expected config file"
            return 3
        fi
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

if [ $# -lt 1 ]; then
    usage
    exit 64
fi

case "$1" in
    check)
        check_installed
        exit $?
        ;;
    install)
        do_install
        exit $?
        ;;
    -h|--help)
        usage
        exit 0
        ;;
    *)
        echo "Unknown command: $1" >&2
        usage
        exit 64
        ;;
esac
