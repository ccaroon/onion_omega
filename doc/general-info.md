# General Info

## Factory Reset
Will reset the Omega to the base firmware currently loaded and DELETE all extra
installed files.

Can do this if you use up all the space and want to start over.

1. `firstboot -y`
2. `sync`
3. `reboot`

## WiFi
1. `wifisetup`

## SSH Access
`ssh -oHostKeyAlgorithms=+ssh-rsa -oPubkeyAcceptedAlgorithms=+ssh-rsa root@ONION-IP-ADDR`

## Format SD
1. Find mount point: `/mnt/mmcblk0p1`
2. Find Device Name: `/dev/mmcblk0p1`
3. `umount /mnt/mmcblk0p1`
4. `mkfs.ext4 /dev/mmcblk0p1`
5. Remount or reboot for auto-mounting

## Development
### Base
1. `opkg update`
2. `opkg install git git-http ca-bundle vim-full`

### Python3
1. `opkg update`
2. `opkg install python3-light`
3. `opkg install python3-pip`

### NodeJS
1. `opkg update`
2. `opkg install nodejs`
3. `opkg install blynk-library`
