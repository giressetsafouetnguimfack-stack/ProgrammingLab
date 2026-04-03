# Esercisio 3 Lez4
class CSVFile():

    def __init__(self, name):
        self.name = name


    def get_data(self):
        paul = []

        file = open(self.name, "r")
        next(file)

        for line in file:
            line = line.strip() 
            p = line.split(',')
            if p not in paul:
                paul.append(p)

        file.close()
        return(paul)
    

file = CSVFile("shampoo_sales.csv")      
print(file.get_data())



        
   