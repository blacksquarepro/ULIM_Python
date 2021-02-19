'''Programul care determină de câte ori litera „e” se conține într-un șir de caractere'''

user_input = str(input('Kindly input any arbitrary string: '))
print(f'The character "e" is contained in the string "{user_input}" for {user_input.count("e")} times')