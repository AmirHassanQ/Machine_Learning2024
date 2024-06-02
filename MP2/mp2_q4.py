# -*- coding: utf-8 -*-
"""MP2_Q4.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1mkqWZbAV91rGgSarcuypuc61N3DXadv4
"""

# Commented out IPython magic to ensure Python compatibility.
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.preprocessing import StandardScaler, MinMaxScaler
import matplotlib.pyplot as plt
from sklearn.utils import shuffle
# %matplotlib inline

!gdown 1mRcvox9KKj5dovyz1zo8WG8o9rgbJ2pp

data = pd.read_csv("/content/heart.csv")
data.head(11)

data.info()

data.describe()

data.groupby('target').size()

sns.countplot(x='target', data=data)

sns.pairplot(data,hue='target')

data.hist()

from imblearn.over_sampling import SMOTE
# Assuming 'data' is your DataFrame and 'target' is your target column
X = data.drop('target', axis=1)
y = data['target']

# Apply SMOTE to oversample the minority class
smote = SMOTE(random_state=44)
X_resampled, y_resampled = smote.fit_resample(X, y)

# Now, 'X_resampled' and 'y_resampled' contain the balanced dataset

# Assuming X_resampled and y_resampled are NumPy arrays
X_resampled_df = pd.DataFrame(X_resampled, columns=X.columns)
y_resampled_df = pd.DataFrame(y_resampled, columns=['target'])

# Now you have X_resampled_df and y_resampled_df as DataFrames

# Assuming X_resampled_df and y_resampled_df are your balanced DataFrames
balanced_data = pd.concat([X_resampled_df, y_resampled_df], axis=1)

# Plot countplot
sns.countplot(data=balanced_data, x='target')
plt.title('Balanced Dataset Distribution')
plt.xlabel('Target')
plt.ylabel('Count')
plt.show()

print(balanced_data.groupby('target').size())
print(balanced_data)

corr_matrix = balanced_data.corr()

plt.figure(figsize=(12,8))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')
plt.show()

shuffled_data = shuffle(balanced_data, random_state=44)
print(shuffled_data.shape)
print(shuffled_data)

X = np.array(shuffled_data.loc[:,shuffled_data.columns!='target'])
y = np.array(shuffled_data.loc[:,shuffled_data.columns=='target'])
print(X.shape)
print(y.shape)

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=44)
print('train:',X_train.shape, y_train.shape,'\ntest: ', X_test.shape, y_test.shape)

scaler = StandardScaler()
scaler.fit(X_train)
print(X_train[:5,:5])
X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)

class NaiveBayes:
    def fit(self, X, y):
        n_samples, n_features = X.shape
        self._classes = np.unique(y)
        n_classes = len(self._classes)

        # calculate mean, var, and prior for each class
        self._mean = np.zeros((n_classes, n_features), dtype=np.float64)
        self._var = np.zeros((n_classes, n_features), dtype=np.float64)
        self._priors = np.zeros(n_classes, dtype=np.float64)

        for idx, c in enumerate(self._classes):
            X_c = X[y == c]
            self._mean[idx, :] = X_c.mean(axis=0)
            self._var[idx, :] = X_c.var(axis=0)
            self._priors[idx] = X_c.shape[0] / float(n_samples)


    def predict(self, X):
        y_pred = [self._predict(x) for x in X]
        return np.array(y_pred)

    def _predict(self, x):
        posteriors = []

        # calculate posterior probability for each class
        for idx, c in enumerate(self._classes):
            prior = np.log(self._priors[idx])
            posterior = np.sum(np.log(self._pdf(idx, x)))
            posterior = posterior + prior
            posteriors.append(posterior)

        # return class with the highest posterior
        return self._classes[np.argmax(posteriors)]

    def _pdf(self, class_idx, x):
        mean = self._mean[class_idx]
        var = self._var[class_idx]
        numerator = np.exp(-((x - mean) ** 2) / (2 * var))
        denominator = np.sqrt(2 * np.pi * var)
        return numerator / denominator

from sklearn.naive_bayes import GaussianNB
MyNB = NaiveBayes()
SKNB= GaussianNB()

MyNB.fit(X_train, y_train.ravel())
SKNB.fit(X_train,y_train.ravel())
pred = MyNB.predict(X_test)
pred2 = SKNB.predict(X_test)

print(pred)
print(pred2)

from sklearn.metrics import classification_report
print(classification_report(y_test,pred))

from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
cm = confusion_matrix(y_test,pred)
names = list(data.groupby('target').groups.keys())
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=names)
disp.plot()
plt.show()

from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, jaccard_score

print('Accuracy :',accuracy_score(y_test,pred))
print('Precision :',precision_score(y_test,pred,average='micro'))
print('Recall :',recall_score(y_test,pred,average='micro'))
print('F1 score :',f1_score(y_test,pred,average='micro'))
print('Jaccard score :',jaccard_score(y_test,pred,average='micro'))

import random
data_for_s = np.append(X_test, y_test.reshape(211 , 1) , axis = 1)
samples = random.sample(list(data_for_s) , 5)
X_sample = (np.array(samples))[: , :13]
y_sample = (np.array(samples))[: , 13]

y_pred_sample = MyNB.predict(X_sample)
print(f"our model predict is {y_pred_sample} and true label is {y_sample}")
acc = 0
for i in range(len(y_pred_sample)):
  if (y_pred_sample[i] == y_sample[i]):
    acc += 1

print(f"{(100*acc)/len(y_pred_sample)}% of predicts are true")