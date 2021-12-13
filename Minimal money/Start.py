print('')

try:
    f = open('File.txt')
    content = f.read().splitlines()
    for idx, ele in enumerate(content):
        if not ('€' in ele and any(c.isdigit() for c in ele)):
            while True:
                content[idx] = input('Ungültiger Betrag in der Datei, geben Sie bitte einen Eurobetrag an: ')
                if '€' in content[idx] and any(c.isdigit() for c in content[idx]):
                    break
except:
    while True:
        content = [input('Ungültiger Betrag, geben Sie bitte einen Eurobetrag an: ')]
        if '€' in content[0] and any(c.isdigit() for c in content[0]):
            break

i = 0
for j in content:
    content[i] = content[i].replace('€', '')
    i += 1

content = list(map(float, content))

for idx, ele in enumerate(content):
    a = divmod(ele, 500)
    b = divmod(round(a[1], 2), 200)
    c = divmod(round(b[1], 2), 100)
    d = divmod(round(c[1], 2), 50)
    e = divmod(round(d[1], 2), 20)
    f = divmod(round(e[1], 2), 10)
    g = divmod(round(f[1], 2), 5)
    h = divmod(round(g[1], 2), 2)
    i = divmod(round(h[1], 2), 1)
    j = divmod(round(i[1], 2), 0.50)
    k = divmod(round(j[1], 2), 0.20)
    l = divmod(round(k[1], 2), 0.10)
    m = divmod(round(l[1], 2), 0.05)
    n = divmod(round(m[1], 2), 0.02)
    o = divmod(round(n[1], 2), 0.01)
    print('')
    string = str(content[idx]) + '€: ' + int(a[0]) * '500€ + ' +\
                                       + int(b[0]) * '200€ + ' +\
                                       + int(c[0]) * '100€ + ' +\
                                       + int(d[0]) * '50€ + ' +\
                                       + int(e[0]) * '20€ + ' +\
                                       + int(f[0]) * '10€ + ' +\
                                       + int(g[0]) * '5€ + ' +\
                                       + int(h[0]) * '2€ + ' +\
                                       + int(i[0]) * '1€ + ' +\
                                       + int(j[0]) * '50ct + ' +\
                                       + int(k[0]) * '20ct + ' +\
                                       + int(l[0]) * '10ct + ' +\
                                       + int(m[0]) * '5ct + ' +\
                                       + int(n[0]) * '2ct + ' +\
                                       + int(o[0]) * '1ct + '
    print(string[:-2] + '\n')