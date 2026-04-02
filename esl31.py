# Esercisio 1 lez4 Classe Veicolo
class Veicolo():

    def __init__(self, anno, modelle, marca):
        # fissiamo modello,marca,anno,speed
        self.anno = anno
        self.modello = modelle
        self.marca = marca
        self.speed = 0

    def __str__(self):
        # Detagli dei veicole
        return('marca: "{}", modello: "{}",  anno: {}, velocità: {})'.format(self.marca, self.modello, self.anno, self.speed))

    def accellerare(self):
        # Agguingere 5 all attributo dati speed
        self.speed = self.speed + 5
        
    def frenare(self):
        # Sottrae 5 dall attributo dati speed
        self.speed = self.speed - 5
        
    def get_speed(self):
        # Restituisce la velocità corrente
        return('{}'.format(self.speed))  
# Esempio
v = Veicolo(2020, "yaris", "Toyota")
print(v)
v.accellerare()
v.accellerare()
print(v.get_speed())
v.frenare()
print(v.get_speed())



        