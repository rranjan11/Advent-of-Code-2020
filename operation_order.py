'''
Day:            18
File:           operation_order.py
Author:         Rishabh Ranjan
Last Modified:  12/18/2020
'''

def evaluate_expression(expression, addition_precedence):
    parentheses_nesting = 0
    start_index = 0
    for i in range(len(expression)):
        if expression[i] == '(':
            if parentheses_nesting == 0:
                start_index = i + 1
            parentheses_nesting += 1
        if expression[i] == ')':
            parentheses_nesting -= 1
            if parentheses_nesting == 0:
                return evaluate_expression(expression[:start_index - 1] + [str(evaluate_expression(expression[start_index:i], addition_precedence))] + expression[i + 1:], addition_precedence)
    while len(expression) > 1:
        if addition_precedence:
            addition_precedence = False
            for i in range(len(expression)):
                if expression[i] == '+':
                    value = int(expression.pop(i - 1))
                    expression.pop(i - 1)
                    value += int(expression.pop(i - 1))
                    expression.insert(i - 1, str(value))
                    addition_precedence = True
                    break
        else:
            for i in range(len(expression)):
                if expression[i] == '+':
                    value = int(expression.pop(i - 1))
                    expression.pop(i - 1)
                    value += int(expression.pop(i - 1))
                    expression.insert(i - 1, str(value))
                    break
                if expression[i] == '*':
                    value = int(expression.pop(i - 1))
                    expression.pop(i - 1)
                    value *= int(expression.pop(i - 1))
                    expression.insert(i - 1, str(value))
                    break
    return int(expression[0])

def main():
    f = open('day_18_input.txt', 'r')
    homework = f.read().splitlines()
    f.close()
    count1 = 0
    count2 = 0
    for i in range(len(homework)):
        all_parentheses_separated = False
        while not all_parentheses_separated:
            all_parentheses_separated = True
            for j in range(len(homework[i])):
                if homework[i][j] == '(' or homework[i][j] == ')':
                    if j > 0 and homework[i][j - 1] != ' ':
                        homework[i] = homework[i][:j] + ' ' + homework[i][j:]
                        all_parentheses_separated = False
                        break
                    if j < len(homework[i]) - 1 and homework[i][j + 1] != ' ':
                        homework[i] = homework[i][:j + 1] + ' ' + homework[i][j + 1:]
                        all_parentheses_separated = False
                        break
        expression1 = homework[i].split()
        expression2 = expression1.copy()
        count1 += evaluate_expression(expression1, False)
        count2 += evaluate_expression(expression2, True)
    print("Part 1 Answer: ", count1)
    print("Part 2 Answer: ", count2)

if __name__ == '__main__':
    main()
