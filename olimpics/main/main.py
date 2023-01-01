import os
import pandas as pd
import numpy as np
import shap
from sklearn.ensemble import RandomForestRegressor
from sklearn.svm import SVR
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.inspection import permutation_importance
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt


# def rmse(y_true, y_predicted):
#     return np.sqrt(mean_squared_error(y_true, y_predicted))


path = os.path.join(os.getcwd(), 'data.csv')
ds = pd.read_csv(path, index_col='index')

eval_set =pd.read_csv('eval_model.csv') 

# brief statistics
print('Dataset statistics: \n',ds.describe())
print('Correlation info: \n', ds.corr())

target = 'Viability (%)'

all_features = set(ds.columns)
categ_features = {"Cell_type", "Coat", "Line_Primary_Cell", "Animal", "Cell_morphology", "Cell_age",
                  "Cell_organ", "Test", "Test_indicator"}

for feature in categ_features:
    ds[feature] = ds[feature].astype("category").cat.codes


random_seed = 341
test_size = 0.2

X_train, X_test, y_train, y_test = train_test_split(ds.drop(target, axis=1), ds[target],
                                                    test_size=test_size, random_state=random_seed)

scaler = MinMaxScaler()
scaler.fit(X_train)
x_train = scaler.transform(X_train)
x_test = scaler.transform(X_test)
eval_set = scaler.transform(eval_set)

model = RandomForestRegressor(n_estimators=163, random_state=random_seed)
model.fit(x_train, y_train)
prediction = model.predict(x_test)
metrics = mean_squared_error(y_test, prediction)
print('RMSE value: ', np.sqrt(metrics))

pred = model.predict(eval_set)
print('validation prediction: \n', pred)

# feature importance
test_x_names = pd.DataFrame(x_test, columns=ds.drop(target, axis=1).columns)

perm_importance = permutation_importance(model, x_test, y_test, random_state=52)
importance = perm_importance['importances_mean']
feature_names = test_x_names.columns
features = np.array(feature_names)
sorted_idx = perm_importance.importances_mean.argsort()
fi_dict = {'Feature id': features[sorted_idx], 'Importance': importance[sorted_idx]}
fi_ds = pd.DataFrame(fi_dict)

print(f'feature importance for Concentration (g/L): {fi_ds.loc[fi_ds[fi_ds["Feature id"] == "Concentration (g/L)"].index, "Importance"]}')
print(f'feature importance for Coat: {fi_ds.loc[fi_ds[fi_ds["Feature id"] == "Coat"].index, "Importance"]}')
print(f'feature importance for Time (h): {fi_ds.loc[fi_ds[fi_ds["Feature id"] == "Time (h)"].index, "Importance"]}')