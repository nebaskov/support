import numpy as np
import matplotlib.pyplot as plt

# вариант 4
a = 0.001
L = 1
t_max = 10
T_0 = 0
T_l = 80
T_init = 0

# массивы времени и длины
tau = 0.3
t = np.arange(0, t_max, tau)
h = 0.1 
l = np.arange(0, L, h)

# массив температур 
T = np.zeros((t.shape[0], l.shape[0]))
T[0, :] = T_0
T[:, -1] = T_0
T[:, 0] = T_l

for k in range(1, t.shape[0]):
    for j in range(1, l.shape[0]-1):
        T[k, j] = a * tau * np.divide((T[k-1, j+1] - 2 * T[k-1, j] + T[k-1, j-1]), np.square(h)) + T[k-1, j]
    
# итоговый массив
teplo = np.ones((t.shape[0], l.shape[0]))
teplo = teplo * T[-1, :]

# вывод графика
plt.contour(teplo, linestyles='dashed', colors='k')
cs = plt.contourf(teplo, linestyles='dashed')
plt.clabel(cs, fontsize=10, colors='k')
plt.colorbar(cs)
plt.xlim(0, 5)
plt.show()