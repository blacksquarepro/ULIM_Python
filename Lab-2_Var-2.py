'''Scrieți un program care efectuează ceea ce este indicat în variantă cu ambele tipuri de cicluri [for/while] (valoarea tuturor variabilelor trebuie citită de la tastatură), apoi afișează pe ecran rezultatul'''

# Variation one, with the 'for' cycle

factorial = 1

number_to_factor = int(
    input('Kindly provide a positive basis for the factorial function: '))

if (number_to_factor < 0):
    print('Factorial can not be calculated for a negative basis')
elif (number_to_factor == 0):
    print(f'The factorial of the 0= {factorial}')
else:
    for i in range(1, number_to_factor + 1):
        factorial = factorial*i
    print(f'The factorial of the {number_to_factor}= {factorial}')


# Variation two, with the 'while' cycle; uncomment if necessary
# factorial = 1

# number_to_factor = int(
#     input('Kindly provide a positive basis for the factorial function: '))
# initial_input = number_to_factor

# if (number_to_factor < 0):
#     print('Factorial can not be calculated for a negative basis')
# elif (number_to_factor == 0):
#     print(f'The factorial of the 0= {factorial}')
# else:
#     while number_to_factor > 1:
#         factorial = factorial * number_to_factor
#         number_to_factor = number_to_factor - 1
#     print(f'The factorial of the {initial_input}= {factorial}')


# Variation three, with the 'math.factorial'; uncomment if necessary
# import math

# factorial = 1
# number_to_factor = int(
#     input('Kindly provide a positive basis for the factorial function: '))

# if (number_to_factor < 0):
#     print('Factorial can not be calculated for a negative basis')
# elif (number_to_factor == 0):
#     print(f'The factorial of the 0= {factorial}')
# else:
#     factorial = math.factorial(number_to_factor)
#     print(f'The factorial of the {number_to_factor}= {factorial}')
