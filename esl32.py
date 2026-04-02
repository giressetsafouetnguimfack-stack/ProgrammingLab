# Esercisio 3 Lez4
class CSVFile():

    def __init__(self, name):
        # Initializziamo il nome del file
        self.name = name
    def get_data(self):
        paul = []
        file =open('self.name', "r")
        for line in file:
            line = line.strip 
            p = line.split(',')
            if p not in paul:
                paul.append(p)
        file.close()
        return(paul)      
        
   