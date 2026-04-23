def conta_vocali(stringa):
    vocali = 'aeiouAEIOU'
    conteggio = 0
    for lettera in stringa:
        if lettera in vocali:
            conteggio += 1
    return conteggio
testo = input('Inserire una stringa: ')
print('Numero di vocali:',
conta_vocali(testo))
        