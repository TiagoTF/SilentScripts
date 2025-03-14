#!/bin/bash

touch ficheiro.txt

if [ -z "$1" ]; then
    echo "Esqueceste-te do Ip address"
    echo "Sintaxe: ./ipsweep.sh 192.168.1"
    exit 1
fi

# Count the number of dots in the provided argument
dot_count=$(echo "$1" | tr -cd '.' | wc -c)

if [ "$dot_count" -eq 2 ]; then
    # Scanning a /24 subnet (192.168.1.x)
    for ip in $(seq 1 254); do
        (
            if ping -c 1 -W 1 "${1}.${ip}" | grep -q "64 bytes"; then
                echo "${1}.${ip}"
            fi
        ) &
    done
    wait  # Ensure all background processes finish

elif [ "$dot_count" -eq 1 ]; then
    # Scanning a /16 subnet (192.168.x.x)
    for ip in $(seq 1 254); do
        for ipp in $(seq 1 254); do
            (
                if ping -c 1 -W 1 "${1}.${ip}.${ipp}" | grep -q "64 bytes"; then
                    echo "${1}.${ip}.${ipp}"
                fi
            ) &
        done
    done
    wait  # Ensure all background processes finish

else
    echo "Formato de IP inválido. Use algo como 192.168 ou 192.168.1"
    exit 1
fi
