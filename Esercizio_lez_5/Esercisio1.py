class Persona:
    def __init__(self, ruolo, nome, cognome):
        self.ruolo = ruolo
        self.nome = nome
        self.cognome = cognome

    def saluta(self):
        print('Ciao sono',self.ruolo + ":", self.nome, self.cognome)

class Studente(Persona):
    # Costruttore sotto_classe
    def __init__(self, nome, cognome, corsi):
        super().__init__("Studente UNITS", nome, cognome)
        self.corsi = corsi

    def saluta(self):
        # Costruttore sotto_class
        Persona.saluta(self)
        print("Frequento i corsi:")
        for corso in self.corsi:
            print("_", corso)

class Docente(Persona):
    def __init__(self, nome, cognome, corsi):
        super().__init__("Docente UNITS", nome, cognome)
        self.corsi = corsi

    def saluta(self):
        Persona.saluta(self) # Uso exsplicamente metodo di persona
        print(">Docente dei corsi:") 
        for corso in self.corsi:
            print("_", corso)

# Esempio
corsi = ["Programmazione", "Laboratorio", "Analisi", "Geometria"]
obj_Irene = Studente("Irene", "Rossi", corsi)
obj_Irene.saluta()
                   