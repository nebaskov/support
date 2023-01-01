import os
import numpy as np
import pandas as pd

from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import VotingRegressor
from lightgbm import LGBMRegressor
from sklearn.model_selection import train_test_split

from sklearn.metrics import mean_squared_error
from sklearn.inspection import permutation_importance
from sklearn.preprocessing import StandardScaler

path = os.path.join(os.getcwd(), 'ds_for_model.csv')
ds = pd.read_csv(path)

ds.drop('Unnamed: 0', axis=1, inplace=True)
eval_set = pd.read_csv('evaluation_set.csv', index_col='index')
eval_set.drop('Unnamed: 0', axis=1, inplace=True)

target = 'toxicity'

all_features = set(ds.columns)
# categ_features = {"Cell_type", "Coat", "Line_Primary_Cell", "Cell_age", "Test_indicator"}
categ_features = {"Cell_type", "Coat", "Line_Primary_Cell",
                  "Cell_age", "Test_indicator", "Cell_morphology",
                  "Cell_organ", "Test", "Animal"}

for feature in categ_features:
    ds[feature] = ds[feature].astype("category").cat.codes

random_seed = 563
test_size = 0.2

X_train, X_test, y_train, y_test = train_test_split(ds.drop(target, axis=1), ds[target],
                                                    test_size=test_size, random_state=random_seed)

scaler = StandardScaler()
scaler.fit(X_train)
x_train = scaler.transform(X_train)
x_test = scaler.transform(X_test)

eval = scaler.transform(eval_set)

rf = RandomForestRegressor(n_estimators=500, random_state=random_seed)
lgbt = LGBMRegressor(n_estimators=1000, learning_rate=0.1594, random_state=random_seed)

model = VotingRegressor([('random_forest', rf), ('lgbt', lgbt)])

model.fit(x_train, y_train)
prediction = model.predict(x_test)

metrics = mean_squared_error(y_test, prediction)
print('RMSE value: ', np.sqrt(metrics))

pred = model.predict(eval)
print('validation prediction: \n', pred)

# feature importance
perm_importance = permutation_importance(model, x_test, y_test, random_state=32)
importance = perm_importance['importances_mean']
feature_names = X_test.columns
features = np.array(feature_names)
sorted_idx = perm_importance.importances_mean.argsort()
fi_dict = {'Feature id': features[sorted_idx], 'Importance': importance[sorted_idx]}
fi_ds = pd.DataFrame(fi_dict)

print(
    f'feature importance for Molecular weight (g/mol): {fi_ds.loc[fi_ds[fi_ds["Feature id"] == "Molecular weight (g/mol)"].index, "Importance"]}')
print(
    f'feature importance for Electronegativity: {fi_ds.loc[fi_ds[fi_ds["Feature id"] == "Electronegativity"].index, "Importance"]}')
print(
    f'feature importance for Diameter (nm): {fi_ds.loc[fi_ds[fi_ds["Feature id"] == "Diameter (nm)"].index, "Importance"]}')
