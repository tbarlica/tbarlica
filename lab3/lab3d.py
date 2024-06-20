#!/usr/bin/env python3

# Author ID: tbarlica

import subprocess

def free_space():
    command = "df -h | grep '/$' | awk '{print $4}'"
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output = process.communicate()
    stdout = output[0].decode('utf-8').strip()
    return stdout

if __name__ == "__main__":
    print(free_space())