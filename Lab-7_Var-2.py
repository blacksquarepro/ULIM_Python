'''Scrieți un program care citește de la tastatură date despre studenții unei grupe (nr., nume, prenume, localitate, adresă, telefon, notă medie ș.a.) sau despre lucrătorii unei întreprinderi (nr., nume, prenume, funcție, salariu, stagiu, localitate ș.a.) în dependență de condiție, le înscrie într-un fișier de pe disc, apoi le citește din fișier și afișează pe ecran doar acele persoane care satisfac condiția din variantă (este de dorit să creați un meniu care să permită: crearea fișierului; afișarea conținutului fișierului; adăugarea datelor; modificarea datelor; eliminarea datelor; prelucrarea datelor conform variantei; ieșirea din program ș.a.)'''
'''Conditia: De afișat studenții cu nota media mai mică decât 5 || studenții unei grupe (nr., nume, prenume, localitate, adresă, telefon, notă medie ș.a.)'''


import csv
def create_file():
    with open('Lab-7_Var-2.csv', 'w', newline='') as f:
        header = ['id', 'first_name', 'last_name', 'locality',
                  'address', 'phone', 'group', 'average_mark']
        writer = csv.DictWriter(f, fieldnames=header)
        writer.writeheader()


def list_file_contents(csv_file):
    with open(csv_file, 'r', newline='') as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            print(f'{", ".join(row)}')


def get_csv_header(csv_file):
    with open(csv_file, 'r', newline='') as f:
        reader = csv.reader(f, delimiter=',')
        headers = next(reader, None)
        return headers


def get_line_to_append():
    line_to_append = []
    for element in get_csv_header('Lab-7_Var-2.csv'):
        line_to_append.append(input(f'Kindly input the element "{element}": '))
    return line_to_append


def add_content(csv_file):
    with open(csv_file, 'a+', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(get_line_to_append())


def modify_data(csv_file):
    lines = []
    student_id = input("Please student's ID to be modified: ")

    with open(csv_file, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            lines.append(row)
            for field in row:
                if field == student_id:
                    print(f'Original row: {", ".join(row)}')
                    lines.remove(row)
                    lines.append(get_line_to_append())
    with open(csv_file, 'w', newline='') as f:
        writer = csv.writer(f)
        for line in lines:
            writer.writerow(line)


def delete_data(csv_file):
    lines = []
    student_id = input("Please student's ID to be deleted: ")

    with open(csv_file, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            lines.append(row)
            for field in row:
                if field == student_id:
                    print(f'Row {", ".join(row)} -> deleted')
                    lines.remove(row)
    with open(csv_file, 'w', newline='') as f:
        writer = csv.writer(f)
        for line in lines:
            writer.writerow(line)


def list_students_below_grade(csv_file):
    with open(csv_file, 'r', newline='') as f:
        reader = csv.reader(f, delimiter=',')
        next(reader, None)
        for row in reader:
            if (float(row[-1]) < 5):
                print(f'{", ".join(row)}')


def menu():
    user_action = ''
    while user_action != '*':
        user_action = input(
            'Kindly choose your action:\nl - list file contents\na - append new row\ne - edit data row\nd - delete row\ng - list students with the grade below "5"\n* - exit the program\nINPUT: ')
        print('================')
        if user_action == 'l':
            list_file_contents('Lab-7_Var-2.csv')
        elif user_action == 'a':
            add_content('Lab-7_Var-2.csv')
        elif user_action == 'e':
            modify_data('Lab-7_Var-2.csv')
        elif user_action == 'd':
            delete_data('Lab-7_Var-2.csv')
        elif user_action == 'g':
            list_students_below_grade('Lab-7_Var-2.csv')
        elif user_action == '*':
            print('Program finished successfully!')
            exit
        else:
            print('Wrong input, retry!\n')


create_file()
menu()
