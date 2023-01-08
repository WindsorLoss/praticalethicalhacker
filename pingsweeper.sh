#!/bin/bash

if [ "$1" == "" ]
then
echo "Você esqueceu de adicionar um endereço de IP!"
echo "Sintaxe de exemplo: ./ipsweeper 192.168.18"

else
for ip in `seq 1 254`; do
ping $1.$ip -c 1 | grep "64 bytes" | cut -d " " -f 4 | tr -d ":" &
done
fi