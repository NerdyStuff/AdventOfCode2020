file = open("luggage_rules.txt", "r")

rules = dict()
for line in file:
    line = line[:-2]
    bagColor = (line[:line.find("bags")])[:-1]
    bags = line[line.find("contain")+8:]
    if not "no other bags" in bags:
        bags = bags.split(",")
        for i in range(len(bags)):
            bags[i] = bags[i].lstrip()     
    else:
        bags = [bags]
    rules[bagColor] = bags
    bags = []

print(rules)