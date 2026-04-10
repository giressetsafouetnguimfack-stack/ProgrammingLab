class CSVFile():

    def __init__(self, name):
        self.name = name

    def get_data(self):

        paul= []
        try:

            file = open(self.name, 'r')
            next(file)

            for line in file:
                p = line.strip().split(',')
                paul.append(p)

            file.close()  

        except FileNotFoundError:
            print('Errore: il file non esiste ')

        return paul

# Sottoclasse NumericalCSVFile
class NumericalCSVFile(CSVFile):

    def  get_data(self):
        paul = super().get_data() # ricuperare i dati   
        new_paul = [] 

        for row in paul:
            new_row = [] 

            try:

                new_row.append(row[0])

                for item in row[1:]:
                    new_row.append(float(item))

                new_paul.append(new_row)  
            except:
                print('Errore sulla linea', row)   

        return new_paul
# Exempio
file = NumericalCSVFile('shampoo_sales.csv')  
print(file.get_data())              








        
                






            



        




                


     