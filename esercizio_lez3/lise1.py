# Esercisio 2 Lez3

# Domanda 1
def Parole (lista):
    diz={}
    for n in lista:
        if n in diz:
            diz[n] += 1
        else:
            diz[n] = 1
    return(diz)  
lista1=["Paul", "Laura", "Eros","Laura"]  
print(Parole(lista1)) 

# Domanda 2
def vendite (shampoo):
    som=0
    file = open(shampoo, "r")
    next(file)
    for line in file:
        p = line.strip().split(",")
        line = p[1]
        line =float(line)
        som +=line
    file.close()    
    return(som) 
file = "shampoo_sales.csv"
print(vendite(file))

# Domanda 3
def conta (conta, parola):
    som= 0
    file= open("conta", "r")
    paul= file.read()   
    file.close()
    papa= paul.split(",")
    for p in papa:
        if p == parola :
            som += 1
    return(som)        

# Domanda  
def prend (polo):
    diz= {}
    file= open("polo", "r")
    long= file.read()
    file.close()
    pongo= long.split(",")
    for n in pongo:
        if n in diz:
            diz[n]+= 1
        else:
            diz[n]= 1
    return(diz)   

# Domanda 5
def banda (baba):
    file= open("baba", "r")
    boris= file.readlines
    file.close()
    site= []
    new_file= ("unique.txt", "w")
    for line in boris:
        if line not in site:
            site.append(line)
            new_file.write(line)
    new_file.close()      










