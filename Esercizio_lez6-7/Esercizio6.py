valore = input('dare un numero intero: ')
try:
    numero = int(valore)
    print('il quadrato è:', numero**2)
    
except ValueError:
    print('Errore: dare un numero intero valido')  

           
