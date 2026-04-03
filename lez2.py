# Esercisio1
minutes = 538
heures = int(minutes/ 60)
reste = minutes % 60
print(heures, "h:", reste, "min")
# Esercio2
n = int(input("Entrez un nombre: "))
carre = n**2
cube = n**3
print("carre:", carre)
print("cube:", cube)
# Esercisio3
n = int(input("Entre un nombre: "))
if n % 2 == 0:
    print("Nombre pair")
else:
    print("Nombre impair") 
# Exercisio4
def table(mot, lettre):
    return mot.count(lettre)
print(table("banane", "a"))
#Exercisio5
n = int(input("Entrez un nombre: "))
premier = True
for i in range(2, n):
    if n % i == 0:
        premier = False 
if premier:
    print("Nombre premier")
else:
    print("pas premier")
# Exercisio6
somme = 0
n = int(input("Entre un nombre (0 pour arreter): "))            
while n != 0:
    somme = somme + n
    n = int(input("Entrez un nombre (0 pour arreter): "))
print("somme:", somme)
# Esercisio7
def factorielle(n):
    f = 1
    for i in range(1, n+1):
        f = f * i
    return f
print(factorielle(5))
# esercisio8
def triangle(a,b,c):
    if a+b>c and a+c>b and b+c>a:
        if a==b==c:
            print("Triangle equilaterale") 
        elif a==b or a==c or b==c:
            print("Triangle isocele")
        else:
            print("Triangle scalene") 
    else:
        print("pas un triangle") 
# Esercisio9
def comptevoyelle(texte):
    voyelles = "aeiou" 
    compteur = 0
    for lettre in texte:
        if lettre in voyelles:
            compteur +=1
    return compteur 
print(comptevoyelle("agriculture"))
    
