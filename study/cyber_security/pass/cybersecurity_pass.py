import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.svm import LinearSVC
from sklearn.metrics import classification_report

ds = pd.read_csv(r'cybersecurity_course\UNSW_NB15_training-set.csv', index_col='id')
print('dtypes before: \n', ds.dtypes)

ds.drop(['proto', 'service', 'state', 'attack_cat'], axis=1, inplace=True)
print('dtypes after: \n', ds.dtypes)

x = ds.drop('label', axis=1)
y = ds['label']

X = MinMaxScaler().fit_transform(x)
X = pd.DataFrame(X, columns=x.columns, index=x.index)

x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=41)

clf = LinearSVC(random_state=41, C=0.27, max_iter=1000, dual=False)
clf.fit(x_train, y_train)

print('coef_4: ', clf.coef_)
print('classification report: \n', classification_report(y_train, clf.predict(x_train)))

prediction = clf.predict(x_test)
prediction = pd.Series(prediction, index=x_test.index, name='prediction')
print('# 15711: ', prediction.loc[15711])
print('# 36702: ', prediction.loc[36702])