#!/bin/bash

addr="$( ifconfig bridge100 | awk '$1 == "inet" {print $2}' )"
ips=($( nmap -sP ${addr}/24 | grep 'for' | grep -v $addr | sed 's/Nmap scan report for //g' ))

for ip in ${ips[@]}; do
#reboot all machines
ssh pirate@$ip <<EOF
    sudo reboot
EOF
done
