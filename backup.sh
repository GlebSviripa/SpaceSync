#!/bin/bash

sudo dd if=/dev/mmcblk0 of=/run/media/alex/data/sdCardNasaBackup_small.img bs=1M count=4096

sudo sync


