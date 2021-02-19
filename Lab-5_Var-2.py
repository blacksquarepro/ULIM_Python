''' Diferența a două mulțimi'''

# Uncomment when necessary

# def define_set():
#     resulting_set = set()
#     counter = 0
#     user_input = 0

#     while user_input != '*':
#         user_input = input(
#             f'Define the element {counter+1}, or input "*" to exit: ')
#         if (user_input != '*'):
#             counter += 1
#             resulting_set.add(user_input)

#     print(resulting_set)
#     return resulting_set


# print('Define set #1')
# set_1 = define_set()

# print('Define set #2')
# set_2 = define_set()

# print(f'Intersection elements are: {set_1.intersection(set_2)}')


'''Creați un dicționar format din minim zece perechi „cheie- valoare”, care reprezintă definiții ale noțiunilor studiate pe parcursul studiilor la specialitatea Dvs., tema fiind indicată mai jos, în variantă, apoi prezentați diferite metode de lucrul cu dicționarele'''

# Uncomment when necessary

def define_dictionary():
    dict_len = int(input('Define the length of the dictionary >10: '))
    dict = {}

    if dict_len > 10:
        for i in range (0, dict_len):
            key = input(f'Define key {i+1}: ')
            value = input(f'Define value {i+1}: ')
            dict.update({key:value})
    else:
        print('The length is incorrect, restart the program')
        exit()
    
    print(dict)
    return dict

# define dict 1
print('Define dictionary #1')
dict_1 = define_dictionary()

# define dict 2
print('Define dictionary #2')
dict_2 = define_dictionary()

# sample - return dict_1 keys
print(dict_2.keys())

# sample - return dict_2 items
print(dict_2.items())