from datetime import datetime
# creare un data di nascita
data_nascita = input('inserire una data di nascita("YYY-MM-DD): ')
# conversione in data
data_nascita = datetime.strptime(data_nascita, "%y-%m-%d")
# data di oggi
oggi = datetime.now()
# calcolare èta
età = oggi.year - data_nascita.year
# verificare se il compleanno è gia passato questa anno
if((oggi.month, oggi.day) < (data_nascita.month, data_nascita.day)):
    età -= 1
    print(f'Età:{età} anni')
# prossimo compleanno
prossimo_compleanno = datetime(oggi.year, data_nascita.month, data_nascita.day)    
if prossimo_compleanno < oggi:
    prossimo_compleanno = datetime(oggi.year+1, data_nascita.month, data_nascita.day )
# il tempo per il prossimo compleanno
tempo_restante = prossimo_compleanno - oggi
giorni = tempo_restante.days
secondi = tempo_restante.seconds
ore = secondi // 3600
minute = (secondi % 3600) // 60
secondi = secondi % 60
#risutati
print('tempo fino al prossimo compleanno:')
print(f"{giorni} giorni, {ore} ore, {minute} minuti, {secondi}secondi")
