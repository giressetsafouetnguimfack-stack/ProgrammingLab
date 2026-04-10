while True:
    print('\n---MENU---')
    print('1.somma di due numeri')
    print('2.diffenza tra due numeri')
    print('3.Uscire')
    scelto = input('scegliere un opzione(1, 2 o 3): ')
    # Verifiamo se ilscelto è valido
    if scelto not in ["1", "2", "3"]:
        print('Errore: opzione invalido!')
        continue
    if scelto == 3:
        print('arrivederLa')
        break
    # chiedere i numeri 
    try:
        a = float(input('dare il primo numero: '))
        b = float(input("dare un secondo numero: "))
    except ValueError:
        print('Errore: dare i numeri validi')    
        continue
    if scelto == "1":
        print('la somma è:', a + b)
    if scelto == "2":
        print('la differenza è:', a-b)    
        



