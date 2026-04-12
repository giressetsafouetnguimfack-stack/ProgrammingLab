class ExamException(Exception):
    pass
# creare la classe MovingAverage
class MovingAverage():
    # Inizilisazione
    def __init__(self, window_length):
        # Controllo su windoew_length
        if not isinstance(window_length, int) and (window_length > 0):
            raise ExamException('Errore:la lunghezza della finestra deve essere un intro positivo')
            self.window_length = window_length
    # scrivere la metodo computer
    def compute(self, lista):
        # controllo su data nel metodo compute
        if not isinstance(lista, list):
            raise ExamException('Errori:lista deve essere un list')
        for elemento in lista:
            if not isinstance(elemento, (int, float)):
                raise ExamException('Errore: gli elementi devono essere numeri')
            
        data = []
        self.lista = lista
        #controllo su la longhezza della lista e quella della finesta
        if len(self.lista) < self.window_length:
            raise ExamException('Errore : la lunghezza della lista deve essere almeno pari alla lunghezza dellla finestra')
        # calcolare la media
        for i in range(len(self.lista) - self.window_length + 1):
            finestra = lista[i:i+ self.window_length]
            media = sum(finestra)/ self.window_length

            data.append(float(media))
        return data    



               


        

