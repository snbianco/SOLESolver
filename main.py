# Author: Samantha Bianco

import numpy as np


def validate(eq_str, eq_num):
    if eq_str.count('=') != 1:
        return False

    left = eq_str.partition('=')[0].strip()
    try:
        right = float(eq_str.partition('=')[2].strip())
    except SyntaxError:
        return False

    if not parse(left, eq_num):
        return False

    B[eq_num][0] = right

    return True

# Add in support for:
# parentheses
# Multiple terms with same variable
# Variable terms on both sides of equation
def parse(left_side, eq_num):
    token = ''

    for ch in left_side:
        if ch.isnumeric() or ch == '-' or ch == '.':
            token += ch
        elif ch in var_lst:
            idx = var_lst.index(ch)
            try:
                A[eq_num][idx] = float(token)
            except SyntaxError:
                return False
            token = ''
        elif ch == ' ' or ch == '+':
            continue
        else:
            return False

    return True


if __name__ == '__main__':
    print('\nWelcome to the Systems of Linear Equations (SOLE) Solver.\n')

    num_vars = int(input('Enter the number of variables in the system: \n'))

    A = np.zeros([num_vars, num_vars])
    B = np.zeros([num_vars, 1])

    var_lst = []
    for i in range(num_vars):
        var = input(f'Enter variable #{i + 1}: \n')

        while len(var) != 1 or not var.isalpha():
            var = input('Variable should be a single alphabetic character. Please enter a valid variable: \n')

        var_lst.append(var)

    for i in range(num_vars):
        form = ''
        for j in range(num_vars):
            form += f'{chr(65 + j)}{var_lst[j]} '
            form += '+ ' if j != num_vars - 1 else f'= {chr(66 + j)}'

        equation = input(f'Enter equation #{i + 1} ({form}): \n')

        while not validate(equation, i):
            equation = input(f'Equation should be in the form {form}. Please enter a valid equation: \n')

    solution = np.linalg.solve(A, B)

    print('Solution:\n')
    for i in range(num_vars):
        print(f'{var_lst[i]} = {solution[i][0]}')