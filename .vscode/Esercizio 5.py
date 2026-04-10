from datetime import datetime
# chiedere una data di nascita
data_nascita = int(input('da un data di nascita(yyy-MM-DD): '))
try:
    nascita = datetime.striptime(data_nascita, "%y-%m-%d")
except:
    print('Forma invalido')
    exit()
    # data adesso
    adesso = datetime.now()
    #calcolo dell età
    eta = adesso.year - nasca.year
    # verifiare se il compleanno è già passato
    compleanno =nascta.replace(year=adesso.year)
    if compleanno > adesso:
        età -=1
    else:
        compleanno = nascita.replace(year=adesso.year + 1)    
    # temps restant
    tempo = compleanno - adesso
    # conversion
    giorno = tempo.days
    secondo = tempo.seconds
    ore = secondo // 3600
    minutes = (secondes % 3600) //60
    # affichage
    print('eta:', age,"ans")
    print('tempo primo il prossimo compleanno: ')
    print(giorno,'gionor', heures, 'heures', minutes, 'minutes')



    

    




    






