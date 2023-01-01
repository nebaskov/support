import numpy as np
import os
import matplotlib.pyplot as plt
from math import sin
from math import pi
import pandas as pd
from scipy import integrate

x = np.arange(-6.375, 6.380, 0.05)
y = np.arange(-6.375, 6.380, 0.05)
r = np.arange(0, 6.380, 0.05)

with open(os.path.join(os.getcwd(), 'psf_c00_00.txt'), 'r') as fl:
    lines = []
    for line in fl:
        values = [value.strip() for value in line.split()]
        lines.append(values)
    psf_arr = np.array(lines, dtype='float64')

full_ener = 0
for i in range(len(x)):
    for j in range(len(y)):
        full_ener += psf_arr[i][j]


#  Функция Энергии в радиусе
def energ_rad(r):
    x = np.arange(-6.375, 6.380, 0.05)
    y = np.arange(-6.375, 6.380, 0.05)
    r_ener = 0
    for i in range(len(x)):
        for j in range(len(y)):
            if x[i] ** 2 + y[i] ** 2 <= r ** 2:
                r_ener += psf_arr[j][i]
            fki = r_ener / full_ener
            fki = abs(fki - 0.8)
    return fki


r = np.arange(0, 6.380, 0.05)
k = energ_rad(0.5)
print('energy in radii: ', k)

xr = 100
xl = 0
eps = 0.05

xm = 1
while abs(energ_rad(xm) - 0) > eps:
    xm = (xr - xl) / 2
    if (energ_rad(xr) * energ_rad(xm)) <= 0:
        xl = xm
    else:
        xr = xm
print('r_min = ', xm)
print('energy_min = ', energ_rad(xm))

print('minimum point: ', min(xr, xl, xm))

from scipy import optimize

minimum = optimize.fminbound(energ_rad, 0, 2, disp=3)
print('r_min = ', minimum)
print('energy_min = ', energ_rad(minimum))


def Lens(r1, r2, r3, d1, d2, n1, n2):
    R1 = -1 / r1 * (n1 - 1)
    R2 = -1 / r2 * (n2 - n1)
    R3 = -1 / r3 * (1 - n2)
    D1 = d1 / n1
    D2 = d2 / n2
    G = R1 * D1 * R2 * D2 * R3
    Lens = -1 / G
    return Lens


def Lens_m(x):
    f_ = 100
    r1 = 47.19
    r2 = -22.06
    # r3=100
    r3 = x[1]
    d1 = 3
    # d2=10
    d2 = x[2]
    n1 = 1.613946
    n2 = 1.548861
    Lens_m = abs(Lens(r1, r2, r3, d1, d2, n1, n2) - f_)
    return Lens_m


def Lens_lim(x):
    c = 10 - abs(x)
    ceq = []


x_2 = np.arange(2, 10
                #  ,0.08
                )
x_1 = np.arange(0, 100)
x = np.array(x)

print('x1 type: ', type(x_1))

print('x1: ', x_1)

from scipy.optimize import minimize

res = minimize(Lens_m, x, method='BFGS',
               options={'disp': True})

import scipy.optimize

xopt = scipy.optimize.fmin(func=Lens_m, x0=x)


def energ_rad(r):
    x = np.arange(-6.375, 6.380, 0.05)
    y = np.arange(-6.375, 6.380, 0.05)
    r_ener = 0
    for i in range(len(x)):
        for j in range(len(y)):
            if x[i] ** 2 + y[i] ** 2 <= r ** 2:
                r_ener += psf_arr[j][i]
            fki = r_ener / full_ener
            fki = abs(fki - 0.8)
    return fki


xr = 2
xl = 0
eps = 0.05

xm = 1
while abs(energ_rad(xm) - 0) > eps:
    xm = (xr - xl) / 2
    if (energ_rad(xr) * energ_rad(xm)) <= 0:
        xl = xm
    else:
        xr = xm
print('r_min = ', xm)
print('energy_min = ', energ_rad(xm))

min(xr, xl, xm)


def Lens(r1, r2, r3, d1, d2, n1, n2):
    R1 = -1 / r1 * (n1 - 1)
    R2 = -1 / r2 * (n2 - n1)
    R3 = -1 / r3 * (1 - n2)
    D1 = d1 / n1
    D2 = d2 / n2
    G = R1 * D1 * R2 * D2 * R3
    Lens = -1 / G
    return Lens


def Lens_m(x):
    f_ = 100
    r1 = 47.19
    r2 = -22.06
    # r3=100
    r3 = x[1]
    d1 = 3
    # d2=10
    d2 = x[2]
    n1 = 1.613946
    n2 = 1.548861
    Lens_m = abs(Lens(r1, r2, r3, d1, d2, n1, n2) - f_)
    return Lens_m
