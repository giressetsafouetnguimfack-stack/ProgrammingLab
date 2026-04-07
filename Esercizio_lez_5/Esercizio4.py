class Poligono():

    def __init__(self, numero):
        self.numero = numero
    
    def descrizione(self):
        # Descrizione del poligono
        return f"Sono un poligono con {self.numero} lati"
    
# Sottoclasse Quadrilatero
class Quadrilatero(Poligono):

    def __init__(self):
        super().__init__(4)

    def descrizione(self):
        # Descrizione Quadrilatero
        return f"Sono un quadrilatero"
      
# Sottoclasse Rectangolo
class Rettangolo(Quadrilatero):

    def __init__(self, base, alteza):
        super().__init__()
        self.base = base
        self.alteza = alteza

    def descrizione(self):
        # descrizione Rettangolo
        return f"Sono un Rettangolo di base: {self.base} e di alteza: {self.alteza}"  
             
    def perimetro(self):
        # calcolo del perimetro
        return 2*(self.alteza + self.base)
    
    def area(self):
        # calcolo del area
        return self.base + self.alteza
    
# Sottoclasse Triangolo
class Triangolo(Poligono):

    # Inizializzazione
    def __init__(self, alteza1, alteza2,alteza3):
        super().__init__(3)
        self.alteza1 = alteza1
        self.alteza2 = alteza2
        self.alteza3 = alteza3

    def descrizione(self):
        # Descrizione Triangolo
        return f"Sono un Triangolo che a per i lati: {self.alteza1}, {self.alteza2}, {self.alteza3}"
    
    def perimetro(self):
        # Calcolo del perimetro
        return self.alteza1 + self.alteza2 + self.alteza3
    
    def is_equilatero(self):
        # verifcare se il triangolo è equilatero
        if self.alteza1 == self.alteza2 == self.alteza3:
            return True
        

# Esempio
p = Poligono(5)        
print(p.descrizione())

q = Quadrilatero()
print(q.descrizione())

r = Rettangolo(10, 5)
print(r.descrizione())
print("Perimetro:", r.perimetro())
print("Area:", r.area())

t = Triangolo(3,3,3)
print(t.descrizione())
print("Perimetro:", t.perimetro())
print("Equilatero:", t.is_equilatero())


        
        





        
       


      

            
        