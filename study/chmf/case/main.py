import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# исходные данные для варианта 6
r0 = 1376.929
e2 = -1.526

c = 1 / r0
k = np.square(e2)

# анализ данных
ds = pd.read_csv('chmf\case\data.txt')
# статистика по данным
print(ds.describe())
# расположение точек в 2-Д
sns.pairplot(ds)
# plt.show()

x = ds['X'].values
z = ds['Y'].values
y = ds['Z'].values

# расположение точек в 3-Д

fig = plt.figure(facecolor = "white")
ax = fig.gca(projection='3d')
ax.plot_trisurf(y, x, z, cmap=plt.cm.jet, linewidth=0.01)
# plt.show()

# график поверхности по формуле
R = 1376.929
e_2 = -1.526
r = np.sqrt(x**2 + y**2)
c = 1/R
k = e_2

z_formula = c*(r**2)/(1+(np.sqrt(1-(1+k)*(c**2)*(r**2))))

print('max of calculated z: ', z_formula.max())
print('mean of calculated z: ', z_formula.mean())
print('min of calculated z: ', z_formula.min())

fig = plt.figure(facecolor = "white")
ax = fig.gca(projection='3d')
ax.plot_trisurf(y, x, z_formula, cmap=plt.cm.jet, linewidth=0.01)
plt.title("поверхность по формуле")
# plt.show()

# переход в полярные координаты
# найдем fi
fi = np.zeros(shape=y.shape[0])
idx0_y = np.where(y==0)
idx0_x = np.where(x[idx0_y] >= 0)
fi[idx0_x] = np.pi / 2
idx0_x = np.where(x[idx0_y] < 0)
fi[idx0_x] = -np.pi / 2

idx1_y = np.where(y >= 0)
fi[idx1_y] = np.arctan(x[idx1_y] / y[idx1_y])
idx1_y = np.where(y < 0)
fi[idx1_y[0]] = np.pi + np.arctan(x[idx1_y] / y[idx1_y])
print(fi)

r20 = 2 * np.square(r) - 1
r40 = 6 * np.power(r, 4) - 6 * np.power(r, 2) + 1
r11 = r
r31 = 3 * np.power(r, 3) - 2 * r
r22 = np.square(r)

# C * R = Z
# C = Z * R**(-1)

R = np.array([r20, r40, r11, r31, r22])
f1 = np.ones(shape=R.shape[1])
f2 = np.ones(shape=R.shape[1])
f3 = np.cos(fi).flatten()
f4 = np.cos(fi).flatten()
f5 = np.cos(2 * fi).flatten()
F = np.array([f1, f2, f3, f4, f5])

Z = z
subc = np.matmul(z, np.linalg.pinv(F))
C = np.matmul(subc, np.transpose(np.linalg.pinv(R)))

# print(C)

# как в лабе по аппроксимации
# диагональная матрица Q
q = F
lamb = R
n = z

Q = np.diag(q)
lambda02 = 0.028

# переменная L
L = np.power(np.power(R, 2) - lambda02, -1)

# вычисление матрицы Lambda
Lamb = np.transpose(np.array([[1] * R.shape[1],
                    np.power(lamb, 2),
                     np.power(lamb, 4),
                     L,
                     np.power(L, 2),
                     np.power(L, 3)], dtype=float))

# print(Lamb) 

# вычисление коэффициентов
M = np.matmul(
                    np.matmul(
                        np.matmul(
                            np.linalg.inv(
                                np.matmul(
                                    np.matmul(
                                        np.transpose(Lamb), np.power(Q, 2)),
                                         Lamb)),
                                          np.transpose(Lamb)),
                                           np.power(Q, 2)),
                                            z.to_numpy())

print(M.shape)
print(M)