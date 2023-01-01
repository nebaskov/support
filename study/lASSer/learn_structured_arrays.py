import numpy as np

# используем логарифмическую шкалу
# чем короче длина волны, тем больше проникание
# излучение не поглотится стенкой сосуда, а пройдет дальше

p = 0.95

intima_water = 0.74 
media_water = 0.73
externa_water = 0.65
cell_water = 0.9

default_intima_h = 0.02
default_media_h = 0.05
default_externa_h = 0.03

medium_h = default_externa_h + default_media_h
full_h = medium_h + default_intima_h 

# mu_h20 = 
# mu_hem_o2 = 
# mu_hem = 

wavelength = np.array([400, 500, 600, 800, 1000, 1100, 1400, 1600, 1800, 1900, 2100, 2500, 3e3, 4e3, 5e3, 75e2, 1e4, 12e3, 15e3])
coeff = np.array([1e-3, 0.5e-3, 5e-3, 0.05, 0.7, 0.1, 10, 9, 10, 100, 50, 70, 1e4, 500, 250, 700, 1e3, 12e2, 5e3], dtype='float32')

intima_h = intima_water / coeff
media_h = media_water / coeff
externa_h = externa_water / coeff

result_arr = np.fromiter([(externa_h[i], media_h[i], intima_h[i]) for i in range(wavelength.shape[0])], dtype=[('externa', 'f4'), ('media', 'f4'), ('intima', 'f4')])

final_arr = np.array([])

for element in result_arr:
    final_arr = np.append(final_arr, max(element))

print(final_arr)

