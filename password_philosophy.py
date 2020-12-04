'''
Day:            2
File:           password_philosophy.py
Author:         Rishabh Ranjan
Last Modified:  12/3/2020
'''

def old_num_valid_passwords(passwords):
    valid_passwords = 0
    for password in passwords:
        letter = password[password.index(':') - 1]
        letter_min = int(password[:password.index('-')])
        letter_max = int(password[password.index('-') + 1:password.index(' ')])
        letter_count = 0
        for i in range(password.index(':') + 2, len(password)):
            if (password[i] == letter):
                letter_count += 1
        if letter_count >= letter_min and letter_count <= letter_max:
            valid_passwords += 1
    return valid_passwords

def new_num_valid_passwords(passwords):
    valid_passwords = 0
    for password in passwords:
        valid = False
        letter = password[password.index(':') - 1]
        position_1 = int(password[:password.index('-')])
        position_2 = int(password[password.index('-') + 1:password.index(' ')])
        if password[password.index(':') + 1 + position_1] == letter or password[password.index(':') + 1 + position_2] == letter:
            valid = True
        if password[password.index(':') + 1 + position_1] == letter and password[password.index(':') + 1 + position_2] == letter:
            valid = False
        if valid:
            valid_passwords += 1
    return valid_passwords

def main():
    f = open('day_2_input.txt', 'r')
    passwords = f.read().splitlines()
    f.close()
    print("Part 1 Answer: ", old_num_valid_passwords(passwords))
    print("Part 2 Answer: ", new_num_valid_passwords(passwords))

if __name__ == '__main__':
    main()
