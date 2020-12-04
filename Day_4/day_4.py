import re
# Day 4
file = open ("passports.txt", "r")
# Part 1
passport = ""
passports = []
validPassports = 0

for line in file:
    if not line in ['\r\n', '\n']:
        passport += (line.replace("\n", "") + " ")
    else:
        passports.append(passport[:-1])
        passport = ""    
passports.append(passport[:-1])
passport = ""

# check passports
for pp in passports:
    if "byr" in pp and "iyr" in pp and "eyr" in pp and "hgt" in pp and "hcl" in pp and "ecl" in pp and "pid" in pp:
        validPassports += 1
print("Valid passports (with cid optional): ", validPassports)
file.close()

# Part 2

def validateInput(line):
    # required fields set
    if "byr" in line and "iyr" in line and "eyr" in line and "hgt" in line and "hcl" in line and "ecl" in line and "pid" in line:
        # check values
        d = dict(x.split(":") for x in line.split(" "))
        
        byr = int(d["byr"])
        iyr = int(d["iyr"])
        eyr = int(d["eyr"])
        hgt = d["hgt"]
        hcl = d["hcl"]
        ecl = d["ecl"]
        pid = d["pid"]

        if byr < 1920 or byr > 2002:
            return False
        if iyr < 2010 or iyr > 2020:
            return False
        if eyr < 2020 or eyr > 2030:
            return False
        if not ("cm" in hgt or "in" in hgt):
            return False
        if "cm" in hgt:
            if int(hgt[:-2]) < 150 or int(hgt[:-2]) > 193:
                return False
        if "in" in hgt:
            if int(hgt[:-2]) < 59 or int(hgt[:-2]) > 76:
                return False
        if not re.search(r'^#([a-f0-9]{6})$', hcl):
            return False
        if not (ecl in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]):
            return False
        if not re.search(r'^([0-9]{9})$', pid):
            return False
        return True
    else:
        return False
    
file = open ("passports2.txt", "r")

passport = ""
passports = []
validPassports = 0

for line in file:
    if not line in ['\r\n', '\n']:
        passport += (line.replace("\n", "") + " ")
    else:
        passports.append(passport[:-1])
        passport = ""    
passports.append(passport[:-1])
passport = ""

# check passports
for pp in passports:
    if validateInput(pp) == True:
        validPassports += 1
print("Valid passports part 2: ", validPassports)
