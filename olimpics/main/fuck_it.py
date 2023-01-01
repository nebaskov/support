import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

ds = pd.read_csv('chrom.csv', index_col='Tag')
ds['Chromophore'] = ds['Chromophore'].astype('category').cat.codes
ds['Solvent'] = ds['Solvent'].astype('category').cat.codes

# violin plots
fig2, ax_ = plt.subplots(5, 4, figsize=(12, 11))
ax = []
for i in ax_:
    ax += i.tolist()
for number, column in enumerate(ds.columns):
    sns.violinplot(data=ds, x=column, ax=ax[number])
fig2.suptitle("Violin plots for columns in db")
plt.subplots_adjust(left=0.1,
                    bottom=0.1,
                    right=0.9,
                    top=0.9,
                    wspace=0.3,
                    hspace=0.6)
plt.show()

ds.drop(ds[ds['Lifetime (ns)'] > 15].index, inplace=True)
ds.drop(ds[ds['Absorption max (nm)'] > 700].index, inplace=True)
ds.drop(ds[ds['Absorption max (nm)'] < 250].index, inplace=True)
ds.drop(ds[ds['Emission max (nm)'] > 800].index, inplace=True)
ds.drop(ds[ds['Molecular weight (g mol-1)'] > 1000].index, inplace=True)

# violin plots
fig2, ax_ = plt.subplots(5, 4, figsize=(12, 11))
ax = []
for i in ax_:
    ax += i.tolist()
for number, column in enumerate(ds.columns):
    sns.violinplot(data=ds, x=column, ax=ax[number])
fig2.suptitle("Violin plots for columns in db")
plt.subplots_adjust(left=0.1,
                    bottom=0.1,
                    right=0.9,
                    top=0.9,
                    wspace=0.3,
                    hspace=0.6)
plt.show()

ds.to_csv('clean_chrom.csv')