This directory included the arduino code for receiving UART message and a python code for Beaglebone to send "hello world" to arduino devices.

Do note that:
The arduino code need to be uploaded to the arduino device before hand.
Device tree overlay had to be done before the UART port of Beaglebone can be used. Below is the instruction for device try overlay

#Reference: https://learn.adafruit.com/introduction-to-the-beaglebone-black-device-tree/exporting-and-unexporting-an-overlay
#Take note that bone_capemgr has been shifted inside /sys/devices/platform
#TRY if UART-1 overlay works
cd /sys/devices/platform/bone_capemgr
echo BB-UART1 > slots 


#Permanently load overlay for UART1 to work
nano /boot/uEnv.txt

#uncomment "cape_enable=bone_capemgr.enable_partno=" and add BB-UART1
#example: "cape_enable=bone_capemgr.enable_partno=BB-UART1"
#Make sure you're doing it under v4.1.x
