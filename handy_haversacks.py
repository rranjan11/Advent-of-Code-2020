'''
Day:            7
File:           handy_haversacks.py
Author:         Rishabh Ranjan
Last Modified:  12/7/2020
'''

def can_contain_color(rule, rules, color, visited):
    rule_words = rule.split()
    rule_color = rule_words[0] + " " + rule_words[1]
    if rule_color != color and color in rule:
        return True
    return_value = False
    for i in range(4, len(rule_words)):
        if rule_words[i].isnumeric():
            new_color = rule_words[i + 1] + " " + rule_words[i + 2]
            new_rule = ""
            for color_rule in rules:
                if color_rule.startswith(new_color):
                    new_rule = color_rule
                    break
            if new_color not in visited:
                visited.add(new_color)
                return_value = return_value or can_contain_color(new_rule, rules, color, visited)
    return return_value

def count_bags(rule, rules):
    count = 0
    rule_words = rule.split()
    for i in range(4, len(rule_words)):
        if rule_words[i].isnumeric():
            color = rule_words[i + 1] + " " + rule_words[i + 2]
            new_rule = ""
            for color_rule in rules:
                if color_rule.startswith(color):
                    new_rule = color_rule
                    break
            count += int(rule_words[i]) + int(rule_words[i])*count_bags(new_rule, rules)
    return count

def main():
    f = open('day_7_input.txt', 'r')
    rules = f.read().splitlines()
    f.close()
    count = 0
    for rule in rules:
        visited = set()
        if can_contain_color(rule, rules, "shiny gold", visited):
            count += 1
    print("Part 1 Answer: ", count)
    for rule in rules:
        if rule.startswith("shiny gold"):
            shiny_gold_rule = rule
            break
    print("Part 2 Answer: ", count_bags(shiny_gold_rule, rules))

if __name__ == '__main__':
    main()
