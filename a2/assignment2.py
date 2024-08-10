#!/usr/bin/env python3

import argparse
import os
import sys

def parse_command_args() -> object:
    "Set up argparse here. Call this function inside main."
    parser = argparse.ArgumentParser(description="Memory Visualiser -- See Memory Usage Report with bar charts", 
                                     epilog="Copyright 2023")
    
    parser.add_argument("-l", "--length", type=int, default=20, help="Specify the length of the graph. Default is 20.")
    
    # Make this entry for human-readable. Check the docs to make it a True/False option.
    parser.add_argument("program", type=str, nargs='?', help="If a program is specified, show memory use of all associated processes. Show only total use if not.")
    
    args = parser.parse_args()
    return args

def percent_to_graph(percent: float, length: int=20) -> str:
    '''
    Turns a percent 0.0 - 1.0 into a bar graph
    The function will return a string of hashes and spaces to represent the percentage of memory used.
    '''
    num_hashes = int(percent * length)
    return '#' * num_hashes + ' ' * (length - num_hashes)

def get_sys_mem() -> int:
    '''
    Return total system memory (used or available) in kB
    The function will open the meminfo file and return the total memory.
    Total memory in linux is stored in the MemTotal line.
    Total memory is the sum of free memory and used memory.
    '''
    # Open the meminfo file to accomplish the task!
    meminfo_file = open("/proc/meminfo", "r")
    lines = meminfo_file.readlines()
    meminfo_file.close()
    
    for line in lines:
        if "MemTotal:" in line:
            parts = line.split() # split the line into parts using whitespace
            total_memory_kb = int(parts[1]) # second part is the total memory in kB
            return total_memory_kb

def get_avail_mem() -> int:
    '''
    Return total memory that is currently in use
    The function will open the meminfo file and return the available memory.
    Avialable memory in linux is stored in the MemAvailable line.
    Avaialble memory is the sum of free memory and memory used by cache.
    '''
    # Open the meminfo file to accomplish the task!
    meminfo_file = open("/proc/meminfo", "r")
    lines = meminfo_file.readlines()
    meminfo_file.close()
    
    for line in lines:
        if "MemAvailable:" in line:
            parts = line.split()
            available_memory_kb = int(parts[1])
            return available_memory_kb

def pids_of_prog(app_name: str) -> list:
    '''
    Given an app name, return all pids associated with app
    The function will return a list of process ids associated with the given app name
    os.popen() is used to run the command 'pidof <app_name>' and get the output
    pidoof command returns a space-separated list of process ids
    '''
    # Please use os.popen('pidof <app>') to accomplish the task!
    pids = os.popen(f'pidof {app_name}').read().strip().split() # strip() removes leading/trailing whitespace
    return pids

def rss_mem_of_pid(proc_id: str) -> int:
    '''
    "Given a process id, return the Resident memory used"
    # For a process, open the smaps file and return the total of each Rss line.
    
    open the smaps file for the given process id and return the total Resident memory used
    Resident memory is the memory that is actually in use by the process
    the function will read the smaps file line by line and sum the Rss values
    '''

    total_rss = 0
    try:
        smaps_file = open(f"/proc/{proc_id}/smaps", "r")
        for line in smaps_file:
            if line.startswith("Rss:"): 
                total_rss += int(line.split()[1]) # Rss is the second value in the line
        smaps_file.close()
    except FileNotFoundError:
        pass
    return total_rss

def bytes_to_human_r(kibibytes: int, decimal_places: int=2) -> str:
    "Turn 1,024 into 1 MiB, for example"
    suffixes = ['KiB', 'MiB', 'GiB', 'TiB', 'PiB']  # iB indicates 1024
    suf_count = 0
    result = kibibytes
    
    while result > 1024 and suf_count < len(suffixes):
        result /= 1024
        suf_count += 1
    
    str_result = f'{result:.{decimal_places}f} '
    str_result += suffixes[suf_count]
    return str_result

if __name__ == "__main__":
    args = parse_command_args()
    
    if not args.program:  # No program name is specified.
        pass
    else:
        pass
