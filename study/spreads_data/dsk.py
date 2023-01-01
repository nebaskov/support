import pandas as pd
import matplotlib.pyplot as plt

datac1 = pd.read_csv('C:\\Users\\nshir\\code\\study\\spreads_data\\dsk\\cooling_spr1.txt', sep=';')
datac2 = pd.read_csv('C:\\Users\\nshir\\code\\study\\spreads_data\\dsk\\cooling_spr2.txt', sep=';')
datac3 = pd.read_csv('C:\\Users\\nshir\\code\\study\\spreads_data\\dsk\\cooling_spr3.txt', sep=';')
datah1 = pd.read_csv('C:\\Users\\nshir\\code\\study\\spreads_data\\dsk\\heating_spr1.txt', sep=';')
datah2 = pd.read_csv('C:\\Users\\nshir\\code\\study\\spreads_data\\dsk\\heating_spr2.txt', sep=';')
datah3 = pd.read_csv('C:\\Users\\nshir\\code\\study\\spreads_data\\dsk\\heating_spr3.txt', sep=';')

datac1['DSC/(mW/mg)'] = [float(str(item).strip()) for item in datac1['DSC/(mW/mg)'].tolist()]
datac2['DSC/(mW/mg)'] = [float(str(item).strip()) for item in datac2['DSC/(mW/mg)'].tolist()]
datac3['DSC/(mW/mg)'] = [float(str(item).strip()) for item in datac3['DSC/(mW/mg)'].tolist()]

datah1['DSC/(mW/mg)'] = [float(str(item).strip()) for item in datah1['DSC/(mW/mg)'].tolist()]
datah2['DSC/(mW/mg)'] = [float(str(item).strip()) for item in datah2['DSC/(mW/mg)'].tolist()]
datah3['DSC/(mW/mg)'] = [float(str(item).strip()) for item in datah3['DSC/(mW/mg)'].tolist()]

c_fig = plt.figure(dpi=180)
plt.plot(datac1['Temp./°C'], datac1['DSC/(mW/mg)'], 'darkblue', linewidth=0.8, label='Спред 1')
plt.plot(datac2['Temp./°C'], datac2['DSC/(mW/mg)'], 'magenta', linewidth=0.8, label='Спред 2')
plt.plot(datac3['Temp./°C'], datac3['DSC/(mW/mg)'], 'lime', linewidth=0.8, label='Маргарин')
plt.title('ДСК анализ образцов (кривая охлаждения)')
plt.xlabel(r'Температура, $\degree C$')
plt.ylabel('ДСК, mW/mg')
plt.legend(loc='upper right')
plt.grid()
plt.show()

h_fig = plt.figure(dpi=180)
plt.plot(datah1['Temp./°C'], datah1['DSC/(mW/mg)'], 'darkblue', linewidth=0.8, label='Спред 1')
plt.plot(datah2['Temp./°C'], datah2['DSC/(mW/mg)'], 'magenta', linewidth=0.8, label='Спред 2')
plt.plot(datah3['Temp./°C'], datah3['DSC/(mW/mg)'], 'lime', linewidth=0.8, label='Маргарин')
plt.title('ДСК анализ образцов (кривая нагревания)')
plt.xlabel(r'Температура, $\degree C$')
plt.ylabel('ДСК, mW/mg')
plt.legend(loc='upper right')
plt.xlim((-30, 75))
plt.ylim((-0.5, 4))
plt.grid()
plt.show()