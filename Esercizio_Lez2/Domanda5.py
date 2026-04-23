n = int(input('Inserire un numero: '))
if n < 2:
    print('Non è primo')
else:
    primo = True
    for i in range(2, n):
        if n % i == 0:
            primo = False
            break
    if primo:
        print('Numero primo')    
    else:
        print('Non è primo')    
