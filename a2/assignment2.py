#!/usr/bin/env python3

'''
Author: Traian Barlica
Description: OPS445 Assignment 2 Version A - Summer 2024
Program: assignment2.py 
The python code in this file is original work written by
Traian Barlica. No code in this file is copied from any other source
except those provided by the course instructor, including any person,
textbook, or on-line resource. I have not shared this python script
with anyone or anything except for submission for grading. I understand
that the Academic Honesty Policy will be enforced and
violators will be reported and appropriate action will be taken.

Description:

This program is a memory visualizer that shows the memory usage of a program or all associated processes.
The program reads the /proc/meminfo file to get the total memory and available memory.
It calculates the memory usage as a percentage and displays it as a bar graph.
The program can display memory usage in human-readable format.
The program can display memory usage of all processes associated with a program.
The program reads the /proc/<pid>/smaps file to get the resident memory of a process.
The program displays the memory usage of each process as a bar graph.
'''

import argparse
import os
import sys

def parse_command_args() -> object:
    '''
    Set up argparse here. Call this function inside main.
    parser.add_argument() is used to add arguments to the parser
    parser.parse_args() is used to parse the command line arguments
    human-readable argument is added with -H alias
    '''
    parser = argparse.ArgumentParser(description="Memory Visualiser -- See Memory Usage Report with bar charts",
                                     epilog="Copyright 2023")
    
    parser.add_argument("-H", "--human-readable", action="store_true", help="Prints sizes in human readable format")
    parser.add_argument("-l", "--length", type=int, default=20, help="Specify the length of the graph. Default is 20.")
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
    args = parse_command_args() # Parse the command line arguments
    
    total_mem = get_sys_mem() # Get the total system memory
    avail_mem = get_avail_mem() # Get the available memory
    used_mem = total_mem - avail_mem # Calculate the used memory
    percent_used = used_mem / total_mem # Calculate the percentage of memory used
    
    if not args.program:  # No program name is specified
        graph = percent_to_graph(percent_used, args.length) # Get the graph representation of memory usage
        if args.human_readable: # Print human readable output
            # Print the memory usage in human readable format
            print(f"Memory [ {graph} | {percent_used:.0%} ] ({bytes_to_human_r(used_mem)} / {bytes_to_human_r(total_mem)})")
        else:
            print(f"Memory [ {graph} | {percent_used:.0%} ] ({used_mem} / {total_mem})")
    else: # A program name is specified
        pids = pids_of_prog(args.program) # Get the process ids of the program
        if not pids:
            print(f"{args.program} not found.") # Print a message if the program is not found
        else:
            total_rss = 0 
            for pid in pids:
                rss_mem = rss_mem_of_pid(pid) # Get the resident memory of the process
                total_rss += rss_mem # Add the resident memory to the total
                percent_used = rss_mem / total_mem # Calculate the percentage of memory used
                graph = percent_to_graph(percent_used, args.length)
                # Print the memory usage of each process
                # :<10 is used to left align the pid in a 10 character wide field
                if args.human_readable:
                    print(f"{pid:<10} [ {graph} | {percent_used:.0%} ] {bytes_to_human_r(rss_mem)} / {bytes_to_human_r(total_mem)}")
                else:
                    print(f"{pid:<10} [ {graph} | {percent_used:.0%} ] ({rss_mem} / {total_mem})")
            # If there are multiple processes, print the total memory usage        
            if len(pids) > 1:
                percent_used = total_rss / total_mem
                graph = percent_to_graph(percent_used, args.length)
                if args.human_readable:
                    print(f"{args.program:<10} [ {graph} | {percent_used:.0%} ] {bytes_to_human_r(total_rss)} / {bytes_to_human_r(total_mem)}")
                else:
                    print(f"{args.program:<10} [ {graph} | {percent_used:.0%} ] ({total_rss} / {total_mem})")

