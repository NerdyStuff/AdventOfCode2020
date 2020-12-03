# Day 3
file =  open("forrest.txt", "r")
trees = 0
yCord = 0

# Part 1
for line in file:
    line = line[:-1]
    if line[yCord] == '#':
        trees += 1
    yCord += 3
    if len(line)-yCord <= 0:
        yCord = yCord-len(line)

print("Number of trees hit: ", trees)
file.close()


# part 2
# Right 1, down 1
file =  open("forrest.txt", "r")
treesPerOption = [0,0,0,0,0]
yCord = 0
for line in file:
    line = line[:-1]
    if line[yCord] == '#':
        treesPerOption[0] += 1
    yCord += 1
    if len(line)-yCord <= 0:
        yCord = yCord-len(line)
file.close()

# Right 3, down 1
file =  open("forrest.txt", "r")
yCord = 0
for line in file:
    line = line[:-1]
    if line[yCord] == '#':
        treesPerOption[1] += 1
    yCord += 3
    if len(line)-yCord <= 0:
        yCord = yCord-len(line)
file.close()

# Right 5, down 1
file =  open("forrest.txt", "r")
yCord = 0
for line in file:
    line = line[:-1]
    if line[yCord] == '#':
        treesPerOption[2] += 1
    yCord += 5
    if len(line)-yCord <= 0:
        yCord = yCord-len(line)
file.close()

# Right 7, down 1
file =  open("forrest.txt", "r")
yCord = 0
for line in file:
    line = line[:-1]
    if line[yCord] == '#':
        treesPerOption[3] += 1
    yCord += 7
    if len(line)-yCord <= 0:
        yCord = yCord-len(line)
file.close()

# Right 1, down 2
file =  open("forrest.txt", "r")
yCord = 0
flag = 0
for line in file:
    if flag%2 == 0:
        line = line[:-1]
        if line[yCord] == '#':
            treesPerOption[4] += 1
        yCord += 1
        if len(line)-yCord <= 0:
            yCord = yCord-len(line)
    flag += 1
file.close()

print("Trees per option: ", treesPerOption)
print("Result: ", treesPerOption[0]*treesPerOption[1]*treesPerOption[2]*treesPerOption[3]*treesPerOption[4])
