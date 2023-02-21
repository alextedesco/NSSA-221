#!/usr/bin/env python3

# Alex Tedesco
# 2/20/2023

# Imports:
import os
import subprocess as sp

# Clears the terminal upon running the script
os.system ("clear")

'''
- For information on RAM use the free command.
- For network information, use ip a, netstat, and ip route commands.
- For DNS examine the /etc/resolv.conf file.
- For system disk information, use the df command.
- Examine the contents of the /etc/proc file for CPU specs and /etc/*release for operating system information
'''

date = sp.getoutput ('date +"%Y-%m-%y"')
hostname = ""
domain = ""
ip_address = ""
gateway = ""
network_mask = ""
dns1 = ""
dns2 = ""
operating_system = ""
version = ""
kernel_version = ""
capacity = sp.getoutput("df -h --total | tail -1 | tr -s ' ' | cut -d ' ' -f 2")
space = sp.getoutput("df -h --total | tail -1 | tr -s ' ' | cut -d ' ' -f 4")
cpu = ""
num_processors = ""
num_cores = ""
total_ram = sp.getoutput("free -g -h -t| sed -n '4p' | tr -s ' ' | cut -d ' ' -f 2")
available_ram = sp.getoutput("free -g -h -t| sed -n '4p' | tr -s ' ' | cut -d ' ' -f 3")



print ('        ' + date + '        ')

print ("\u001b[32m" + "Device Information" + "\u001b[37m")
print ("Hostname:              " + hostname)
print ("Domain:              " + domain + "\n")

print ("\u001b[32m" + "Network Information" + "\u001b[37m")
print ("IP Address:              " + ip_address)
print ("Gateway:              " + gateway)
print ("Network Mask:              " + network_mask)
print ("DNS1:              " + dns1)
print ("DNS2:              " + dns2 + "\n")

print ("\u001b[32m" + "OS Information" + "\u001b[37m")
print ("Operating System:              " + operating_system)
print ("Operating Version:              " + version)
print ("Kernel Version:              " + kernel_version + "\n")

print ("\u001b[32m" + "Storage Information" + "\u001b[37m")
print ("Hard Drive Capacity:              " + capacity)
print ("Available Space:              " + space + "\n")

print ("\u001b[32m" + "Processor Information" + "\u001b[37m")
print ("CPU Model:              " + cpu)
print ("Number of processors:              " + num_processors)
print ("Number of cores:              " + num_cores + "\n")

print ("\u001b[32m" + "Memory Information" + "\u001b[37m")
print ("Total RAM:              " + total_ram)
print ("Available RAM:              " + available_ram + "\n")