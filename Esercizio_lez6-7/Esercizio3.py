class CSVFile():

    def __init__(self, name):
         # Verificare se il nome del file è un string
        if not isinstance(name, str):
            raise('Errore: il nome del file deve essere un string')
        self.name = name

    def get_data(self, start=None, end=None):
        paul = []

        try:

            file = open(self.name, "r")
                
            for line in file:
                p = line.strip().split(',')
                paul.append(p)

            file.close() 

        except FileNotFoundError:
            print('Errore: il file non esiste')
            return []
            
        # Geszione di start e end
        if start is None:
            start = 1
        if end is None:
                end = len(paul)
        # Securisare i valore
        if start < 1:
            start = 1
        if end > len(paul):
            end = len(paul)
        if start > end:
            return[]    

        return paul[start-1 : end] 
         
# Esempio
file =CSVFile( "shampoo_sales.csv")
print(file.get_data(2,3))
        



 
            



                    
                    




        
 
 