def tipo_triangolo(a, b,c):
    if a+b > c and a+c > b and b+c > a:
        if a == b == c:
            return'Triangolo equilatero'
        elif a == b or b == c or a == c:
            return'Triangolo isoscele'
        else:
            return 'Triangolo scaleno'
    else:
        return'Non è un triangolo'
a = int(input('lato 1: '))            
b = int(input('Lato 2: '))
c = int(input('Lato 3: '))
