class CSVFile():
    # Inizializzazione
    def __init__(self, name):
        self.name = name

    def get_data(self):
        # Ritornare i dati dal file CSV come lista di liste
        paul =[]
        file = open(self.name, "r")
        next(file)

        for line in file:
            p= line.strip().split(',')
            paul.append(p)

        file.close()        
        return(paul)        
# Esempio
file = CSVFile("shampoo_sales.csv")
print(file.get_data())





        
 
 
 