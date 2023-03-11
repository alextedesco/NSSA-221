#!/usr/bin/env python3

# Alex Tedesco
# 3/10/2023

# Imports:
import os
import sys
import subprocess as sp
import time
from pathlib import Path

# Clears the terminal upon running the script
os.system ("clear")

desktop = str(Path.home()) + "/Desktop"

# Infinite Loop that displays user options and awaits inputs
while True:
    print ("    **************************************")
    print ("    *********" + '\u001b[32m' + " Shortcut Creater " + '\u001b[37m' + "***********")
    print ("    **************************************")
    print ("\n\nEnter Selection:\n")
    print ("	1 - Create a shortcut in your home directory.")
    print ("	2 - Remove a shortcut from your home directory")
    print ("	3 - Run shortcut report.\n")
    num = input ('Please enter a ' + '\u001b[32m' + "number (1-3) " + '\u001b[37m' + "or " + '\u001b[32m' + '"Q/q"' + '\u001b[37m' + ' to quit the program.	')
    
# Creates a symlink
    if num == '1':
        # Clears the terminal
        os.system ("clear")
        add = input ("Please enter the file name to create a shortcut:          ")

        # Gets the output of where the file is
        file = sp.getoutput('find /home -name ' + add)
        
        # Determines if the file exists
        if file.startswith("/home") == True:
            confirmation = input ('\u001b[32m' + "Found " + '\u001b[37m' + file + " Select Y/y to create a shortcut.     ")
            if confirmation == "Y" or confirmation == "y":
                try:
                    os.symlink (file,  desktop + "/" + add)
                    print ("Creating Shortcut, please wait.\n")
                    
                    # Progress Bar
                    for i in range(21):
                        sys.stdout.write('\r')
                        sys.stdout.write("[%-20s] %d%%" % ('='*i, 5*i))
                        sys.stdout.flush()
                        time.sleep(0.25)
                        
                    print ("\nShortcut created. Returning to Main Menu.")
                    time.sleep(3)
                    os.system("clear")
                except FileExistsError:
                    print ("File is already a symbolic link. Returning to Main Menu")
                    time.sleep(3)
                    os.system("clear")
                except Exception as e:
                    print ("Invalid information inputed. Returning to Main Menu")
                    os.system("clear")
            else:
                print ("Invalid information inputed. Returning to Main Menu")
                time.sleep(3)
                os.system("clear")

        else:
            print ("File does not exist. Returning to Main Menu.")
            time.sleep(3)
            os.system ("clear")

# Removes a symlink
    elif num == '2':
        os.system ("clear")
        remove = input ("Please enter the shortcut/link to remove:          ")
        confirmation = input ("Are you sure you want to remove " + '\u001b[32m' + 
        remove + '\u001b[37m' + "? Press " + '\u001b[32m' + "Y/y" + 
        '\u001b[37m' + " to confirm:       ")
        if confirmation == "Y" or confirmation == "y":
            try:
                os.remove (desktop +"/" + remove)
                print ("Removing link, please wait...")

                # Progress Bar
                for i in range(21):
                    sys.stdout.write('\r')
                    sys.stdout.write("[%-20s] %d%%" % ('='*i, 5*i))
                    sys.stdout.flush()
                    time.sleep(0.25)
                print ("\nLink removed, returning to Main Menu")
                time.sleep(3)
                os.system("clear")
            # Error handling for if symlink already exists
            except FileExistsError:
                print ("File is already a symbolic link")
            # Error handling for if the file does not exist
            except FileNotFoundError:
                print ("File does not exist. Returning to Main Menu")
                time.sleep(3)
                os.system("clear")
            # Error handling for all other errors
            except Exception as e:
                print ("Invalid")
        # If anything else that isn't Y or y is inputed, go back to Main Menu
        else:
            print ("Invalid Information Entered! Returning to Main Menu")
            # Sleeps terminal for 3 seconds
            time.sleep(3)
             # Clears terminal and goes back Main Menu
            os.system("clear")

# Outputs the number of symlinks made
    elif num == '3':
        # Clears the terminal
        os.system ("clear")
        print ("    **************************************")
        print ("    *********" + '\u001b[32m' + " Shortcut Report " + '\u001b[37m' + "***********")
        print ("    **************************************")
        # Determines how many symlinks there are by counting the amount of outputed lines
        amount = sp.getoutput ("find " + desktop + " -type l | wc -l")
        # Stores the current directory to a variable
        current = sp.getoutput ('pwd')
        print("\n\nYour current directory is " + '\u001b[33m' + current + '\u001b[37m')
        print ("The number of links is " + '\u001b[33m' + amount + '\u001b[37m')
        # Sleeps terminal for 3 seconds
        time.sleep (3)
        # Clears the terminal
        os.system ("clear")
        print ("Returning to " + '\u001b[33m' + "Main Menu" + '\u001b[37m' + " shortly. Please wait...")

        # Progress bar
        for i in range(21):
            sys.stdout.write('\r')
            sys.stdout.write("[%-20s] %d%%" % ('='*i, 5*i))
            sys.stdout.flush()
            time.sleep(0.25)
        # Clears terminal and goes back Main Menu
        os.system("clear")


# Ends the troubleshooter
    elif num == 'Q' or num == 'q' or num == "quit":
        os.system ("clear")
        print ("\nQuitting program: returning to shell \n\n" + '\u001b[33m' + "Have a wonderful day!" + '\u001b[37m')
        break

# Displays error message for when all else is inputed
    else:
        print ("Incorrect or Invalid Information")
        time.sleep(3)
        os.system("clear")