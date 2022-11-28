import os
import sys

print("Downloding files")

os.system("docker pull dorowu/ubuntu-desktop-lxde-vnc:latest")

print("Runig server")

#os.system("docker run -d \ --name ubuntu_desktop \ -v /dev/shm:/dev/shm \ -p 6080:80 \ dorowu/ubuntu-desktop-lxde-vnc")

os.system("docker run -d   --name ubuntu_desktop   -v /dev/shm:/dev/shm   -p 6080:80   dorowu/ubuntu-desktop-lxde-vnc")
