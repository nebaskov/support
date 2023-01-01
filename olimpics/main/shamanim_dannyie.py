import pandas as pd
from sklearn.preprocessing import StandardScaler

ds = pd.read_excel('dataset.xlsx')
# print(ds.columns)
new_ds = ds.sample(1545)
scaler = StandardScaler()
# new_ds.drop(['Cell_morphology', 'Cell_organ', 'Test', 'Animal'], axis=1, inplace=True)
# final = scaler.fit_transform(new_ds.drop('Viability (%)', axis=1))
# final = pd.DataFrame(final, columns=ds.drop('Viability (%)', axis=1).columns)
# fff = final.merge(new_ds['Viability (%)'], right_index=True, left_index=True)

new_ds.rename(columns={'Viability (%)': 'toxicity'}, inplace=True)
new_ds.reset_index(inplace=True)
new_ds.drop(['index', 'Unnamed: 0'], axis=1, inplace=True)

new_ds.to_csv('ds_for_model.csv')

valid = ds.drop(new_ds.index).sample(1)
# valid.drop(['Cell_morphology', 'Cell_organ', 'Test', 'Animal', 'Viability (%)'], axis=1, inplace=True)
valid.drop(['Viability (%)'], axis=1, inplace=True)
# f = scaler.transform(valid.drop('Viability (%)', axis=1))
# ff = pd.DataFrame(f, columns=ds.drop('Viability (%)', axis=1).columns)
valid.reset_index(inplace=True)
valid.drop('Unnamed: 0', axis=1, inplace=True)
valid.to_csv('evaluation_set.csv')