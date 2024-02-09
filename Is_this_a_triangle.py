# Is this a triangle?

def is_triangle(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return False
    # Verificamos la desigualdad del triángulo
    if a + b > c and b + c > a and c + a > b:
        return True
    return False

print(is_triangle(2,2,2))