#!/bin/bash

if [ "$1" == "" ]
then
echo "Esqueceste-te do Ip address"
echo "Sintaxe: ./ipsweep.sh 192.168.1"

else
> ficheiro.txt
for ip in `seq 1 254`; do 
if [ ! -z $(ping -c 1 $1.$ip | grep "64 bytes" | cut -d " " -f 4| tr -d ":" &) ] &
then
ping -c 1 $1.$ip | grep "64 bytes" | cut -d " " -f 4| tr -d ":" >> ficheiro.txt &
fi
done
fi 
