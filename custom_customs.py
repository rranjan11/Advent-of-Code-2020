'''
Day:            6
File:           custom_customs.py
Author:         Rishabh Ranjan
Last Modified:  12/6/2020
'''

def answered_questions(forms, answers_list):
    count = 0
    for answers in answers_list:
        count += len(answers)
    count2 = 0
    for i in range(len(forms)):
        for answer in answers_list[i]:
            everyone = True
            for line in forms[i]:
                if not answer in line:
                    everyone = False
            if everyone:
                count2 += 1
    return count, count2

def main():
    f = open('day_6_input.txt', 'r')
    input = f.read().splitlines()
    f.close()
    forms = []
    temp_form = []
    answers_list = []
    temp_answers = set()
    for line in input:
        form = []
        answers = set()
        if line == "":
            forms.append(temp_form)
            answers_list.append(temp_answers)
        else:
            form = temp_form
            answers = temp_answers
            form.append(line)
            for answer in line:
                answers.add(answer)
        temp_form = form
        temp_answers = answers
    forms.append(temp_form)
    answers_list.append(temp_answers)
    answers_anyone, answers_everyone = answered_questions(forms, answers_list)
    print("Part 1 Answer: ", answers_anyone)
    print("Part 2 Answer: ", answers_everyone)

if __name__ == '__main__':
    main()
