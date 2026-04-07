class Veicolo():
    def __init__(self, anno, modello, marca):
        self.anno = anno
        self.modello = modello
        self.marca = marca
        self.speed = 0

    def __str__(self):
        # Detagli dei veicolo
        return('marca:"{}", modello: "{}", anno: "{}",velocità: "{}"'.format(self.marca, self.modello, self.anno, self.speed))

    def accellare(self):
        # Agguingere 5 all attributo di speed
        self.speed += 5

    def frenare(self):
        # sotrae 5 all attributo di speed
        if self.speed < 5:
            print(la velocità non puo essere negtiva )       
        
        