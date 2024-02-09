# Rubik's Cube Art

def cube(n):
    lista1 = []
    for i in range(1,n+1):
        t = ' '*(n-i)  + '/\\'*i   + '_\\'*n + '\n'
        lista1.append(t)
    lista2 = []
    for i in range(n):
        t = ' '*(i) + '\\/'*(n-i) + '_/'*n
        if i < n-1:
            t += '\n'
            lista2.append(t)
        else:
            lista2.append(t)

    lista3 = lista1 + lista2
    aux = ""
    for i in lista3:
        aux += i

    return aux

print(cube(4))