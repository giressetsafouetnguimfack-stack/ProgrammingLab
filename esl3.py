# Esercisio/ Esempio Lez4

import random
class Coin: 

    def __init__(self, faccia):
        self.faccia = faccia

    def lancia(self):
        # Similare il lanciato della moneta
        self.faccia = random.choice(["testa", "croce"])
       
    def valore(self):
        # Ritorna il valore di faccia
        return('{}'.format(self.faccia))
# Esempio    
p = Coin("faccia")
p.lancia()
print('valore della faccia:', p.valore())


        
