'''
Day:            16
File:           ticket_translation.py
Author:         Rishabh Ranjan
Last Modified:  12/16/2020
'''

def find_error_rate(fields, nearby_tickets):
    error_rate = 0
    invalid_tickets = []
    for ticket in nearby_tickets:
        invalid_ticket = False
        for value in ticket:
            valid = False
            for ranges in fields.values():
                for value_range in ranges:
                    if value >= value_range[0] and value <= value_range[1]:
                        valid = True
                        break
                if valid:
                    break
            if not valid:
                error_rate += value
                invalid_ticket = True
        if invalid_ticket:
            invalid_tickets.append(ticket)
    return error_rate, invalid_tickets

def find_field_positions(fields, my_ticket, nearby_tickets):
    possible_fields = []
    for i in range(len(nearby_tickets[0])):
        possible_fields.append(list(fields.keys()))
    for i in range(len(nearby_tickets[0])):
        for j in range(len(nearby_tickets)):
            for field, ranges in fields.items():
                valid = False
                for value_range in ranges:
                    if nearby_tickets[j][i] >= value_range[0] and nearby_tickets[j][i] <= value_range[1]:
                        valid = True
                        break
                if field in possible_fields[i] and not valid:
                    possible_fields[i].remove(field)
    all_fields_found = False
    while not all_fields_found:
        all_fields_found = True
        for field_list in possible_fields:
            if len(field_list) == 1:
                for other_field_list in possible_fields:
                    if field_list != other_field_list and field_list[0] in other_field_list:
                        other_field_list.remove(field_list[0])
            else:
                all_fields_found = False
    starting_word = "departure"
    product = 1
    for i in range(len(my_ticket)):
        if possible_fields[i][0].startswith(starting_word):
            product *= my_ticket[i]
    return product

def main():
    f = open('day_16_input.txt', 'r')
    input = f.read().splitlines()
    f.close()
    fields = {}
    my_ticket = []
    nearby_tickets = []
    parsing_ranges = True
    parsing_nearby_tickets = False
    parsing_my_ticket = False
    for line in input:
        if line == "":
            parsing_ranges = False
            continue
        if line == "your ticket:":
            parsing_my_ticket = True
            continue
        if line == "nearby tickets:":
            parsing_nearby_tickets = True
            continue
        if parsing_ranges:
            field = line[:line.index(':')]
            ranges = []
            for word in line.split():
                if '-' in word:
                    ranges.append((int(word[:word.index('-')]), int(word[word.index('-') + 1:])))
            fields[field] = ranges
            continue
        if parsing_my_ticket:
            my_ticket = list(map(int, line.split(',')))
            parsing_my_ticket = False
            continue
        if parsing_nearby_tickets:
            nearby_tickets.append(list(map(int, line.split(','))))
    error_rate, invalid_tickets = find_error_rate(fields, nearby_tickets)
    print("Part 1 Answer: ", error_rate)
    for ticket in invalid_tickets:
        nearby_tickets.remove(ticket)
    print("Part 2 Answer: ", find_field_positions(fields, my_ticket, nearby_tickets))

if __name__ == '__main__':
    main()
