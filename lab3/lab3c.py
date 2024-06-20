#!/usr/bin/env python3
'''Lab 3 Inv 2 function operate '''
# Author ID: tbarlica

def operate(number1, number2, operator):
    # Place logic in this function

    if operator == 'add':
        value = int(number1) + int(number2)
    elif operator == 'subtract':
        value = int(number1) - int(number2)
    elif operator == 'multiply':
        value = int(number1) * int(number2)
    else:
        value = 'Error: function operator can be "add", "subtract", or "multiply"'
    return value

if __name__ == '__main__':
    print(operate(10, 5, 'add'))
    print(operate(10, 5, 'subtract'))
    print(operate(10, 5, 'multiply'))
    print(operate(10, 5, 'divide'))