import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.ensemble import RandomForestRegressor
from lightgbm import LGBMRegressor 
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error, r2_score

ds = pd.read_csv('clean_chrom.csv', index_col='Tag')

# sns.heatmap(ds.corr())
# plt.show()

target = ['Absorption max (nm)', 'Emission max (nm)', 'Quantum yield']

x = ds.drop(target[2], axis=1)
y = ds[target[2]]

X_train, X_test, y_train, y_test = train_test_split(x, y, random_state=2134, test_size=0.2)

scaler = StandardScaler()
scaler.fit(X_train)
x_train = scaler.transform(X_train)
x_test = scaler.transform(X_test)

# model = RandomForestRegressor()
model = LGBMRegressor()
model.fit(x_train, y_train)
pred = model.predict(x_test)

# print('RMSE absorption: ', np.sqrt(mean_squared_error(y_test, pred)))
# print('RMSE emission: ', np.sqrt(mean_squared_error(y_test, pred)))
print('RMSE Quantum yield: ', np.sqrt(mean_squared_error(y_test, pred)))
print('R2-score Quantum yield: ', r2_score(y_test, pred))