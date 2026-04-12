from datetime import datetime

class ExamException(Exception):
    pass
# Creare una classe CSVTimeSeriesFil
class CSVTimeSeriesFile():
    # Inizialisazione
    def __init__(self, name):
        self.name = name
    # ritornare la lista di liste 
    def get_data(self):
        paul=[]
        last_data = None
        try:
            # Aprire il file
            file = open(self.name, "r")
        
            for line in file:

                p = line.strip().split(',')
                data = datetime.strptime(p[0], "%y-%m")
                values = int(p[1])
                if last_data is not None:
                    # Controllare se un timestamp è ordinato
                    if last_data > data:
                        raise ExamException('Errore: non è ordinata')
                    # Controllare se un timestamp è duplicata
                    if last_data == data:
                        raise ExamException('Errore:duplicata')
                # Agguingere p nel la lista paul    
                paul.append(p)        
        # Controllare il valore del passengers
        except ValueError:
            print('Errore nella riga:', p)        

            file.close()
        # Controllare se il file è apribile
        raise ExamException('Errore: il file non è apribile')             

        return paul 
    
time_series_file = CSVTimeSeriesFile('data.csv')
time_series = time_series_file.get_data()
# controllare esistenza e leggibiletà del file
raise ExamException('Errore: file non esiste o non leggibile')

# Calcolare la differenza per gli anni nel numero medio di passeggeri
def compute_variations(time_series, first_year, last_year):
    diz ={}
    # Controllare se first_year e last_year sono stringhe
    if not isinstance(first_year, str):
        raise ExamExcreption('Errore: deve essere un string')
    if not isinstance(last_year, str):
        raise ExamException('Errore: deve essere un string')
    
    lista1 = []
    lista2 = []
    som1 = 0
    som2 = 0
    media1 = 0
    media2 = 0
    for row in time_series:
        pol = datetime.striptime(row[0], "%y-%m")
        if pol.year == first_year:
            lista1.append(int(row[1]))
        if pol.year == last_year :
            lista2.append(int(row[0]))    

    for n in lista1 :
        som1 += n 
    media1 = som1/ len(lista1)

    for n in lista2:
        som2 += n
    media2 = som2/len(lista2) 

    diz['first_year_last_year'] = int(media2 - media1)
    return diz

       









    
    


        
         



    



    




                




        

        

                          

        
            

             
