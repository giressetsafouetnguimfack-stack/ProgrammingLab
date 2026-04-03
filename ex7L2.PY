def fattoriele(n) :
    fattoriele = 1
    for i in range(1, n+1):
        fattoriele = fattoriele*i
    return(fattoriele)
print(fattoriele(3))



