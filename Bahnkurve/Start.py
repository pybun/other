from re import A
import sys
import numpy as np
from scipy import optimize
import matplotlib.pyplot as plt

L0 = 1.5
L1 = 0.5
L2 = 1.5
L3 = 1.0

list = [L0, L1, L2, L3]
list.sort()

if(list[0] + list[3] > list[1] + list[2]):
    print('Ein vollständig drehbares Gelenkviereck liegt nicht vor; das Programm wird beendet!')
    sys.exit(0)

AX = 0
AY = 0
DX = L0
DY = 0

def Bx(phi):
    return L1 * np.cos(np.deg2rad(phi))

def By(phi):
    return L1 * np.sin(np.deg2rad(phi))

def Cx(phi, psi):
    return Bx(phi) + L2 * np.cos(np.deg2rad(psi))

def Cy(phi, psi):
    return By(phi) + L2 * np.sin(np.deg2rad(psi))

def Kopplung(psi, phi):
    return np.power(Cx(phi, psi) - DX, 2) + np.power(Cy(phi, psi) - DY, 2) - np.power(L3, 2)

px = []
py = []
bx = []
by = []
cx = []
cy = []

psi_geraten = 45

def Psi(phi, psi_geraten):
    return optimize.root(Kopplung, psi_geraten, phi, method = 'krylov').x

for phi in range(0, 361, 2):
    psi_geraten = Psi(phi, psi_geraten)
    # print(phi, psi_geraten)
    px.append(Bx(phi) + L2 * np.cos(np.deg2rad(psi_geraten + 60)))
    py.append(By(phi) + L2 * np.sin(np.deg2rad(psi_geraten + 60)))
    bx.append(Bx(phi))
    by.append(By(phi))
    cx.append(Cx(phi, psi_geraten))
    cy.append(Cy(phi, psi_geraten))

plt.plot(px, py, color = 'red')
plt.plot(bx, by, color = 'blue')
plt.plot(cx, cy, color = 'black')

x = [0, Bx(70), Cx(phi, psi_geraten), DX]
y = [0, By(70), Cy(phi, psi_geraten), DY]

# ---------- ? ---------- #
z = [px[35], Cx(180, 28)]
zz = [py[35], Cy(180, 28)]
# ---------- ? ---------- #

plt.plot(x, y, '-o')
plt.plot(z, zz)
plt.show()