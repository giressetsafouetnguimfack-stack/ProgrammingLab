class CSVFile():
    # inizializzatione
    def __init__(self, name):
        self.name = name
    # Ritorna i dati dal file CSV come liste di liste
    def get_data(self):
        paul = []
        
        try:

            file = open(self.name, "r") # aprire il file

            for line in file:
                p = line.strip().split(',')
                paul.append(p)

            file.close() 

        except FileNotFoundError:
            print('Errore : il file non esiste') # il messaggio

            return paul          

# Esempio
file = CSVFile('shampoo.csv')
print(file.get_data())            


             
                

                




               

    
    







        