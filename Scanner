#!/bin/bash

# Mon scanner de ports optimisé
ip_cible=$1

# Liste des ports communs à scanner par défaut
ports_communs=(21 22 25 53 80 110 443 445 8080 3306)

# Fonction de scan de port
scan_port() {
    (echo > /dev/tcp/$1/$2) >/dev/null 2>&1 && echo "Port $2 ouvert sur $1" || echo "Port $2 fermé sur $1"
}

# Validation des paramètres
if [ $# -eq 1 ]; then
    for port in "${ports_communs[@]}"; do
        scan_port $ip_cible $port &
    done
    wait
elif [ $# -eq 3 ]; then
    for port in $(seq $2 $3); do
        scan_port $ip_cible $port &
    done
    wait
else
    echo "Usage : $0 <IP cible> [port_debut port_fin]"
    exit 1
fi
