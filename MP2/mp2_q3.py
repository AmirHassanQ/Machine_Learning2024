# -*- coding: utf-8 -*-
"""MP2_Q3.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1_nRk54q5XyWNm38e6uk0hA30d2ZMogU_
"""

from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn import tree
import numpy as np

!gdown 1tyRNdk5e64Rnta1D3Lq5G6hdMj8I7ohK

data = pd.read_csv('/content/drug_data.csv')

y_d = data[['Drug']].values
X_d = data[['Age' , 'Sex' , 'BP' , 'Cholesterol' , 'Na_to_K']].values

X_pick , X_not_pick , y_pick , y_not_pick = train_test_split(X_d ,y_d ,test_size = 0.2)

X_train , X_test , y_train , y_test = train_test_split(X_pick ,y_pick ,test_size = 0.2)

X_d,y_d

from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, jaccard_score
from sklearn.metrics import confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt

clf_dt1 = tree.DecisionTreeClassifier(max_depth=3, random_state=44)
clf_dt1.fit(X_train, y_train)
tree.plot_tree(clf_dt1);
print(clf_dt1.score(X_test, y_test))
y_pred_drug1 = clf_dt1.predict(X_test)
print(precision_score(y_test , y_pred_drug1 ,average='micro'))
print(recall_score(y_test , y_pred_drug1 ,average='micro'))
print(f1_score(y_test , y_pred_drug1 ,average='micro'))
print(jaccard_score(y_test , y_pred_drug1 ,average='micro'))
cf_matrix_tree1 = confusion_matrix(y_test, y_pred_drug1)
plt.figure(figsize=(10, 6))
sns.heatmap(cf_matrix_tree1, annot=True, fmt='d', annot_kws={"size": 12})


plt.gca().set_ylim(len(np.unique(y_test)), 0)
plt.title('Confusion Matrix')
plt.xlabel('Predicted labels')
plt.ylabel('True labels')
plt.tight_layout()

clf_dt2 = tree.DecisionTreeClassifier(max_depth=3, random_state=44,criterion='entropy')
clf_dt2.fit(X_train, y_train)
tree.plot_tree(clf_dt2);
print(clf_dt2.score(X_test, y_test))
y_pred_drug2 = clf_dt2.predict(X_test)
print(precision_score(y_test , y_pred_drug2 ,average='micro'))
print(recall_score(y_test , y_pred_drug2 ,average='micro'))
print(f1_score(y_test , y_pred_drug2 ,average='micro'))
print(jaccard_score(y_test , y_pred_drug2 ,average='micro'))
cf_matrix_tree2 = confusion_matrix(y_test, y_pred_drug2)
plt.figure(figsize=(10, 6))
sns.heatmap(cf_matrix_tree2, annot=True, fmt='d', annot_kws={"size": 12})


plt.gca().set_ylim(len(np.unique(y_test)), 0)
plt.title('Confusion Matrix')
plt.xlabel('Predicted labels')
plt.ylabel('True labels')
plt.tight_layout()

clf_dt3 = tree.DecisionTreeClassifier(max_depth=2, random_state=44)
clf_dt3.fit(X_train, y_train)
tree.plot_tree(clf_dt3);
print(clf_dt3.score(X_test, y_test))
y_pred_drug3 = clf_dt3.predict(X_test)
print(precision_score(y_test , y_pred_drug3 ,average='micro'))
print(recall_score(y_test , y_pred_drug3 ,average='micro'))
print(f1_score(y_test , y_pred_drug3 ,average='micro'))
print(jaccard_score(y_test , y_pred_drug3 ,average='micro'))
cf_matrix_tree3 = confusion_matrix(y_test, y_pred_drug3)
plt.figure(figsize=(10, 6))
sns.heatmap(cf_matrix_tree3, annot=True, fmt='d', annot_kws={"size": 12})

clf_dt4 = tree.DecisionTreeClassifier(max_depth=2, random_state=44,criterion='entropy')
clf_dt4.fit(X_train, y_train)
tree.plot_tree(clf_dt4);
print(clf_dt4.score(X_test, y_test))
y_pred_drug4 = clf_dt4.predict(X_test)
print(precision_score(y_test , y_pred_drug4 ,average='micro'))
print(recall_score(y_test , y_pred_drug4 ,average='micro'))
print(f1_score(y_test , y_pred_drug4 ,average='micro'))
print(jaccard_score(y_test , y_pred_drug4 ,average='micro'))
cf_matrix_tree4 = confusion_matrix(y_test, y_pred_drug4)
plt.figure(figsize=(10, 6))
sns.heatmap(cf_matrix_tree4, annot=True, fmt='d', annot_kws={"size": 12})


plt.gca().set_ylim(len(np.unique(y_test)), 0)
plt.title('Confusion Matrix')
plt.xlabel('Predicted labels')
plt.ylabel('True labels')
plt.tight_layout()

clf_dt5 = tree.DecisionTreeClassifier(max_depth=4, random_state=44,criterion='entropy')
clf_dt5.fit(X_train, y_train)
tree.plot_tree(clf_dt5);
print(clf_dt5.score(X_test, y_test))
y_pred_drug5 = clf_dt5.predict(X_test)
print(precision_score(y_test , y_pred_drug5,average='micro'))
print(recall_score(y_test , y_pred_drug5 ,average='micro'))
print(f1_score(y_test , y_pred_drug5 ,average='micro'))
print(jaccard_score(y_test , y_pred_drug5,average='micro'))
cf_matrix_tree5 = confusion_matrix(y_test, y_pred_drug5)
plt.figure(figsize=(10, 6))
sns.heatmap(cf_matrix_tree5, annot=True, fmt='d', annot_kws={"size": 12})


plt.gca().set_ylim(len(np.unique(y_test)), 0)
plt.title('Confusion Matrix')
plt.xlabel('Predicted labels')
plt.ylabel('True labels')
plt.tight_layout()

clf_dt6 = tree.DecisionTreeClassifier(max_depth=3, random_state=44,criterion='entropy',ccp_alpha= 0.2)
clf_dt6.fit(X_train, y_train)
tree.plot_tree(clf_dt6);
print(clf_dt6.score(X_test, y_test))
y_pred_drug6 = clf_dt6.predict(X_test)
print(precision_score(y_test , y_pred_drug6 ,average='micro'))
print(recall_score(y_test , y_pred_drug6 ,average='micro'))
print(f1_score(y_test , y_pred_drug6 ,average='micro'))
print(jaccard_score(y_test , y_pred_drug6 ,average='micro'))
cf_matrix_tree6 = confusion_matrix(y_test, y_pred_drug6)
plt.figure(figsize=(10, 6))
sns.heatmap(cf_matrix_tree6, annot=True, fmt='d', annot_kws={"size": 12})


plt.gca().set_ylim(len(np.unique(y_test)), 0)
plt.title('Confusion Matrix')
plt.xlabel('Predicted labels')
plt.ylabel('True labels')
plt.tight_layout()

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

clf_random_forest = RandomForestClassifier(max_depth=2, random_state=44)
clf_random_forest.fit(X_train , y_train)
print(clf_random_forest.score(X_test , y_test))
y_pred_drug_forest = clf_random_forest.predict(X_test)

cf_matrix_forest = confusion_matrix(y_test, y_pred_drug_forest)
plt.figure(figsize=(8, 6))
sns.heatmap(cf_matrix_forest, annot=True, fmt='d', annot_kws={"size": 12})


plt.gca().set_ylim(len(np.unique(y_test)), 0)
plt.title('Confusion Matrix')
plt.xlabel('Predicted labels')
plt.ylabel('True labels')
plt.tight_layout()