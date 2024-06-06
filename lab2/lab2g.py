#!/usr/bin/env python3

#Author: Traian Barlica
#Author ID: 117979229
#Date Created: 2024/05/30

import sys

if len(sys.argv) != 2:
    timer = 3
else:    
    timer = int(sys.argv[1])

while timer != 0:
    print(timer)
    timer -= 1
print('blast off!')