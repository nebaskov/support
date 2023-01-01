import os
import numpy as np
import pandas as pd

path = os.path.join(os.getcwd(), 'dataset.xlsx')
ds = pd.read_excel(path)
ds.drop('Unnamed: 0', axis=1, inplace=True)

idx = ds.index.to_numpy(dtype=np.int32)
samples = np.random.choice(idx, 1937)
fds = ds.iloc[samples]
# fds.to_csv('data.csv')

eval_set = ds.drop(samples)
evs = np.random.choice(eval_set.index.to_numpy(), 1)
print(eval_set.iloc[evs].values().to_list())