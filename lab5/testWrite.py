exList = ['line1', 'line2', 'line3']
number = 0
for list in exList:
    exList[number] = str(number + 1) + ':' + list
    number += 1
print(exList)