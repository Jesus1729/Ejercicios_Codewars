# Linear Regression of Y on X

def regressionLine(x, y):
    """ Return the a (intercept)
        and b (slope) of Regression Line
        (Y on X).
    """
    n = len(x)
    x_square = list(map(lambda x:x**2,x))
    sum_x_square = sum(x_square)
    sum_y = sum(y)
    sum_x = sum(x)
    sum_xi_por_yi = sum([a*b for a,b in zip(x, y)])

    # Para "a"
    numerador_a = sum_x_square*sum_y - sum_x*sum_xi_por_yi
    denominador_a = n*sum_x_square - sum_x**2
    a= round(numerador_a/denominador_a,4)

    # Para b
    numerador_b = n*sum_xi_por_yi - sum_x*sum_y
    denominador_b = denominador_a
    b = round(numerador_b/denominador_b,4)

    return (a,b)

print(regressionLine([56,42,72,36,63,47,55,49,38,42,68,60], [147,125,160,118,149,128,150,145,115,140,152,155]))