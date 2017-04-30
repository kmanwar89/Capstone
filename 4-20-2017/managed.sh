#! /bin/bash

sudo iwconfig mon0
sudo iw dev mon0 del
sudo iw phy phy0 interface add wlp2s0 type managed
sudo ifconfig wlp2s0 up
