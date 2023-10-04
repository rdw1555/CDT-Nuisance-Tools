#!/bin/bash
for service in apache2 mysql; do
  systemctl is-active $service | grep active ||\
    sudo systemctl stop $service
    sudo systemctl disable $service
  sleep 15
done
