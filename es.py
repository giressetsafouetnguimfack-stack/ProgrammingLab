# Esercisio 1

class Etudiant():

    def __init__(self, nom, age):
        # fissiamo nom e age
        self.nom = nom
        self.age = age

    def __str__(self,):
        return('Etudiant "{}", {} ans'.format(self.nom, self.age))   

    def se_presenter(self):
        print('je m appelle {} et j ai {} ans.'.format(self.nom, self.age))

e = Etudiant("paul", 20)    
e.se_presenter()
print(e)


#Esercisio 2

class Voture():

    def __init__(self, marque, vitesse):
        # fissiamo marque et vitesse
        self.marque = marque
        self.vitesse = vitesse

    def __str__(self):
        return('Voture : "{}", {}'.format(self.marque, self.vitesse))
        
    def accelerer(self):
        # augmentons la vitesse de +10
        self.vitesse = self.vitesse + 10
        return('{}'.format(self.vitesse))

v = Voture("Toyota", 50)
v.accelerer()
print(v.vitesse)
print(v)

# Esercisio 3

class Personne:
    pays = "Cameroun"

    def __init__(self, nom):
        self.nom = nom

    def __str__(self):
        return('Personne "{}"'.format(self.nom))
    
p = Personne("jean")
print(p)
print(p.pays) 

# Esercisio 4

class CompteBancaire():

    def __init__(self, solde):
        self.solde = solde

    def __str__(self):
        return('CompteBancaire {}'.format(self.solde))    

    def depose(self, montant):
        self.solde = self.solde + montant
        return('{}'.format(self.solde))    

    def retirer(self, montant):
        self.solde = self.solde - montant
        return('{}'.format(self.solde))    

c = CompteBancaire(1000)        
c.depose(500)
c.retirer(200)
print(c.solde)

# Esercisio 5

class Livre():

    def __init__(self, titre, auteur):
        self.titre = titre
        self.auteur = auteur

    def __str__(self):
        return('Livre "{}-{}"'.format(self.titre, self.auteur))

l = Livre("python", "Kana")        
print(l)

# Esercisio 8

class Rectangle():
    def __init__(self, longueur, largeur):
        self.longueur = longueur
        self.largeur = largeur

    def surface(self):
        return(self.longueur * self.largeur) 
           
    def perimetre(self):
        return 2*(self.longueur + self.largeur)
       
r = Rectangle(5, 3)
print(r.surface())
print(r.perimetre())



        
    

        







        






        
    



