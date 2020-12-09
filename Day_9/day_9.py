import numpy as np
# Day 9

# Part 1
file = open("encoding.txt", "r")

numbers = []
for line in file:
    line = line[:-1]
    numbers.append(line)

file.close()

def isValidNo(arr, no):
    for elem in arr:
        a = str(int(no)-int(elem))
        if a in arr:
            return True
    return False

startArr = numbers[:24]

invalidNo = 0
for number in numbers[24:]:
    if isValidNo(startArr, int(number)):
        startArr.append(number)
    else:
        invalidNo = number
        print("Non valid number: ", number)
        break

# Part 2
summands = []
numbers = list(map(int, numbers))
for i in range(len(numbers)):
    for j in range(len(numbers)):
        sumArr = np.sum(numbers[i:j])
        if sumArr == int(invalidNo):
            summands.append(numbers[i])

print("Min: ", min(summands), " max: ", max(summands), " sum: ", (min(summands) + max(summands)))