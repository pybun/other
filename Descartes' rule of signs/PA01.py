def sign(z):
    if z >= 0:
        return 1
    else:
        -1

def roots(a, b, c, d, e, f):
    array = [a, b, c, d, e, f]

    c = sum(sign(x) != sign(y) for x, y in zip(array, array[1:]))

    if c % 2 == 0:
        print('Das Polynom hat eine gerade Anzahl von positiven reellen Wurzeln.') 
    else:
        print('Das Polynom hat eine ungerade Anzahl von positiven reellen Wurzeln.')