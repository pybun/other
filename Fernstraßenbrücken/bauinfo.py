# /usr/bin/python3
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
from math import radians, sin, cos, acos, floor

# ------------------------- Deutschlandkarte.txt -------------------------- #

def readMap():
    # Die x- und y- Koordinaten der Grenze Deutschlands, gespeichert in
    # „Deutschlandkarte.txt“, werden Zeile für Zeile eingelesen,
    # zurechtgeschnitten sowie in den dazugehörigen Listen als „float“-Werte
    # gespeichert und anschließend dem Plot übergeben; „zorder“ legt die
    # Reihenfolge der Ebenen fest – die Grenze wird dementsprechend nach ganz
    # unten platziert.
    x = []
    y = []
    with open('Deutschlandkarte.txt', encoding = 'utf-8') as file:
        for line in file:
            x.append(float(line.split()[0]))
            y.append(float(line.split()[1]))
    plt.plot(x, y, zorder = 0)

# --------------------------- Zustandsnoten.csv --------------------------- #

def readCsv():
    # In diesem Schritt wird „Zustandsnoten.csv“ eingelesen und die erste
    # Zeile – wo die Überschriften vorzufinden sind – übersprungen.
    list = []
    with open('Zustandsnoten.csv', encoding = 'utf-8') as file:
        next(file)
    # Anschließend werden die restlichen Zeilen eingelesen. Wenn die Spalten
    # von „NB“ sowie „OL“ ungleich 0 sind (manche beinhalten merkwürdigerweise
    # diese Zahl) werden „oben“, „unten“, „ZN“, „NB“ und „OL“ extrahiert sowie
    # der Liste „list“ hinzugefügt. Kommata werden durch Punkte und
    # Hochkommata durch Leerzeichen ersetzt und ersteres zu „float“
    # konvertiert.
        for line in file:
            if float(line.strip().split('\t')[10].replace(',', '.')) != 0\
            and float(line.strip().split('\t')[11].replace(',', '.')) != 0:
                list.append((\
                [line.strip().split('\t')[3].replace('"', '')],\
                [line.strip().split('\t')[4].replace('"', '')],\
                [float(line.strip().split('\t')[6].replace(',', '.'))],\
                [float(line.strip().split('\t')[10].replace(',', '.'))],\
                [float(line.strip().split('\t')[11].replace(',', '.'))]\
                ))
    return list

# -------------------------- Brücke oder Straße? -------------------------- #

def bOrS():
    # Es wird solange gefragt ob nach Brücken oder einer Straße gesucht wird,
    # bis „b“, „B“, „s“ oder „S“ eingegeben wurde.
    while True:
        choice = input('\nNach Brücken (b) oder einer Straße (s) suchen?: ')
        if choice == 'b' or choice == 'B' or choice == 's' or choice == 'S':
            break
    return choice

# --------------- Brücke: Geokoordinate oder Zustandsnote? ---------------- #

def gOrZ():
    # Wenn „b“ oder „B“ (Brücke) eingegeben wurde, besteht die nächste Frage
    # darin, ob die Brücken anhand einer Geokoordinate („g“ oder „G“) oder
    # einer Zustandsnote („z“ oder „Z“) gesucht werden sollen. Es wird wieder
    # solange gefragt, bis „g“, „G“, „z“ oder „Z“ eingegeben wurde.
    while True:
        choice = input('\nBrücken mit Geokoordinate (g) oder Zustandsnote (z)\
 suchen?: ')
        if choice == 'g' or choice == 'G' or choice == 'z' or choice =='Z':
            break
    return choice

# ------------------------- Brücke: Geokoordinate ------------------------- #

def g(list):
    # Wenn „g“ oder „G“ eingegeben wurde und dementsprechend mittels
    # Geokoordinate nach den Brücken gesucht werden soll, wird zunächst
    # der/die Benutzer/-in aufgefordert, die Koordinaten und den
    # gewünschten Umkreis einzugeben. Vom Programm werden nur Zahlen
    # akzeptiert, welche darauffolgend zu „float“ umgewandelt werden.
    print('\n#####################################################\
########\
##\n# Beispieleingabe:                                            #\
\n# Geokoordinate x: 8                                          #\
\n# Geokoordinate y: 50                                         #\
\n# Umkreis in km: 25                                           #\
\n###########################################################\
####')
    while True:
        try:
            gk_x = float(input('\nGeokoordinate x: '))
            gk_y = float(input('Geokoordinate y: '))
            umkreis = float(input('Umkreis in km: '))
            break
        except:
            print('Falsche Eingabe! Versuchen Sie es erneut.')
    print('Deutschlandkarte wird konstruiert ...\n')
    # Die Liste wird durchlaufen und übergibt die eingegebene x- sowie y-
    # Koordinate sowie „NB“ und „OL“ – welche zuvor zu einem Tupel
    # zusammengefasst wurden – an die Funktion „geodist“ weiter. Wenn der
    # Rückgabewert kleiner gleich dem eingebenenen Umkreis ist, werden die
    # Koordinaten des Indexes „i“ der neuen Liste „new_list“ hinzugefügt.
    new_list = []
    for i in list:
        if geodist((gk_y, gk_x), tuple([j[0] for j in i[3:]\
        if isinstance(j[0], float)])) <= umkreis:
            new_list.append(([i[3]], [i[4]]))
    # Die Position des Titels – bestehend aus „OL: ?, NB: ?, Umkreis: ?“ –
    # wird horizontal und vertikal ausgerichtet.
    plt.gcf().text(0.5, 0.95, f'OL: {gk_x}, NB: {gk_y}, Umkreis: {umkreis}\
 km', ha = 'center', va = 'top')
    # Hier findet die Visualisierung der Punkte statt. Die „for“-Schleife
    # durchläuft jedes Element aus „new_list“ und platziert Punkte an den
    # Koordinaten; „zorder“ legt die Punkte über die Grenze.
    for i in new_list:
        plt.scatter(i[1], i[0], zorder = 1, color = 'red')
    # Anschließend wird „geplottet“.
    plt.show()

def geodist(P1, P2):
    L1, B1 = map(radians, P1)
    L2, B2 = map(radians, P2)
    return 6378.388 * acos(sin(L1) * sin(L2) + cos(L1) * cos(L2) * cos(B2-B1))

# ------------------------- Brücke: Zustandsnote -------------------------- #

def z(list):
    # Wenn die Brücken nicht mittels Geokoordinate sondern anhand der
    # Zustandsnote ermittelt werden sollen und somit „z“ oder „Z“
    # eingegeben wurde, muss in diesem Schritt eine Zustandsnote zwischen 1
    # und 4 mit maximal einer Nachkommastelle eingeben werden. Wenn mehr als
    # eine Nachkommastelle oder ein falsches Format (z. B. ein Buchstabe)
    # eingegeben wurde, muss die Eingabe wiederholt werden.
    print('\n######################################################\
#######\
##\n# Die Zustandsnote ist eine Zahl zwischen 1 und 4 mit maximal #\
\n# einer Nachkommastelle – getrennt durch einem Punkt.         #\
\n###########################################################\
####')
    while True:
        try:
            zn = float(input('\nZustandsnote: '))
            if zn == (floor(zn * 10) / 10) and zn >= 1.0 and zn <= 4.0:
                break
            raise
        except:
            print('Falsche Eingabe! Versuchen Sie es erneut.')
    # Außerdem kann man einstellen ob die Punkte bei der Visualisierung
    # farblich nach Zustandsnotenbereichen dargestellt werden sollen oder
    # nicht (nur rot).
    while True:
        farbe = input('Farbige Ansicht einschalten? (j/n): ')
        if farbe == 'j' or farbe == 'J' or farbe == 'n' or farbe == 'N':
            break
    print('Deutschlandkarte wird konstruiert ...\n')
    # Hier werden die Bereiche der Zustandsnote samt Farbe festgelegt.
    if zn >= 1.0 and zn <= 1.4:
        bereich = ['(sehr guter Zustand)', 'green']
    elif zn >= 1.5 and zn <= 1.9:
        bereich = ['(guter Zustand)', 'lime']
    elif zn >= 2.0 and zn <= 2.4:
        bereich = ['(befriedigender Zustand)', 'yellow']
    elif zn >= 2.5 and zn <= 2.9:
        bereich = ['(ausreichender Zustand)', 'orange']
    elif zn >= 3.0 and zn <= 3.4:
        bereich = ['(nicht ausreichender Zustand)', 'pink']
    elif zn >= 3.5 and zn <= 4.0:
        bereich = ['(ungenügender Zustand)', 'red']
    # Die Liste wird durchlaufen und überprüft ob die eingegebene
    # Zustandsnote (die zu einer Liste umgewandelt wurde) mit den
    # Zustandsnoten aus der extrahierten Liste am Anfang – „list“ –
    # übereinstimmen. Wenn ja, werden die Koordinaten des Indexes „i“ der
    # neuen Liste „new_list“ hinzugefügt.
    new_list = []
    for i in list:
        if i[2] == [zn]:
            new_list.append((i[3], i[4]))
    # Die Position des Titels wird horizontal und vertikal ausgerichtet.
    plt.gcf().text(0.5, 0.95, f'Karte der {len(new_list)} deutschen\
 Fernstraßenbrücken\nmit der Zustandsnote {zn} {bereich[0]}', ha = 'center',\
    va = 'top')
    # Hier findet die Visualisierung der Punkte statt. Die „for“- Schleife
    # durchläuft jedes Element aus „new_list“ und platziert Punkte an den
    # Koordinaten; „zorder“ legt die Punkte über die Grenze. Außerdem
    # entscheidet das Programm hier, ob die Visualierung farblich ablaufen
    # soll.
    if farbe == 'j':
        for i in new_list:
            plt.scatter(i[1], i[0], zorder = 1, color = bereich[1])
    elif farbe == 'n':
        for i in new_list:
            plt.scatter(i[1], i[0], zorder = 1, color = 'red')
    # Anschließend wird „geplottet“.
    plt.show()

# -------------------------------- Straße --------------------------------- #

def s(list):
    print('Straßen werden geladen ...')
    # Wenn zu Beginn „s“ oder „S“ eingegeben wurde, wird nachfolgend nach
    # einer Straße gesucht. Es wird eine neue Liste erstellt wo Straßen,
    # die nicht beinhaltet sind, hinzugefügt werden.
    streets = []
    for i in list:
        if i[0] not in streets:
            streets.append(i[0])
        if i[1] not in streets:
            streets.append(i[1])
    print()
    print(streets)
    print('\n######################################################\
#######\
##\n# Wählen Sie Ihre Straße aus – Angabe ohne Anführungsstriche  #\
\n# oder Klammern.                                              #\
\n###########################################################\
####')
    # Die Liste wird durchlaufen und überprüft, ob die eingegebene Straße im
    # Index 0 oder 1 vorzufinden ist. Wenn ja, wird die Straße samt
    # Koordinaten der neuen Liste „new_list“ hinzugefügt.
    straße = input('\nStraße: ')
    new_list = []
    for i in list:
        if i[0] == [straße] or i[1] == [straße]:
            new_list.append(([i[3]], [i[4]]))
    # Wenn diese Liste leer ist, sprich wenn diese Straße nicht auffindbar
    # ist, erscheint eine entsprechende Meldung.
    if not new_list:
        print(f'„{straße}“ ist nicht vorhanden!\n')
    else:
    # Andererseits wird die Karte konstruiert.
        print('Deutschlandkarte wird konstruiert ...\n')
    # Die Position des Titels wird horizontal und vertikal ausgerichtet.
        plt.gcf().text(0.5, 0.95, straße, ha = 'center', va = 'top')
    # Hier findet die Visualisierung der Punkte statt. Die „for“-Schleife
    # durchläuft jedes Element aus „new_list“ und platziert Punkte an den
    # Koordinaten; „zorder“ legt die Punkte über die Grenze.
        for i in new_list:
            plt.scatter(i[1], i[0], zorder = 1, color = 'red')
    # Anschließend wird „geplottet“.    
        plt.show()

# --------------------------------- Main ---------------------------------- #

def main():
    print('\n######################################################\
#########\
\n# Dieses Programm stellt Brücken anhand der Zustandsnote oder #\
\n# des Umkreises einer Geokoordinate sowie Straßen aus         #\
\n# „Zustandsnoten.csv“ auf einer Deutschlandkarte dar.         #\
\n###########################################################\
####')
    # „Deutschlandkarte.txt“ wird eingelesen
    readMap()
    # „Zustandsnoten.csv“ wird eingelesen
    list = readCsv()
    # Brücke oder Straße?
    choice = bOrS()
    # Brücke
    if choice == 'b' or choice == 'B':
        # Brücke: Geokoordinate oder Zustandsnote?
        choice = gOrZ()
        # Brücke: Geokoordinate
        if choice == 'g' or choice == 'G':
            g(list)
        # Brücke: Zustandsnote
        elif choice == 'z' or choice == 'Z':
            z(list)
    # Straße
    elif choice == 's' or choice == 'S':
        s(list)

if __name__ == '__main__':
    main()