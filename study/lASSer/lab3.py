import numpy as np
import pandas as pd
import scipy
import matplotlib.pyplot as plt


def func(x, a, c):
    return a * np.exp(x) + c


data = pd.read_csv('C:\\Users\\nshir\\code\\study\\lASSer\\lab3.txt')

p = np.polyfit(data['R'], data['P'], deg=2)
coeff = np.poly1d(p)

log, cov = scipy.optimize.curve_fit(lambda t, a, b: a + b * np.log(t), data['R'], data['P'])
# log_approx = lambda t, a, b: a + b*np.log(t)
plt.plot(data['R'], data['P'], ls='--', marker='o')
plt.title('График зависимости мощности потерь в оптоволокне от радиуса изгиба')
plt.grid()
# plt.plot(data['R'], coeff(data['R']), ls=':')
plt.xlabel('Радиус изгиба, см')
plt.ylabel('Мощность на измерителе, мВт')
plt.show()