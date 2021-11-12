def roots(a, b, c, d, e, f):
    polynomial = [1, a*d, a*e+b*d, a*f+b*e+c*d, b*f+c*e, c*f]

    last_sign = 1
    sign_changes = 0

    for x in polynomial:
        if x != 0:
            sign = x / abs(x)
        if sign == -last_sign:
            sign_changes += 1
            last_sign = sign

    if sign_changes % 2 == 0:
        return 'Das Polynom hat eine gerade Anzahl von positiven reellen Wurzeln.'
    else:
        return 'Das Polynom hat eine ungerade Anzahl von positiven reellen Wurzeln.'
