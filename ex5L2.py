n = int(input("date un numero: "))
if n <= 1 :
        print("numero non primo")
else:
    for i in range(2, n) :
        if n % i == 0 :
                print("numero non primo") 
        else :
                print("numero primo")                





        
