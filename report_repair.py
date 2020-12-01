def main():
    f = open('day_1_input.txt', 'r')
    expense_report = []
    for x in f:
        expense_report.append(x[:len(x) - 1])
    f.close()
    found = False
    for i in range(len(expense_report)):
        for j in range(i + 1, len(expense_report)):
            if int(expense_report[i]) + int(expense_report[j]) == 2020:
                print("Part 1 Answer: ", int(expense_report[i])*int(expense_report[j]))
                found = True
                break
        if found:
            break
    for i in range(len(expense_report)):
        for j in range(i + 1, len(expense_report)):
            for k in range(j + 1, len(expense_report)):
                if int(expense_report[i]) + int(expense_report[j]) + int(expense_report[k]) == 2020:
                    print("Part 2 Answer: ", int(expense_report[i])*int(expense_report[j])*int(expense_report[k]))
                    return

if __name__ == '__main__':
    main()
