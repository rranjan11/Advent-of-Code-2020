'''
Day:            4
File:           passport_processing.py
Author:         Rishabh Ranjan
Last Modified:  12/6/2020
'''

def get_valid_passports(passports, required_fields):
    count_old = 0
    count_new = 0
    for passport in passports:
        valid_old = True
        valid_new = True
        for field in required_fields:
            if not field in passport:
                valid_old = False
                valid_new = False
                break
            if field == "byr" and valid_new == True:
                if len(passport[field]) != 4:
                    valid_new = False
                    continue
                if int(passport[field]) < 1920 or int(passport[field]) > 2002:
                    valid_new = False
                    continue
            elif field == "iyr" and valid_new == True:
                if len(passport[field]) != 4:
                    valid_new = False
                    continue
                if int(passport[field]) < 2010 or int(passport[field]) > 2020:
                    valid_new = False
                    continue
            elif field == "eyr" and valid_new == True:
                if len(passport[field]) != 4:
                    valid_new = False
                    continue
                if int(passport[field]) < 2020 or int(passport[field]) > 2030:
                    valid_new = False
                    continue
            elif field == "hgt" and valid_new == True:
                if passport[field][len(passport[field]) - 2:len(passport[field])] == "cm":
                    if not (passport[field][:len(passport[field]) - 2].isnumeric() and int(passport[field][:len(passport[field]) - 2]) >= 150
                        and int(passport[field][:len(passport[field]) - 2]) <= 193):
                        valid_new = False
                        continue
                elif passport[field][len(passport[field]) - 2:len(passport[field])] == "in":
                    if not (passport[field][:len(passport[field]) - 2].isnumeric() and int(passport[field][:len(passport[field]) - 2]) >= 59
                        and int(passport[field][:len(passport[field]) - 2]) <= 76):
                        valid_new = False
                        continue
                else:
                    valid_new = False
                    continue
            elif field == "hcl" and valid_new == True:
                if len(passport[field]) != 7 or passport[field][0] != '#':
                    valid_new = False
                    continue
                for i in range(1, len(passport[field])):
                    if not (passport[field][i].isnumeric() or passport[field][i] == 'a' or passport[field][i] == 'b' or passport[field][i] == 'c'
                        or passport[field][i] == 'd' or passport[field][i] == 'e' or passport[field][i] == 'f'):
                        valid_new = False
                        break
                if valid_new == False:
                    continue
            elif field == "ecl" and valid_new == True:
                if (passport[field] != "amb" and passport[field] != "blu" and passport[field] != "brn" and passport[field] != "gry"
                    and passport[field] != "grn" and passport[field] != "hzl" and passport[field] != "oth"):
                    valid_new = False
                    continue
            elif field == "pid" and valid_new == True:
                if not (len(passport[field]) == 9 and passport[field].isnumeric()):
                    valid_new = False
                    continue
        if valid_old:
            count_old += 1
        if valid_new:
            count_new += 1
    return count_old, count_new

def main():
    f = open('day_4_input.txt', 'r')
    input = f.read().splitlines()
    f.close()
    passports = []
    temp_passport = {}
    for line in input:
        passport = {}
        if line == "":
            passports.append(temp_passport)
        else:
            passport = temp_passport
        start_index = 0
        field = ""
        value = ""
        for i in range(len(line)):
            if line[i] == ':':
                field = line[start_index:i]
                start_index = i + 1
            if line[i] == ' ':
                value = line[start_index:i]
                passport[field] = value
                start_index = i + 1
            if i == len(line) - 1:
                value = line[start_index:i + 1]
                passport[field] = value
        temp_passport = passport
    passports.append(temp_passport)
    required_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    valid_passports_old, valid_passports_new = get_valid_passports(passports, required_fields)
    print("Part 1 Answer: ", valid_passports_old)
    print("Part 2 Answer: ", valid_passports_new)

if __name__ == '__main__':
    main()
