import numpy as np
import matplotlib.pyplot as plt

# используем логарифмическую шкалу
# чем короче длина волны, тем больше проникание
# излучение не поглотится стенкой сосуда, а пройдет дальше

p = 0.95
# содержание воды в слоях
intima_water = 0.74 
media_water = 0.73
externa_water = 0.65
cell_water = 0.9

# глубина слоев
default_intima_h = 0.02
default_media_h = 0.05
default_externa_h = 0.03
cell_h = default_externa_h + default_media_h + default_intima_h

# коэффициенты для воды
wavelength = np.array([400, 500, 600, 700, 800, 900, 1000, 1100, 1400, 1600, 1800, 1900, 2100, 2500, 3e3, 4e3, 5e3, 75e2, 1e4, 12e3, 15e3])
coeff = np.array([1e-3, 0.5e-3, 5e-3, 8e-3, 0.05, 9e-2, 0.7, 0.1, 10, 9, 10, 100, 50, 70, 1e4, 500, 250, 700, 1e3, 12e2, 5e3])
hb_waves = np.array([400, 500, 600, 700, 800, 900, 1000, 1100])
hb_spectra = np.array([6e3, 1e3, 7e2, 60, 25, 18, 7, 0.1])
hbo_spectra = np.array([6e3, 1e3, 70, 8, 25, 40, 50, 10])

# коэффициенты для слоев
intima_h = intima_water / coeff
media_h = media_water / coeff
externa_h = externa_water / coeff

# создаем structured array (https://numpy.org/doc/stable/user/basics.rec.html), 
# где каждой длине волны в соответствие ставится глубина прохождения на каждом слое
result_arr = np.fromiter([(externa_h[i], media_h[i], intima_h[i]) for i in range(wavelength.shape[0])],
                            dtype=[('externa', 'f4'), ('media', 'f4'), ('intima', 'f4')])

# итоговый массив глубин пропускания
final_arr = np.fromiter([max(element) for element in result_arr], dtype=float)

condition = np.where((final_arr < 1) & (final_arr > 1e-2))

# создаем график 
fig_full = plt.figure()
plt.plot(wavelength, final_arr,
        wavelength, [default_externa_h]* wavelength.shape[0],
        wavelength, [default_media_h + default_externa_h]* wavelength.shape[0],
        wavelength, [default_intima_h + default_media_h + default_externa_h]* wavelength.shape[0])

plt.legend(['Кривая глубины проникновения', 'externa', 'media', 'intima'], loc='upper right')
plt.title('График глубины проникновения излучения в ткани')
plt.xlabel('Длина волны, нм')
plt.ylabel('Глубина проникновения, см')
plt.xscale('log')
plt.yscale('log')
plt.grid()
plt.show()

fig_close = plt.figure()
plt.plot(wavelength[condition], final_arr[condition],
        wavelength[condition], [default_externa_h]* wavelength[condition].shape[0],
        wavelength[condition], [default_media_h + default_externa_h]* wavelength[condition].shape[0],
        wavelength[condition], [default_intima_h + default_media_h + default_externa_h]* wavelength[condition].shape[0])

plt.legend(['Кривая глубины проникновения', 'externa', 'media', 'intima'], loc='upper right')
plt.title('График глубины проникновения излучения в ткани (увеличенный масштаб)')
plt.xlabel('Длина волны, нм')   
plt.ylabel('Глубина проникновения, см')
plt.xscale('log')
plt.yscale('log')
plt.grid()
plt.show()

# длины волн, на которых слои прозрачны
wave_ext = wavelength[np.where(final_arr < default_externa_h)] 
wave_med = wavelength[np.where((final_arr < default_externa_h + default_media_h) & (final_arr > default_externa_h))] 
wave_int = wavelength[np.where((final_arr < cell_h) & (final_arr > default_externa_h + default_media_h))]

print(f'длины волн, которые поглощаются в externa: {wave_ext}')
print(f'длины волн, которые поглощаются в externa + media: {wave_med}')
print(f'длины волн, которые поглощаются externa + media + intima: {wave_int}')

# спектры поглощения крови
mu_k = cell_water * coeff[hb_spectra.shape[0]] \
    + (1 - cell_water) * (p * hbo_spectra + (1 - p) * hb_spectra)

plt.plot(hb_waves, mu_k)
plt.title('Спектры поглощения крови')
plt.xlabel('Длина волны, нм')
plt.ylabel('Коэффициент поглощения')
plt.xscale('log')
plt.yscale('log')
plt.grid()
plt.show()