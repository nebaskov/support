import os
import pandas as pd
import matplotlib.pyplot as plt

filenames = [r'sensors\data\film1.txt', r'sensors\data\film2.txt',
             r'sensors\data\film3.txt', r'sensors\data\Rast10-1_Text.txt',
             r'sensors\data\Rast10-2.txt', r'sensors\data\Voda_Texet.txt',
             r'sensors\data\Voda_Texet.txt', r'sensors\data\mix_1.txt',
             r'sensors\data\mix_2.txt', r'sensors\data\mix_25.txt']

metals = ['медь 10-1', 'медь 10-2', 'медь 10-3']

cu_1 = pd.read_excel(os.path.join(os.getcwd(), 'sensors\data\Raschyoty.xlsx'), sheet_name=metals[0],
                     names=['wl', 'val'])
cu_2 = pd.read_excel(os.path.join(os.getcwd(), 'sensors\data\Raschyoty.xlsx'), sheet_name=metals[1],
                     names=['wl', 'val'])
cu_3 = pd.read_excel(os.path.join(os.getcwd(), 'sensors\data\Raschyoty.xlsx'), sheet_name=metals[2],
                     names=['wl', 'val'])

film1 = pd.read_csv(filenames[0], sep=' ')
film2 = pd.read_csv(filenames[1], sep=' ')
film3 = pd.read_csv(filenames[2], sep=' ')

sol1 = pd.read_csv(filenames[3], sep=' ')
sol2 = pd.read_csv(filenames[4], sep=' ')

water = pd.read_csv(filenames[5], sep=' ')

mix1 = pd.read_csv(filenames[6], sep=' ')
mix2 = pd.read_csv(filenames[7], sep=' ')
mix25 = pd.read_csv(filenames[8], sep=' ')

cu_1_fig = plt.figure()
plt.plot(cu_1['wl'], cu_2['val'])
plt.title(r'Спектры меди концентрации $10^{-1}$')
cu_1_fig.savefig('sensors/images/cu1_sol.png')
# plt.show()

cu_2_fig = plt.figure()
plt.plot(cu_2['wl'], cu_2['val'])
plt.title(r'Спектры меди концентрации $10^{-2}$')
cu_2_fig.savefig('sensors/images/cu2_sol.png')
# plt.show()

cu_3_fig = plt.figure()
plt.plot(cu_3['wl'], cu_3['val'])
plt.title(r'Спектры меди концентрации $10^{-3}$')
cu_3_fig.savefig('sensors/images/cu3_sol.png')
# plt.show()

film1_fig = plt.figure()
plt.plot(film1['wl'], film1['val'])
plt.title('Спектры пленки 1')
film1_fig.savefig('sensors/images/film1.png')
# plt.show()

film2_fig = plt.figure()
plt.plot(film2['wl'], film2['val'])
plt.title('Спектры пленки 2')
film2_fig.savefig('sensors/images/film2.png')
# plt.show()

film3_fig = plt.figure()
plt.plot(film3['wl'], film3['val'])
plt.title('Спектры пленки 3')
film3_fig.savefig('sensors/images/film3.png')
# plt.show()

sol1_fig = plt.figure()
plt.plot(sol1['wl'], sol1['val'])
plt.title(r'Спектры пленки в растворе $10^{-1}$')
sol1_fig.savefig('sensors/images/sol1.png')
# plt.show()

sol2_fig = plt.figure()
plt.plot(sol2['wl'], sol2['val'])
plt.title(r'Спектры пленки в растворе $10^{-2}$')
sol2_fig.savefig('sensors/images/sol2.png')
# plt.show()

water_fig = plt.figure()
plt.plot(water['wl'], water['val'])
plt.title(r'Спектры пленки в воде')
water_fig.savefig('sensors/images/film_water.png')
# plt.show()

mix1_fig = plt.figure()
plt.plot(mix1['wl'], mix1['val'])
plt.title(r'Спектры раствора $ЭО+CuCl_2$ $10^{-1}$')
mix1_fig.savefig('sensors/images/mix1.png')
# plt.show()

mix2_fig = plt.figure()
plt.plot(mix2['wl'], mix2['val'])
plt.title(r'Спектры раствора $ЭО+CuCl_2$ $10^{-2}$')
mix2_fig.savefig('sensors/images/mix2.png')
# plt.show()

mix25_fig = plt.figure()
plt.plot(mix25['wl'], mix2['val'])
plt.title(r'Спектры раствора $ЭО+CuCl_2$ $5 \cdot 10^{-2}$')
mix25_fig.savefig('sensors/images/mix25.png')
# plt.show()
