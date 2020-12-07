file = open("luggage_rules.txt", "r")

# TODO => NEEDS TO BE REFACTORED FOR INPUT
def findColor(searchColor, dictionary):
    foundKeys = []
    if any(searchColor in string for string in bagList) == True:
        foundKeys.append(dictionary[color])
    return foundKeys

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

liste = []
for color, bagList in rules.items():
    if any("shiny gold" in string for string in bagList) == True:
        liste.append({color: rules[color]})
print(liste)