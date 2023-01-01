import os
import numpy as np
import scipy as sp


def en_in_r(psf: np.array, radii):
    """
    :param psf: array of energy values
    :param radii: radii to calculate energy concentration in
    :return: energy concentration in the selected radii
    """
    full_eng = psf.sum()
    local_en = 0
    for i in range(len(x)):
        for j in range(len(y)):
            if np.square(x[i]) + np.square(y[j]) <= np.square(radii):
                local_en += psf[j][i]
            ecf = local_en / full_eng

    return ecf


# def r_for_en(x, y, psf: np.array, concentr):
#     r = 0
#     ecf = 0
#     local_en = 0
#     full_eng = psf.sum()
#     for i in range(len(x)):
#         for j in range(len(y)):
#             local_en += psf[j][i]
#             ecf = local_en / full_eng
#             if ecf <= concentr + 1e-3 or ecf >= concentr - 1e-3:
#                 break
#     return r


def half_split(rl, rm, rr, value):
    """
    :param value: the value of energy concentration
    :param rl: left bound
    :param rm: medium point
    :param rr: right bound
    :return: min radii in the selected bounds
    """
    eps = 1 - value
    while abs(en_in_r(psf_arr, rm) - 0) > eps:
        rm = (rr - rl) / 2
        if (en_in_r(psf_arr, rr) * en_in_r(psf_arr, rm)) <= 0:
            rl = rm
        else:
            rr = rm
    print('r_min = ', rm)
    print('energy_min = ', en_in_r(psf_arr, rr))

    return min(rr, rl, rm)


with open(os.path.join(os.getcwd(), 'psf_c00_00.txt'), 'r') as fl:
    lines = []
    for line in fl:
        values = [value.strip() for value in line.split()]
        lines.append(values)
    psf_arr = np.array(lines, dtype='float64')

# вариант 5
# стекло 1, стекло 2 = БФ7, ТФ7
# параметры оптимизации: r1, r2
# ограничения: |r| > 30

ecf = 0.83
r1 = 100
r2 = -100
r3 = -116.16
d1 = 7
d2 = 5
f = 70

x = np.arange(start=-6.375, stop=(6.375 + 0.05), step=0.05, dtype='float64')
y = np.arange(start=-6.375, stop=(6.375 + 0.05), step=0.05, dtype='float64')
# r = np.arange(start=0, stop=6.380, step=0.05, dtype='float64')
min_r = half_split(r1, r2, r3, ecf)
print(min_r)
