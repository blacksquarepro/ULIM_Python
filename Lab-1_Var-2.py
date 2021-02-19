'''Scrieți o secvență de instrucțiuni care citește de la tastatură valoarea variabilei x, calculează valoarea expresiei indicate în variantă, apoi, îndeplinește următoarele: dacă variabila y este negativă, afișați pe ecran mesajul „y este negativ, y= valoare calculată”; dacă variabila y este nulă afișați că y este nul, iar dacă y este pozitivă afișați mesajul „y este pozitiv, y= valoare calculată”. Demonstrați din punct de vedere matematic că rezultatul oferit de program este cel corect. Fiți atenți să nu apară erori matematice de genul împărțirii la zero, radical sau logaritm din număr negativ, tangentă sau cotangentă infinită etc.'''

'''Lab 1, Varianta 2
y = (cos(x)+(7*x))/((x^4)-(3*(x^2)))
'''


import math
x = int(input('Please indicate the value of the x: '))
y = (math.cos(x)+(7*x))/((x ^ 4)-(3*(x ^ 2)))

if y < 0:
    print(f'y is negative\ny= {y}')
elif y > 0:
    print(f'y is positive\ny= {y}')
else:
    print('y is nil')
