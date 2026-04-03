# Esercisio 1
def conteggio (lista):
    diz= []
    for n in lista: 
        if len(n) >= 5:
            if n in diz:
                diz[n] += 1
            else:
                diz[n] = 1
    return(diz)               

# Esercisio 2
def vendite (pongo, limite):
    som=0
    file= open("pongo", "r")  
    for line in pongo:
        line= line.strip()
        line= float(line)
        if line > limite:
            som += line
    file.close()        
    return(som)        

# Esercisio 3
def majuscule (baba, parola):
    som= 0
    file= open("baba", "r")
    paul= file.read()
    file.close()
    boris= paul.split("_")
    for n in boris:
        if n.lower() == parola.lower():
            som += 1
    return(som)        

# Esercisio 4
def lunghezza (ivan):
    file= open("ivan", "r")
    bell= file.read()
    file.close()
    diz= {}
    pol= bell.split("_")
    for n in pol: 
        if len(n) in diz:
            diz[len(n)] += 1
        else:
            diz[len(n)] = 1
    return(diz)  

# Esercisio 5
def unique (arial):
    file= open("ariel", "r")        
    papa= file.readlines()
    file.close()
    oscar=[]
    new= open("ordinate.txt", "w")
    for line in papa:
        if line not in new:
            oscar.append(line)
            new.write(line)
    new.close()   

# Esercisio 6
def pair (lista):
    som= 0
    for n in lista:
        if n % 2 == 0:
            som += n
    return(som) 

# Esercisio7
def comune (lista1, lista2):
    lista3= []   
    for n in lista1:
        if n in lista2 :
            if n not in lista3:
                 lista3.append(n)
    return(lista3)        

# Esercisio 8
def palin (lista):
    new=[]
    for n in lista:
        if n== n[ :: -1]:
            new.append(n)
    return(new)        


      





        



            


            


            
           

