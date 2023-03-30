#!/usr/bin/env python3

# Alex Tedesco
# 3/28/2023

# Imports:
import os
from collections import Counter
from geoip import geolite2
import datetime

# Clears the terminal upon running the script
os.system ("clear")

with open('syslog.log') as file:
    ipaddresses = []

    for line in file:
        line = line.strip()
        if "Failed password for" in line:
            line = line.split(": ")
        
            if line[1].startswith("Failed password for invalid user"):
                failedpasswd = line[1]
                failedpasswd = failedpasswd.split(" ")
                ipaddresses.append(failedpasswd[7])
            
            elif line[1].startswith("Failed password for root"):
                failedpasswd = line[1]
                failedpasswd = failedpasswd.split(" ")
                ipaddresses.append(failedpasswd[5])

    counts = Counter(ipaddresses)

counts = counts.most_common()

date = datetime.datetime.now()

print ("\u001b[32m" + "Attacker Report" + "\u001b[37m" + " - " + date.strftime ("%B") + " " + date.strftime ("%d") + ", " + date.strftime ("%Y") + "\n")
print ('\u001b[31m' + "COUNT           IP Address              COUNTRY" + "\u001b[37m")

for i in counts[::-1]:
    if i[1] >= 20:
        ip_address = str(i[0])
        count = str(i[1])
        country = geolite2.lookup(i[0]).country
        print (count  + "             " + ip_address + "        " + country)