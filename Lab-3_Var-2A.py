'''Scrieți un program care efectuează ceea ce este indicat în variantă, utilizând funcții, apoi afișează pe ecran rezultatul. Utilizarea cel puțin a unei funcții care întoarce valori, declarată de Dvs., este obligatorie. De asemenea este obligatoriu ca funcția să aibă cel puțin un parametru cu valoare implicită. Se cere să prezentați diverse exemple de apel: cu valori citite de la tastatură, cu valori scrise direct, de diferite tipuri de date, inclusiv șir de caractere. Pentru a primi nota maximală se cere de utilizat și o funcție cu număr variabil de parametri'''

from statistics import geometric_mean


def get_iterable():
    iterable = []
    user_input = input('Enter the positive number, * to stop: ')
    while (user_input != '*'):
        if (float(user_input) >= 0):
            iterable.append(float(user_input))
            user_input = input('Enter the positive number, * to stop: ')
        else:
            print("The number is negative, please add another positive number")

    return iterable


iterable = get_iterable()
geo_mean = geometric_mean(iterable)
print(geo_mean)
