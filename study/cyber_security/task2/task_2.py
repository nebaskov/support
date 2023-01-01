import pandas as pd
import matplotlib
import numpy as np
import os
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report
from sklearn import tree

df = pd.read_csv(os.path.join(os.getcwd(), 'cyber_security\\task2\\360T.csv'))

X_train, X_test, y_train, y_test = train_test_split(df.iloc[:,:-1], df.iloc[:,-1], 
                                                    test_size=0.3, random_state=65, stratify = df.iloc[:,-1])

clf = tree.DecisionTreeClassifier(criterion='entropy', #критерий разделения
                              min_samples_leaf=31, #минимальное число объектов в листе
                              max_leaf_nodes=30, #максимальное число листьев
                              random_state=65)
clf=clf.fit(X_train, y_train)
predictions = clf.predict(X_test)
print(classification_report(y_test, predictions, digits=3))

print(clf.get_depth())
from sklearn.tree import export_graphviz
import graphviz 
dot_data = tree.export_graphviz(clf, out_file=None) 
graph = graphviz.Source(dot_data) 
columns = list(X_train.columns)
dot_data = tree.export_graphviz(clf, out_file=None,
                                feature_names=columns,
                                class_names=['0', '1'],  
                                filled=True, rounded=True,  
                                special_characters=True)  
graph = graphviz.Source(dot_data)  
graph 


test_obj0 = pd.read_csv(os.path.join(os.getcwd(), 'cyber_security\\task2\\Task_2_test_file_44.csv'))
print("1 Assigned class: ", clf.predict(test_obj0))

test_obj1 = pd.read_csv(os.path.join(os.getcwd(), 'cyber_security\\task2\\Task_2_test_file_78.csv'))
print("2 Assigned class: ", clf.predict(test_obj1))

test_obj2 = pd.read_csv(os.path.join(os.getcwd(), 'cyber_security\\task2\\Task_2_test_file_107.csv'))
print("3 Assigned class: ", clf.predict(test_obj2))

test_obj3 = pd.read_csv(os.path.join(os.getcwd(), 'cyber_security\\task2\\Task_2_test_file_166.csv'))
print("4 Assigned class: ", clf.predict(test_obj3))