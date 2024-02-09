# Histogram - H1

def histogram(l):
    s = ""
    l.reverse()
    for index, value in zip(range(len(l), 0, -1), l):
        if value != 0:
            s += f"{index}|{'#'*value} {value}\n"
        else:
            s += f"{index}|\n"
    return s

print(histogram([3,3,4,6,7,7]))