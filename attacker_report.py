#!/usr/bin/env python3

# Alex Tedesco
# 3/30/2023

# Imports:
import os
from collections import Counter
from geoip import geolite2
import datetime

# Clears the terminal upon running the script
os.system ("clear")

# Opens syslog as file
with open('syslog.log') as file:
    ip_addresses = []

# Iterates over each line in syslog
    for line in file:
        # Removes white space from the line
        line = line.strip()
        # Checks if the line is a failed password attempt
        if "Failed password for" in line:
            line = line.split("from ")
            newLine = line[1]
            newLine = newLine.split (" ")
            # Appends the IP address into a list
            ip_addresses.append (newLine[0])

    # Converts the list in a collection of nested lists ["IP", "Count"]
    counts = Counter(ip_addresses)

# Converts the collection to a tuple
counts = counts.most_common()

# Obtains the current date
date = datetime.datetime.now()

# Prints the results to standard output
print ("\u001b[32;1m" + "Attacker Report" + "\u001b[0m" + " - " + date.strftime ("%B") + " " + date.strftime ("%d") + ", " + date.strftime ("%Y") + "\n")
print ('\u001b[31;1m' + "COUNT" + '\t' + "IP Address" + '\t' + "COUNTRY" + "\u001b[0m")

# Iterates over each element in the counts tuple. Reverses the order of the tuple to least to greatest
for i in counts[::-1]:
    # Checks if the IP is shown more than 10 times
    if i[1] >= 10:
        # Stores data as string variables
        ip_address = str(i[0])
        count = str(i[1])
        country = geolite2.lookup(i[0]).country
        # Prints to standard output
        print (count, ip_address, country, sep="\t")