# Strong Number (Special Numbers Series #2)

def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact*=i
    return fact

def strong_num(number):
    s = str(number)
    suma = 0
    for i in s:
        suma += factorial(int(i))
    if suma == number:
        return "STRONG!!!!"
    else:
        return "Not Strong !!"

print(strong_num(8))