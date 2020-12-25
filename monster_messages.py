# WIP

'''
Day:            19
File:           monster_messages.py
Author:         Rishabh Ranjan
Last Modified:  12/25/2020
'''

def main():
    f = open('day_19_input.txt', 'r')
    input = f.read().splitlines()
    f.close()
    rules = {}
    messages = []
    parsing_rules = True
    for line in input:
        if line == "":
            parsing_rules = False
            continue
        if parsing_rules:
            rule = line.split()
            rules[rule[0][:-1]] = rule[1:]
        else:
            messages.append(line)
    # rules['8'] = ["42", '|', "42", '8']
    # rules["11"] = ["42", "31", '|', "42", "11", "31"]
    max_message_length = max(list(map(len, messages)))
    # print(rules)
    possible_messages = [rules['0']]
    all_possibilities_found = False
    while not all_possibilities_found:
        # if i % 10000 == 0:
        print(len(possible_messages))
            # if len(possible_messages) == 2097152:
            #     break
        new_possible_messages = []
        for message in possible_messages:
            # print(message)
            new_message = []
            for item in message:
                if item.isnumeric():
                    if len(rules[item]) == 3 and rules[item][1] == '|':
                        new_message += [rules[item][0], "||", rules[item][2]]
                    elif len(rules[item]) == 4 and rules[item][1] == '|':
                        new_message += [rules[item][0], "|||", rules[item][2], rules[item][3]]
                    elif len(rules[item]) == 6 and rules[item][2] == '|':
                        new_message += rules[item][:2] + ["||||"] + rules[item][3:]
                    else:
                        new_message += rules[item]
                else:
                    new_message.append(item)
            message_variations = [new_message]
            pipe_symbol_present = True
            while pipe_symbol_present:
                pipe_symbol_present = False
                new_message_variations = []
                for message_variation in message_variations:
                    if '|' in message_variation:
                        pipe_symbol_present = True
                        pipe_index = message_variation.index('|')
                        left_copy = message_variation.copy()
                        left_copy.pop(pipe_index - 2)
                        left_copy.pop(pipe_index - 2)
                        left_copy.pop(pipe_index - 2)
                        right_copy = message_variation.copy()
                        right_copy.pop(pipe_index)
                        right_copy.pop(pipe_index)
                        right_copy.pop(pipe_index)
                        new_message_variations.append(left_copy)
                        new_message_variations.append(right_copy)
                    elif "||" in message_variation:
                        pipe_symbol_present = True
                        pipe_index = message_variation.index("||")
                        left_copy = message_variation.copy()
                        left_copy.pop(pipe_index - 1)
                        left_copy.pop(pipe_index - 1)
                        right_copy = message_variation.copy()
                        right_copy.pop(pipe_index)
                        right_copy.pop(pipe_index)
                        new_message_variations.append(left_copy)
                        new_message_variations.append(right_copy)
                    elif "|||" in message_variation:
                        pipe_symbol_present = True
                        pipe_index = message_variation.index("|||")
                        left_copy = message_variation.copy()
                        left_copy.pop(pipe_index - 1)
                        left_copy.pop(pipe_index - 1)
                        right_copy = message_variation.copy()
                        right_copy.pop(pipe_index)
                        right_copy.pop(pipe_index)
                        right_copy.pop(pipe_index)
                        # num_triple_pipes = 0
                        # num_quad_pipes = 0
                        # for item in left_copy:
                        #     if item == "|||":
                        #         num_triple_pipes += 1
                        #     elif item == "||||":
                        #         num_quad_pipes += 1
                        if len(left_copy) <= max_message_length:
                            new_message_variations.append(left_copy)
                        else:
                            print("limit reached")
                        new_message_variations.append(right_copy)
                    elif "||||" in message_variation:
                        pipe_symbol_present = True
                        pipe_index = message_variation.index("||||")
                        left_copy = message_variation.copy()
                        left_copy.pop(pipe_index - 2)
                        left_copy.pop(pipe_index - 2)
                        left_copy.pop(pipe_index - 2)
                        right_copy = message_variation.copy()
                        right_copy.pop(pipe_index)
                        right_copy.pop(pipe_index)
                        right_copy.pop(pipe_index)
                        right_copy.pop(pipe_index)
                        num_quad_pipes = 0
                        # for item in left_copy:
                        #     if item == "||||":
                        #         num_quad_pipes += 1
                        if len(left_copy) <= max_message_length:
                            new_message_variations.append(left_copy)
                        else:
                            print("limit reached")
                        new_message_variations.append(right_copy)
                    else:
                        new_message_variations.append(message_variation)
                message_variations = new_message_variations
            for message_variation in message_variations:
                new_possible_messages.append(message_variation)
        possible_messages = new_possible_messages
        all_possibilities_found = True
        for message in possible_messages:
            for item in message:
                if item != '"a"' and item != '"b"':
                    all_possibilities_found = False
    possible_messages_strings = set()
    for message in possible_messages:
        message_string = ""
        for item in message:
            message_string += item[1]
        possible_messages_strings.add(message_string)
    # print(possible_messages_strings)
    # print(len(possible_messages), len(possible_messages_strings))
    count = 0
    for message in messages:
        if message in possible_messages_strings:
            # print(message_string)
            count += 1
    print(count)

if __name__ == '__main__':
    main()
