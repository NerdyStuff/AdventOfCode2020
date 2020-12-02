# Day 2
counter = 0

# Part 1
def countCharsInWord(letter, word):
    letterCount = 0
    for i in word:
        if i == letter:
            letterCount = letterCount + 1
    return letterCount

file = open("passwords.txt", "r")
for line in file:
    minLetters = int(line.split('-')[0])
    maxLetters = int(line[line.find('-')+1:line.find(' ')])
    letter = line[line.find(' ')+1]
    password = line[line.find(':') + 1:]

    if countCharsInWord(letter, password) >= minLetters and countCharsInWord(letter, password) <= maxLetters:
        counter = counter + 1
print("Passwords which fill requirements: ", counter)
file.close()

# Part 2
file = open("passwords.txt", "r")
counter = 0
for line in file:
    firstPos = int(line.split('-')[0])
    secondPos = int(line[line.find('-')+1:line.find(' ')])
    letter = line[line.find(' ')+1]
    password = line[line.find(':') + 1:]
    password = password[1:]

    if password[firstPos-1] == letter:
        if(password[secondPos-1] != letter):
            counter = counter + 1
    else:
        if(password[secondPos-1] == letter):
            counter = counter + 1
print("Passwords which new fill requirements: ", counter)
file.close()
