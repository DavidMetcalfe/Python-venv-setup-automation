#!/usr/bin/env python

""" Expedites creation of venv environments and
requirements.txt files.
"""
import re
import os
import sys
from time import sleep
import subprocess

# Create venv command input
pattern = re.compile('([^\s\w]|_)+')

userinput = input('Input desired venv folder name: ')
foldername = pattern.sub('', userinput)
foldername = " ".join(foldername.split())

# Check if first letter of foldername is uppercase.
if foldername[0].isupper():
    venvcom = "python -m venv " + "\"" + foldername + "\""
else:
    # If the first letter is not capitalized, then capitalize it.
    foldername = foldername.capitalize()
    venvcom = "python -m venv " + "\"" + foldername + "\""

# Command for venv
print("Creating venv folders.\n")
subprocess.run(venvcom, shell=True)

# Filesystem vars
scriptpath = os.path.dirname(os.path.realpath(__file__))
destination = os.path.normpath(os.path.join(scriptpath, foldername))

# Create requirements.txt file
requirements = []

loopcounter = 0

print('Waiting on folder creation')
while not os.path.exists(destination):
    print('.', end='')
    loopcounter += 1
    if loopcounter <= 60:
        break
    sleep(0.5)

if os.path.exists(destination):
    print("************************************\n")
    print("venv folder created.\n")
    with open(os.path.join(destination, 'requirements.txt'), 'w') as f:
        reqinput = input(
            "Enter modules (if any) to include in requirements.txt (hit Enter after each package): \n")

        while reqinput is not "":
            requirements.append(reqinput)
            reqinput = input("")

        if requirements:
            for i in requirements:
                f.write("{}\n".format(i))

        # Install requirements to venv.
        subprocess.run([os.path.join(destination, 'Scripts',
                                     'pip.exe')] + 'install {}'.format(' '.join(requirements)).split())

else:
    sys.exit(0)
