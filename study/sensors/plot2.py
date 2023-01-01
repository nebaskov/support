import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data0 = pd.read_csv('sensors\data\zero.txt', sep=' ')
x_ticks = np.arange(data0['wavelength'].min(), data0['wavelength'].max(), step=100)
y_ticks = np.arange(0, 105, step=25)

fig0 = plt.figure()
plt.plot(data0['wavelength'], data0['intensity'])
plt.title('Нулевое измерение (вода)')
plt.xticks(x_ticks) 
plt.savefig('sensors/images/water.png')
# plt.show()

data1 = pd.read_csv('sensors\\data\\1__5.txt', sep=' ')
fig1 = plt.figure()
plt.plot(data1['wavelength'], data1['intensity'])
plt.title(r'Краситель концентрации $10^{-5}$')
plt.xticks(x_ticks)
plt.yticks(y_ticks)
plt.savefig('sensors/images/dye_5.png')
# plt.show()

data2 = pd.read_csv('sensors\\data\\5__5.txt', sep=' ')
fig2 = plt.figure()
plt.plot(data2['wavelength'], data2['intensity'])
plt.title(r'Краситель концентрации $5 \cdot 10^{-5}$')
plt.xticks(x_ticks)
plt.yticks(y_ticks)
plt.savefig('sensors/images/dye_55.png')
# plt.show()

data3 = pd.read_csv('sensors\\data\\1__4.txt', sep=' ')
fig3 = plt.figure()
plt.plot(data3['wavelength'], data3['intensity'])
plt.title(r'Краситель концентрации $10^{-4}$')
plt.savefig('sensors/images/dye_4.png')
plt.xticks(x_ticks)
plt.yticks(y_ticks)
# plt.show()

data4 = pd.read_csv('sensors\\data\\5__4.txt', sep=' ')
fig4 = plt.figure()
plt.plot(data4['wavelength'], data4['intensity'])
plt.title(r'Краситель концентрации $5 \cdot 10^{-4}$')
plt.xticks(x_ticks)
plt.yticks(y_ticks)
plt.savefig('sensors/images/dye_45.png')
# plt.show()