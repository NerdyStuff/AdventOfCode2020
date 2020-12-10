# Day 10

# Part 1
file = open("jolts.txt", "r")

jolts = []
for line in file:
    line = line[:-1]
    jolts.append(int(line))

file.close()

sortedAdapters = jolts
sortedAdapters.sort()

oneCounter = 0
threeCounter = 0
otherCounter = 0

for i in range(len(sortedAdapters)):
    idx = i + 1
    if idx >= len(sortedAdapters):
        idx = len(sortedAdapters)-1

    if sortedAdapters[idx] - sortedAdapters[i] == 1:
        oneCounter += 1
    elif sortedAdapters[idx] - sortedAdapters[i] == 3:
        threeCounter += 1
    else:
        otherCounter += 1
print("one jolts: ", oneCounter,"three jolts: ", threeCounter, "other: ", otherCounter)
print("Multiplied: ", oneCounter * threeCounter)