# My calculator V 1.0

def calculate():

    n1 = int(input('Type a number: '))
    n2 = int(input('Type other number: '))
    op = (input('''
    Please, type in the math operation: 
    + for addition
    - for subtraction
    * for multiplication
    ** for calculate powers
    / for division
    // for division discards the fractional part
    '''))

    # Addition
    if op == '+':
        r = (n1 + n2)
        print('{} + {} = {}'.format(n1, n2, r))

    # Subtraction
    elif op == '-':
        r = (n1 - n2)
        print('{} - {} = {}'.format(n1, n2, r))

    # Multiplication
    elif op == '*':
        r = (n1 * n2)
        print('{} - {} = {}'.format(n1, n2, r))

    # Powers
    elif op == '**':
        r = (n1 ** n2)
        print('{} ** {} = {}'.format(n1, n2, r))

    # Division
    elif op == '/':
        r = (n1 / n2)
        print('{} / {} = {}'.format(n1, n2, r))

    # Division discards the fractional part
    elif op == '//':
        r = (n1 // n2)
        print('{} // {} = {}'.format(n1, n2, r))

    # Remainder of the division
    elif op == '%':
        r = (n1 % n2)
        print('{} % {} = {}'.format(n1, n2, r))

    else:
        print('This operation does bot exist or you not have a valid operator type!')
        
    again()
# Play again
def again():
    calc_again = input('''
        Do you want to calculate again?
        Please, type Y (Yes) or N (No) 
        ''')
    if calc_again.upper() == 'Y':
        calculate()
        
    elif calc_again.upper() == 'N':
        print('See you later!')
        
    else:
        again()

calculate()
