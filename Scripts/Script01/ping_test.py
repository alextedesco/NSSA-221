#!/usr/bin/env python3

# Alex Tedesco
# 2/10/2023

# Imports:
import os
import subprocess as sp

# Clears the terminal upon running the script
os.system ("clear")

# Obtains the default gatway by cutting the output at each space and using the 3rd delimeter 
default_gateway = sp.getoutput ("ip r | grep default | cut -d ' ' -f3")

# Infinite Loop that displays user options and awaits inputs
while True:
    print ("    **************************************")
    print ("    ****** " + '\u001b[32m' + "Ping Test Troubleshooter " + '\u001b[37m' + "******")
    print ("    **************************************")
    print ("\n\nEnter Selection:\n")
    print ("	1 - Test connectivity to your gateway.")
    print ("	2 - Test for remote connectivity.")
    print ("	3 - Test for DNS resolution.")
    print ("	4 - Display gateway IP Address.\n")
    num = input ('Please enter a ' + '\u001b[32m' + "number (1-4) " + '\u001b[37m' + "or " + '\u001b[32m' + '"Q/q"' + '\u001b[37m' + ' to quit the program.	')
    
# Tests connectivity to the default gateway
    if num == '1':
        os.system ("clear")
        print ("Running test, please wait.\n")
        # '>/dev/null 2>&1' redirects the stdout and stderr to null
        # Saves the exit code to a variable which is checked to see if the ping command was successful
        output = os.system('ping -c 5 '  + default_gateway + " >/dev/null 2>&1")
        if output == 0:
            print ("Please inform your system administrator that the test was " + '\u001b[33m' + "SUCCESSFUL" + '\u001b[37m' + "!\n")        
        else:
            print ("Please inform your system administrator that the test was " + '\u001b[31m' + "FAILED" + '\u001b[37m' + "!\n")

# Tests the remote connectivity by pinging RIT
    elif num == '2':
        os.system ("clear")
        print ("Running test, please wait.\n")
        # '>/dev/null 2>&1' redirects the stdout and stderr to null
        # Saves the exit code to a variable which is checked to see if the ping command was successful
        output = os.system("ping -c 5 129.21.3.17 >/dev/null 2>&1")
        if output == 0:
            print ("Please inform your system administrator that the test was " + '\u001b[33m' + "SUCCESSFUL" + '\u001b[37m' + "!\n")        
        else:
            print ("Please inform your system administrator that the test was " + '\u001b[31m' + "FAILED" + '\u001b[37m' + "!\n")

# Tests the DNS resolution by pinging google.com
    elif num == '3':
        os.system ("clear")
        print ("Running test, please wait.\n")
        # '>/dev/null 2>&1' redirects the stdout and stderr to null
        # Saves the exit code to a variable which is checked to see if the ping command was successful
        output = os.system("ping -c 5 www.google.com >/dev/null 2>&1")
        print (output)
        if output == 0:
            print ("Please inform your system administrator that the test was " + '\u001b[33m' + "SUCCESSFUL" + '\u001b[37m' + "!\n")        
        else:
            print ("Please inform your system administrator that the test was " + '\u001b[31m' + "FAILED" + '\u001b[37m' + "!\n")

# Displays the gateway IP address obtained earlier on Line 14
    elif num == '4':
        os.system ('clear')
        print ('\n\u001b[33m' + "Your gateway IP address is " + '\u001b[37m' + default_gateway + "\n")

# Ends the troubleshooter
    elif num == 'Q' or num == 'q':
        os.system ("clear")
        print ("\nQuitting program: returning to shell \n\n" + '\u001b[33m' + "Have a wonderful day!" + '\u001b[37m')
        break

# Displays error message for when all else is inputed
    else:
        print ("Incorrect or Invalid Information")
