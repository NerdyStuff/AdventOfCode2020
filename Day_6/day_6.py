# Day 6

# Part 1
file = open("answers.txt", "r")

answers = []
answer = ""
answerSum = 0

for line in file:
    if not line in ['\r\n', '\n']:
        answer += (line.replace("\n", "") + " ")
    else:
        answers.append(answer[:-1])
        answer = ""    
answers.append(answer[:-1])
answer = ""

for i in range(len(answers)):
    answers[i] = answers[i].replace(" ", "") # remove blanks
    answers[i] = list(dict.fromkeys(answers[i])) # remove duplicates
    answerSum += len(answers[i])

print("Sum of answers: ", answerSum)
file.close()

# Part 2 (Does not work, butr can be used as start)
file = open("answers.txt", "r")

answers = []
answer = ""
answerSum = 0

for line in file:
    if not line in ['\r\n', '\n']:
        answer += (line.replace("\n", "") + " ")
    else:
        answers.append(answer[:-1])
        answer = ""    
answers.append(answer[:-1])
answer = ""

for i in range(len(answers)):
    aws = answers[i].split(' ')
    match = set()
    for j in range(len(aws)):
        match = set(aws[0]).intersection(aws[j])
    answerSum += len(match)
    print(match)

print("Sum of answers for part 2: ", answerSum)
file.close()