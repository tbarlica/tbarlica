#!/usr/bin/env python3

print("1. Convert inches -> cm")
print("2. Convert cm -> inches")

selection = input("Make your selection (1, 2): ")

if selection == "1":
    inches = float(input("Enter inches: "))
    cm = inches * 2.54
    print("Number of cm: " + str(cm))
elif selection == "2":
    cm = float(input("Enter cm: "))
    inches = cm / 2.54
    print("Number of inches: " + str(inches))
else:
    print("Invalid selection")