# Day 8

# Part 1
file = open("bootcode.txt", "r")

bootcode = []
for line in file:
    line = line[:-1]
    bootcode.append(line)

file.close()

linesVisited = []
counter = 0
index = 0
interrupt = False
while interrupt == False:
    if "nop" in bootcode[index]:
        index += 1
        continue
    elif "acc" in bootcode[index]:
        val = bootcode[index][bootcode[index].find(" ")+1:]
        counter += int(val)
        index += 1
    elif "jmp" in bootcode[index]:
        val = bootcode[index][bootcode[index].find(" ")+1:]
        index += int(val)
    if index not in linesVisited:
        linesVisited.append(index)
    else:
        break

print("Counter: ", counter)

# Part 2
linesVisited = []
codesVisited = []
counter = 0
index = 0
interrupt = False
while interrupt == False:
    if "nop" in bootcode[index]:
        index += 1
        continue
    elif "acc" in bootcode[index]:
        val = bootcode[index][bootcode[index].find(" ")+1:]
        counter += int(val)
        index += 1
    elif "jmp" in bootcode[index]:
        val = bootcode[index][bootcode[index].find(" ")+1:]
        index += int(val)
    if index not in linesVisited:
        linesVisited.append(index)
        codesVisited.append(bootcode[index])
    else:
        break

print(index, " | ", bootcode[index])
print("Counter: ", counter)