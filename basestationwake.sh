#!/bin/sh
while :
do
    sudo PYTHONPATH=/home/pi/pythonscripts python3 basestation.py >> /tmp/basestation.log 
done
