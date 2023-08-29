def arithmetic_arranger(math, answer=False):

    right_alligned_1strow = None
    right_alligned_2ndrow = None
    dasher = None
    right_alligned_result = None
    arithmetics = math
    solver = answer
    arranged_1st_row = []
    arranged_2nd_row = []
    dashers = []
    answers = []

    for problems in arithmetics:
        if len(arithmetics) > 5:
            problems_lenght_error = "Error: Too many problems."
            return problems_lenght_error
        elements = problems.split()
        first_number = elements[0]
        second_number = elements[2]
        operator = elements[1]
        if operator != '+':
            if operator != '-':
                return "Error: Operator must be '+' or '-'."
        try:
            number1_int = int(first_number)
        except ValueError:
            return 'Error: Numbers must only contain digits.'
        try:
            number2_int = int(second_number)
        except ValueError:
            return 'Error: Numbers must only contain digits.'

        if len(first_number) > 4 or len(second_number) > 4:
            return 'Error: Numbers cannot be more than four digits.'

        
        if len(first_number) > len(second_number) and operator == '+':
            right_alligned_1strow = first_number.rjust(len(first_number) + 2)
            right_alligned_2ndrow = '+' + second_number.rjust(len(right_alligned_1strow) - 1)
            dasher = '-' * len(right_alligned_1strow)
            result = str(number1_int + number2_int)
            right_alligned_result = result.rjust(len(right_alligned_1strow))

        elif len(first_number) < len(second_number) and operator == '+':
            right_alligned_2ndrow = '+' + second_number.rjust(len(second_number) + 1)
            right_alligned_1strow = first_number.rjust(len(right_alligned_2ndrow))
            dasher = '-' * len(right_alligned_2ndrow)
            result = str(number1_int + number2_int)
            right_alligned_result = result.rjust(len(right_alligned_2ndrow))

        elif len(first_number) > len(second_number) and operator == '-':
            right_alligned_1strow = first_number.rjust(len(first_number) + 2)
            right_alligned_2ndrow = '-' + second_number.rjust(len(right_alligned_1strow) - 1)
            dasher = '-' * len(right_alligned_1strow)
            result = str(number1_int - number2_int)
            right_alligned_result = result.rjust(len(right_alligned_1strow))

        elif len(first_number) < len(second_number) and operator == '-':
            right_alligned_2ndrow = '-' + second_number.rjust(len(second_number) + 1)
            right_alligned_1strow = first_number.rjust(len(right_alligned_2ndrow))
            dasher = '-' * len(right_alligned_2ndrow)
            result = str(number1_int - number2_int)
            right_alligned_result = result.rjust(len(right_alligned_2ndrow))

        elif len(first_number) == len(second_number) and operator == '-':
            right_alligned_2ndrow = '-' + second_number.rjust(len(second_number) + 1)
            right_alligned_1strow = first_number.rjust(len(right_alligned_2ndrow))
            dasher = '-' * len(right_alligned_2ndrow)
            result = str(number1_int - number2_int)
            right_alligned_result = result.rjust(len(right_alligned_2ndrow))

        elif len(first_number) == len(second_number) and operator == '+':
            right_alligned_2ndrow = '+' + second_number.rjust(len(second_number) + 1)
            right_alligned_1strow = first_number.rjust(len(right_alligned_2ndrow))
            dasher = '-' * len(right_alligned_2ndrow)
            result = str(number1_int + number2_int)
            right_alligned_result = result.rjust(len(right_alligned_2ndrow))

        if len(arranged_1st_row) < 1:
            arranged_1st_row.append(right_alligned_1strow)
        else:
            arranged_1st_row.append('    ')
            arranged_1st_row.append(right_alligned_1strow)

        if len(arranged_2nd_row) < 1:
            arranged_2nd_row.append(right_alligned_2ndrow)
        else:
            arranged_2nd_row.append('    ')
            arranged_2nd_row.append(right_alligned_2ndrow)

        if len(dashers) < 1:
            dashers.append(dasher)
        else:
            dashers.append('    ')
            dashers.append(dasher)

        if len(answers) < 1:
            answers.append(right_alligned_result)
        else:
            answers.append('    ')
            answers.append(right_alligned_result)

    arranged_1st_row = ''.join(arranged_1st_row)
    arranged_2nd_row = ''.join(arranged_2nd_row)
    dashers = ''.join(dashers)
    answers = ''.join(answers)

    if not solver:
        arranged_problems = arranged_1st_row + '\n' + arranged_2nd_row + '\n' + dashers
    else:
        arranged_problems = arranged_1st_row + '\n' + arranged_2nd_row + '\n' + dashers + '\n' + answers

    return arranged_problems
