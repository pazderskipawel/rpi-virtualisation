#!/bin/bash

# Aktualizacja systemu
echo "Aktualizacja systemu..."
sudo apt-get update && sudo apt-get upgrade -y

# Instalacja Ansible z repozytorium
echo "Instalacja Ansible..."
sudo apt-get install -y ansible

# Weryfikacja instalacji
if command -v ansible &> /dev/null; then
    echo "Ansible został pomyślnie zainstalowany."
    ansible --version
else
    echo "Instalacja Ansible nie powiodła się."
    exit 1
fi

echo "Instalacja zakończona."
