# Esercizi 1 Lez3
# Domanda 1
def paul (t):
    som =0
    for n in t:
        som+= n
    return(som)
t2=[2,3,5,4]  
print(paul(t2))   

# Domanda 2
def palindromo (s):
    if s == s[::-1]:
        return(True)
    else:
        return(False) 
s2="cia"       
print(palindromo(s2))

# Domanda 3
def scambia (A, i, j):
    temp=A[i]
    A[i]= A[j]
    A[j]=temp
A2=[2,3,4,5,6,7]
scambia(A2, 1, 4)
print(A2)

# Domanda 4
def comune (B, D):
    for n in B :
        if n in D:
           return(True)  
B4=[2,4,8,]      
D4=[2,7,4]
print(comune(B4, D4))

# Domanda 5
def numeri (F):
    parole=[ "zero","uno", "due", "tre", "quattro", "cinque","sei", "sette", "otto", "nove"]
    P=[]
    for n in F:
        P.append(parole[n])
    return(P)         
F5=[7,3,5,6,9] 
print(numeri(F5))








  

    


        

 

