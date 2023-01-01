import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# файлы с растворами красителя
color_files = ['data/1__4.txt', 'data/1__5.txt', 'data/5__4.txt', 'data/5__5.txt']

# файлы со спектрами сухих пленок
raw_film_files = ['data/film1.txt', 'data/film2.txt', 'data/film3.txt']

# файлы со спектрами пленок в смеси краситель/металл + последний файл - пленка в воде
color_metal_film_files = ['data/Rast10-1_Text.txt', 'data/Rast10-2.txt', 'data/Voda_Texet.txt']

# файлы со спектрами смеси красителя с металлом
color_metal_solution_files = ['data/mix_1.txt', 'data/mix_2.txt', 'data/mix_25.txt']

# файл со спектром воды
water_file = 'data/zero.txt'

# читаем файлы с растворами красителя
color_ds1__4 = pd.read_csv(os.path.join(os.getcwd(), color_files[0]), sep=' ')
color_ds1__5 = pd.read_csv(os.path.join(os.getcwd(), color_files[1]), sep=' ')
color_ds5__4 = pd.read_csv(os.path.join(os.getcwd(), color_files[2]), sep=' ')
color_ds5__5 = pd.read_csv(os.path.join(os.getcwd(), color_files[3]), sep=' ')

# строим графики красителей
# color_fig = plt.figure()
# plt.plot(color_ds1__4['wavelength'], color_ds1__4['intensity'], label='1')  # краситель концентрации $10^{-4}$
# plt.plot(color_ds5__4['wavelength'], color_ds5__4['intensity'], label='2')  # краситель концентрации $5 * 10^{-4}$
# plt.plot(color_ds1__5['wavelength'], color_ds1__5['intensity'], label='3')  # краситель концентрации $10^{-5}$')
# plt.plot(color_ds5__5['wavelength'], color_ds5__5['intensity'], label='4')  # краситель концентрации $5 \cdot 10^{-5}$')
# plt.xlabel('Длина волны, нм')
# plt.ylabel('А, относительные ед.')
# plt.legend(loc='upper right')
# plt.grid(True)
# plt.show()

# читаем графики сухих пленок
film_ds1 = pd.read_csv(os.path.join(os.getcwd(), raw_film_files[0]), sep=' ')
film_ds2 = pd.read_csv(os.path.join(os.getcwd(), raw_film_files[1]), sep=' ')
film_ds3 = pd.read_csv(os.path.join(os.getcwd(), raw_film_files[2]), sep=' ')

# строим графики пленок
# raw_film_fig = plt.figure()
# plt.plot(film_ds1['wl'], film_ds1['val'], label='1')  # пленка № 1
# plt.plot(film_ds2['wl'], film_ds2['val'], label='2')  # пленка № 2
# plt.plot(film_ds3['wl'], film_ds3['val'], label='3')  # пленка № 3
# plt.xlabel('Длина волны, нм')
# plt.ylabel('А, относительные ед.')
# plt.legend(loc='upper right')
# plt.grid(True)
# plt.show()

# читаем файлы пленок в смеси краситель/металл и в воде
color_metal_film_ds_1 = pd.read_csv(os.path.join(os.getcwd(), color_metal_film_files[0]), sep=' ')
color_metal_film_ds_2 = pd.read_csv(os.path.join(os.getcwd(), color_metal_film_files[1]), sep=' ')
color_metal_film_ds_water = pd.read_csv(os.path.join(os.getcwd(), color_metal_film_files[2]), sep=' ')

# строим графики пленок в красителе+металлы и в воде
# color_metal_film_fig = plt.figure()
# plt.plot(color_metal_film_ds_1['wl'], color_metal_film_ds_1['val'], label='1')  # пленка металл+краситель $10^{-1}$
# plt.plot(color_metal_film_ds_2['wl'], color_metal_film_ds_2['val'], label='2')  # пленка металл+краситель $10^{-2}$
# plt.plot(color_metal_film_ds_water['wl'], color_metal_film_ds_water['val'], label='3')  # пленка вода
# plt.xlabel('Длина волны, нм')
# plt.ylabel('А, относительные ед.')
# plt.legend(loc='upper right')
# plt.grid(True)
# plt.show()

# читаем файлы смеси растворов красителя + металла
color_metal_solution_ds1 = pd.read_csv(color_metal_solution_files[0], sep=' ')
color_metal_solution_ds2 = pd.read_csv(color_metal_solution_files[1], sep=' ')
color_metal_solution_ds25 = pd.read_csv(color_metal_solution_files[2], sep=' ')

# строим графики
# color_metal_solution_fig = plt.figure()
# plt.plot(color_metal_solution_ds1['wl'], color_metal_solution_ds1['val'], label='1')  # концентр 10^{-1}
# plt.plot(color_metal_solution_ds2['wl'], color_metal_solution_ds2['val'], label='2')  # концентр 10^{-2}
# plt.plot(color_metal_solution_ds25['wl'], color_metal_solution_ds25['val'], label='3')  # концентр 5 * 10^{-2}
# plt.xlabel('Длина волны, нм')
# plt.ylabel('А, относительные ед.')
# plt.legend(loc='upper right')
# plt.grid(True)
# plt.show()

# читаем файлы со спектрами растворов металла
metals = ['медь 10-1', 'медь 10-2', 'медь 10-3']

cu_1 = pd.read_excel(os.path.join(os.getcwd(), 'data\Raschyoty.xlsx'), sheet_name=metals[0],
                     names=['wl', 'val'])
cu_2 = pd.read_excel(os.path.join(os.getcwd(), 'data\Raschyoty.xlsx'), sheet_name=metals[1],
                     names=['wl', 'val'])
cu_3 = pd.read_excel(os.path.join(os.getcwd(), 'data\Raschyoty.xlsx'), sheet_name=metals[2],
                     names=['wl', 'val'])
#
# metal_fig = plt.figure()
# plt.plot(cu_1['wl'], cu_1['val'], label='1')  # медь 10-1
# plt.plot(cu_2['wl'], cu_2['val'], label='2')  # медь 10-2
# plt.plot(cu_3['wl'], cu_3['val'], label='3')  # медь 10-3
# plt.xlabel('Длина волны, нм')
# plt.ylabel('А, относительные ед.')
# plt.legend(loc='upper right')
# plt.grid(True)
# plt.show()

# new plots

# colorant 5e-5 + me 5e-2
fist_plt = plt.figure()
plt.plot(color_metal_solution_ds25['wl'], color_metal_solution_ds25['val'], label=1)  # mix
plt.plot(color_ds5__5['wavelength'], color_ds5__5['intensity'], label=2)  # colorant
plt.plot(cu_3['wl'], cu_3['val'], label=3)  # metal
plt.xlabel('Длина волны, нм')
plt.ylabel('А, относительные ед.')
plt.legend(loc='upper right')
plt.grid(True)
plt.show()

# colorant 1e-5 + me 1e-2
second_plt = plt.figure()
plt.plot(color_metal_solution_ds2['wl'], color_metal_solution_ds2['val'], label=1)  # mix
plt.plot(color_ds1__5['wavelength'], color_ds1__5['intensity'], label=2)  # colorant
plt.plot(cu_2['wl'], cu_2['val'], label=3)  # metal
plt.xlabel('Длина волны, нм')
plt.ylabel('А, относительные ед.')
plt.legend(loc='upper right')
plt.grid(True)
plt.show()

# colorant 1e-5 + me 1e-1
fist_plt = plt.figure()
plt.plot(color_metal_solution_ds1['wl'], color_metal_solution_ds1['val'], label=1)  # mix
plt.plot(color_ds1__5['wavelength'], color_ds1__5['intensity'], label=2)  # colorant
plt.plot(cu_1['wl'], cu_1['val'], label=3)  # metal
plt.xlabel('Длина волны, нм')
plt.ylabel('А, относительные ед.')
plt.legend(loc='upper right')
plt.grid(True)
plt.show()
