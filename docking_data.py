'''
Day:            14
File:           docking_data.py
Author:         Rishabh Ranjan
Last Modified:  12/16/2020
'''

def execute_program(program):
    mem = {}
    zero_mask = 0
    one_mask = 0
    for line in program:
        if line[:4] == "mask":
            zero_mask = int("0b" + line[7:].replace('X', '1'), 2)
            one_mask = int("0b" + line[7:].replace('X', '0'), 2)
        else:
            address = int(line.split()[0][4:-1])
            mem[address] = (int(line.split()[2]) & zero_mask) | one_mask
    return sum(mem.values())

def execute_program_v2(program):
    mem = {}
    mask = ""
    for line in program:
        if line[:4] == "mask":
            mask = line[7:]
        else:
            address = bin(int(line.split()[0][4:-1]))[2:]
            if len(address) < len(mask):
                for i in range(len(mask) - len(address)):
                    address = '0' + address
            x_list = []
            for i in range(len(address)):
                if mask[i] == '1':
                    address = address[:i] + '1' + address[i + 1:]
                elif mask[i] == 'X':
                    address = address[:i] + 'X' + address[i + 1:]
                    x_list.append(i)
            for i in range(2**len(x_list)):
                binary_i = bin(i)[2:]
                if len(binary_i) < len(x_list):
                    for j in range(len(x_list) - len(binary_i)):
                        binary_i = '0' + binary_i
                for j in range(len(binary_i)):
                    address = address[:x_list[j]] + binary_i[j] + address[x_list[j] + 1:]
                address_int = int("0b" + address, 2)
                mem[address_int] = int(line.split()[2])
    return sum(mem.values())

def main():
    f = open('day_14_input.txt')
    program = f.read().splitlines()
    f.close()
    print("Part 1 Answer: ", execute_program(program))
    print("Part 2 Answer: ", execute_program_v2(program))

if __name__ == '__main__':
    main()
