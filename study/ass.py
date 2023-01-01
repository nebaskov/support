import numpy as np

x = np.array([12, 9, 8, 14, 15, 11, 10, 15])
y = np.array([42, 107, 100, 60, 78, 79, 90, 54])

coef = np.polyfit(x, y, deg=1)
print(coef)