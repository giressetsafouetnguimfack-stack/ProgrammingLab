def conta_lettera(parola, lettera):
    return parola.count(lettera)
parola = input('Inserire una parola: ')    
lettera = input('Inserire una lettera: ')
print('La lettera appare',
      conta_lettera(parola, lettera), "volte")
      