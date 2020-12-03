'''
Day:            1
File:           report_repair.py
Author:         Rishabh Ranjan
Last Modified:  12/1/2020
'''

def two_entries_with_sum(expense_report, sum):
    for i in range(len(expense_report)):
        for j in range(i + 1, len(expense_report)):
            if expense_report[i] + expense_report[j] == sum:
                return expense_report[i]*expense_report[j]

def three_entries_with_sum(expense_report, sum):
    for i in range(len(expense_report)):
        for j in range(i + 1, len(expense_report)):
            for k in range(j + 1, len(expense_report)):
                if expense_report[i] + expense_report[j] + expense_report[k] == sum:
                    return expense_report[i]*expense_report[j]*expense_report[k]

def main():
    f = open('day_1_input.txt', 'r')
    expense_report = []
    for x in f:
        expense_report.append(int(x.rstrip('\n')))
    f.close()
    sum = 2020
    print("Part 1 Answer: ", two_entries_with_sum(expense_report, sum))
    print("Part 2 Answer: ", three_entries_with_sum(expense_report, sum))

if __name__ == '__main__':
    main()
