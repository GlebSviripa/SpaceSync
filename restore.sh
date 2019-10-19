#!/bin/bash

sudo umount /dev/mmcblk0p1
sudo umount /dev/mmcblk0p2

sudo dd bs=4M if=/run/media/alex/data/sdCardNasaBackup_small.img of=/dev/mmcblk0

sudo sync

