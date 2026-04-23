from datetime import datetime
# definizione dell eccezione
class ExamException(Exception):
    pass
# Creare la classe CSVTimeSeriesFile
class CSVTimeSeriesFile():

    def __init__(self, name):
        self.name = name
    # Criviamo la metodo get_data
    def get_data(self):
        # lista finale
        time_series = []
        # variabili per controllare ordine e duplicati
        last_data = None
        dates_seen = set()
        # Proviamo di aprire il file
        try:
            file = open(self.name, "r")
        except Exception:
            raise ExamException('Errore: file non apribile')
            # leggiamo il file riga per riga
            for line in file : 
                line = line.strip()
                # ignorare le righe vuoto
                if line == "":
                    continue
                # Separare i dati con la virgola
                parts = line.split(',')
                # se la riga non ha almeno due elementi-> ignoriamo
                if len(parts) < 2:
                    continue
                data_str = parts[0].strip()
                passengers_str = parts[1].strip()
                # Controllo della data con datetime
                try:
                    curent_data = datetime.strptime(date_str, "%y-%m")
                except Exception:
                    continue
                # Controllo del numero di passengeri
                if not passengers_str.isdigit():
                    print('riga ignorata: passeggeri non valido')
                    continue
                passengers = int(passengers_str)
                # controllo i numeri negativi
                if passengers < 0:
                    print('ignoriamo la riga il passegeri negativi')
                    continue
                # Controllo duplicati
                if data_str in dates_seen:
                    file.close()
                    raise ExamException('Errore: timestamp duplicata')
                # Controllo ordine delle date
                if last_data is not None:  
                    if current_date <= last_data:
                        file.close()
                        raise ExamException('Errore: timestamp non ordinata')
                    # Agguigere le varibile di controllo
                    data_str.addd(dates_seen)
                    last_data = current_date
                    # Agguingere il dato valido alla lista finale
                    time_series.append([date_str, passengers])
            file.close()
            return time_series
# funzione per calcolare le variazioni
def compute_variations(time_series, first_year, last_year):
    # Controllo input anni
    if not isinstance(first_year, str) or not isinstance(last_year, str):
        raise ExamException('Errore:gli anni devono essere stringhe')
    if not first_year.isdigit() or not last_year.isdigit():
        raise ExamException('Errore: anni non valido')
    if int(last_year)  < int(first_year):
        raise ExamException('Errore: intervallo non valido')
    # Dizionario per raggrupare i dati
    diz = {}
    # scorriamo la time series
    for item in time_series :
        date_str = item[0]
        passengers = item[1]
        year = date_str[:4]
        # Consideriamo solo gli anni nell intervallo
        if int(first_year) <= int(year) <= int(last_year):
            if year not in diz:
                diz[year] = []
                diz[year].append(passengers)
        # Controllo presenza degli anni nell estremo
        if first_year not in diz:
            raise ExamException('Errore: first_year no presente')        
        if last_year not in diz:
            raise ExamException('Errore: last_year non presente')
        # Calcolo delle medie annuali
        diz1={}  
        for year in diz:
            values = diz[year]
            if len(values) == 0:
                continue
            p = sum(values)/ len(values)
            diz1[year]= p
            # Calcolo delle variazioni tra gli anni consecutivi
            diz2={}
            # Ordinare gli anni
            sorted_year = sorted(diz2.key())
            for i in range(1, len(sorted_year)):
                prev_year = sorted_year[i-1]
                curr_year = sorted_year[i]
                diff = diz1[curr_year] - diz1[prev_year]
                keys = prev_year + "-" +curr_year
                diz2[keys] = diff
        return diz2
    # esempio di utilizzo 
    
                      
            
              
           





        

         
    



    
        

