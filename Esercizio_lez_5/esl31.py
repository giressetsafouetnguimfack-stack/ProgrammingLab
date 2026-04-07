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
        self.speed += 5
        
    def frenare(self):
        # Sottrae 5 dall attributo dati speed
        if self.speed < 5:
            print("La velocita non puo essere negativa")
        else:
            self.speed -= 5
        
    def get_speed(self):
        # Restituisce la velocità corrente
        return('{}'.format(self.speed))
    
class Auto(Veicolo):
# Costrutore sotto_classe
    def __init__(self, anno, modelle, marca, numero_porte):
        super().__init__(anno, modelle, marca)
        self.numero_porte = numero_porte 

    def __str__(self):
        return super().__str__() + f" numero_porte: {self.numero_porte}"  


class Moto(Veicolo):
    # Costrutore sotto_classe
    def __init__(self, anno, modelle, marca, tipo):
        super().__init__(anno, modelle, marca)
        self.tipo = tipo

    def __str__(self):
        return super().__str__() + f"Tipo: {self.tipo}"  

# Esempio
v = Veicolo(2020, "yaris", "Toyota")
print(v)
M = Moto(2022, "ML", "Mercedes", "Spotiva")
print(M)
A = Auto(2018, "yaya","Nanfan", 71)
print(A)



        