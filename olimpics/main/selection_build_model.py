import re
import pandas as pd
import numpy as np
import seaborn as sns
from rdkit.Chem.Descriptors import ExactMolWt
from rdkit import Chem

ds = pd.read_csv('DB_chromophore.csv', index_col='Tag')
print(ds.describe())

ds = ds.drop_duplicates()
print('NaN in raw ds: \n', ds.isna().sum())
ds = ds.replace(' ', np.nan)

print('NaN after replacing: \n', ds.isna().sum())
search = re.compile('\d+\.\d+')

fuck = ds['Quantum yield'].apply(lambda x: search.findall(x))
for idx in ds.index:
  ds.loc[idx, 'Quantum yield'] = fuck.loc[idx][0]

print('quant yield after re: \n', ds['Quantum yield'])

ds['Quantum yield'] = ds['Quantum yield'].astype('float')
print('quant yield after astype: \n', ds['Quantum yield'])

ds['Chromophore'] = ds['Chromophore'].apply(lambda x: x.upper())
print(ds['Chromophore'])

missing_weight = ds[ds['Molecular weight (g mol-1)'].isna()]
ds.drop(missing_weight.index, inplace=True)

print('NaN after all: \n', ds.isna().sum())

ds.to_csv('chrom.csv')