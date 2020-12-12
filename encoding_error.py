'''
Day:            9
File:           encoding_error.py
Author:         Rishabh Ranjan
Last Modified:  12/12/2020
'''

def first_invalid_num(xmas):
    for i in range(25, len(xmas)):
        valid = False
        for j in range(i - 25, i):
            for k in range(j + 1, i):
                if xmas[i] == xmas[j] + xmas[k]:
                    valid = True
        if not valid:
            return xmas[i], i

def find_encryption_weakness(xmas, invalid_num, invalid_num_index):
    for i in range(2, invalid_num_index):
        for j in range(invalid_num_index - i + 1):
            sum = 0
            sum_range = set()
            for k in range(i):
                sum_range.add(xmas[j + k])
                sum += xmas[j + k]
            if sum == invalid_num:
                return min(sum_range) + max(sum_range)

def main():
    f = open('day_9_input.txt', 'r')
    xmas = list(map(int, f.read().splitlines()))
    f.close()
    invalid_num, invalid_num_index = first_invalid_num(xmas)
    print("Part 1 Answer: ", invalid_num)
    print("Part 2 Answer: ", find_encryption_weakness(xmas, invalid_num, invalid_num_index))

if __name__ == '__main__':
    main()
