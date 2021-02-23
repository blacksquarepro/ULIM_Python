'''Scrieți un program care prezintă diverse exemple de prelucrare a diferitor tipuri de excepție: atunci când avem împărțire la zero, radical din număr negativ, când încercăm să accesăm un element inexistent al unui tablou, când încercăm să accesăm un element în afara unui șir de caractere, atunci când în loc de număr utilizatorul introduce litere, atunci când încercăm să apelăm o metodă a unui obiect care are referință nulă etc. Pentru notă maximă trebuie de creat o metodă care generează excepție proprie.'''

import math


def division_by_zero_handling():
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    try:
        print(f"{a} / {b} is {a/b}")
    except ZeroDivisionError:
        print("ZeroDivisionError caught; can not divide by zero")


def negative_square_root_handling():
    a = float(input("Enter the number to extract a square root: "))
    try:
        print(math.sqrt(a))
    except ValueError:
        print("ValueError caught; can not use a negative number to extract a square root")


def no_dict_key():
    test_dictionary = {"country": "Moldova", "city": "Chisinau",
                       "population": 800000, "phone_code": "022", "has_airport": True}
    print(test_dictionary)

    a = str(input("Enter the key to retrieve the value: "))
    try:
        print(test_dictionary[a])
    except KeyError:
        print("KeyError caught; provided key is not in dictionary")


def out_of_range_error_handling():
    a = str(input("Enter the string to be used as a reference: "))
    b = int(
        input("Enter the position of the character you want to get (positive int): "))
    try:
        print(a[b])
    except IndexError:
        print("IndexError caught; provided index is out of range")


def value_error_handling():
    try:
        a = int(input("Enter an integer number: "))
        print(a)
    except ValueError:
        print("ValueError caught; provided input is not an integer number")


#==============================CUSTOM EXCEPTIONS IMPLEMENTATION AND HANDLING=======================================#

class HumanComfortableTemperatureException(Exception):
    """Exception raised for errors in the input temperature.
    Attributes:
        temperature -- input temperature which caused the error
        exceptionmessage -- explanation of the error
    """

    def __init__(self, temperature, exceptionmessage="Temperature is not in (18, 26) range"):
        self.temperature = temperature
        self.exceptionmessage = exceptionmessage
        super().__init__(self.exceptionmessage)

    def __str__(self):
        return f'{self.temperature} -> {self.exceptionmessage}'


human_comfortable_temperature = int(input(
    "Enter the temperature comfortable for a human (hint: somewhere in-between 18 and 25 degrees celsius): "))
if not 18 <= human_comfortable_temperature <= 25:
    raise HumanComfortableTemperatureException(human_comfortable_temperature)
