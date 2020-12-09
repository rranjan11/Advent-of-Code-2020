'''
Day:            8
File:           handheld_halting.py
Author:         Rishabh Ranjan
Last Modified:  12/8/2020
'''

def run_boot_code(boot_code):
    accumulator = 0
    visited = set()
    i = 0
    terminated = True
    while i < len(boot_code):
        if i in visited:
            terminated = False
            break
        visited.add(i)
        if boot_code[i][:3] == "acc":
            accumulator += int(boot_code[i][4:])
        elif boot_code[i][:3] == "jmp":
            i += int(boot_code[i][4:]) - 1
        i += 1
    return accumulator, terminated

def main():
    f = open('day_8_input.txt', 'r')
    boot_code = f.read().splitlines()
    f.close()
    accululator, terminated = run_boot_code(boot_code)
    print("Part 1 Answer: ", accululator)
    for i in range(len(boot_code)):
        boot_code_copy = boot_code.copy()
        if boot_code_copy[i][:3] == "jmp":
            boot_code_copy[i] = boot_code_copy[i].replace("jmp", "nop")
        elif boot_code_copy[i][:3] == "nop":
            boot_code_copy[i] = boot_code_copy[i].replace("nop", "jmp")
        else:
            continue
        accumulator, terminated = run_boot_code(boot_code_copy)
        if terminated:
            print("Part 2 Answer: ", accumulator)
            break

if __name__ == '__main__':
    main()
