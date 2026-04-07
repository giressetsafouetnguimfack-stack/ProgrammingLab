class Canguro():

    def __init__(self, contenuto_tasca= None):
        if contenuto_tasca is None:
            self.contenuto_tasca = []
        else:
            self.contenuto_tesca = contenuto_tasca 

    def intasca(self, x):
        # inserire oggetto in contenuto_tasca
        self.contenuto_tasca.append(x)

    def __str__(self):
        # Restituisce un stringa
        return('Canguro con testa: {}'.format(self.contenuto_tasca))
# Provare il codo
can = Canguro()        
guro = Canguro()
can.intasca(5)
can.intasca(18)
print("CAN:", can)
print("GURO:", guro)




          

    





        


        
