class CSVFile():

    def __init__(self, name):
        self.name = name

    def get_data(self):
        paul = []  

        try:

            with open(self.name, 'r') as file:

                for line in file:
                    p = line.strip().split(',')
                    paul.append(p)

        except FileNotFoundError:
            print('Errore: file non esiste')

        return paul
# Sottoclasse  NumericalCSVFile
class NumericalCSVFile(CSVFile):

    def get_data(self, *args, **kwargs):
        paul = super().get_data(*args, **kwargs) 

        new_paul= []               

        for row in paul:
            new_row =[]

            try:

                new_row.append(row[0])

                for item in row[1:]:
                    new_row.append(float(item))

                new_paul.append(new_row) 

            except FileNotFoundError:
                print('Errore:', row)  

        return new_paul             



             

              

    
 