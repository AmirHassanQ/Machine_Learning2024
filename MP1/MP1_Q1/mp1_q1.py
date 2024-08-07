# -*- coding: utf-8 -*-
"""MP1_Q1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/190Evtioz7wgvdG1NtnLVX0OK3MTH8FI_

# Q1_2

importing libraries
"""

import numpy as np
from sklearn.datasets import make_classification
import matplotlib.pyplot as plt

"""define inputs and labels"""

X1,y1 = make_classification(n_samples = 1000, n_features= 3, n_redundant=0, n_classes = 4,n_clusters_per_class=1,random_state=12, class_sep=2)

print('shape of X as input:',X1.shape)
print('shape of y as label:',y1.shape)

#plt.scatter(X[:,0],X[:,1],X[:,2],c=y)

"""plotting 3D of data"""

fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(X1[:, 0], X1[:, 1], X1[:, 2], c=y1, s=50, edgecolors='w')  # Scatter plot of the original data points
ax.set_xlabel('Feature 1')
ax.set_ylabel('Feature 2')
ax.set_zlabel('Feature 3')
ax.set_title('3D view of features')
plt.savefig('3D_class_sep2.png')

"""plotting 2D of data
each axis is for one feature
"""

plt.subplot(3,1,1)
plt.scatter(X1[:,0],X1[:,1],c=y1)
plt.xlabel('feature1')
plt.ylabel('feature2')
plt.title('2D view of feature 1 and feature2')

plt.subplot(3,1,2)
plt.scatter(X1[:,0],X1[:,2],c=y1)
plt.xlabel('feature1')
plt.ylabel('feature3')
plt.title('2D view of feature 1 and feature3')

plt.subplot(3,1,3)
plt.scatter(X1[:,1],X1[:,2],c=y1)
plt.xlabel('feature2')
plt.ylabel('feature3')
plt.title('2D view of feature 2 and feature3')

plt.subplots_adjust(wspace=0.5, hspace = 1)
plt.savefig('2D_classes_sep2.png')

"""changing class_sep"""

X2,y2 = make_classification(n_samples = 1000, n_features= 3, n_redundant=0, n_classes = 4,n_clusters_per_class=1,random_state=44, class_sep=0.5)

fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(X2[:, 0], X2[:, 1], X2[:, 2], c=y2, s=50, edgecolors='w')  # Scatter plot of the original data points
ax.set_xlabel('Feature 1')
ax.set_ylabel('Feature 2')
ax.set_zlabel('Feature 3')
ax.set_title('3D view of features')
plt.savefig('3D_class_sep0.5.png')

"""# Q1_3

importing libraries
"""

import numpy as np
from sklearn.datasets import make_classification
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression,SGDClassifier,Perceptron

x_train,x_test,y_train,y_test = train_test_split(X1,y1,test_size = 0.2)
print('shape of x_train as input:',x_train.shape)
print('shape of x_test as validation input:',x_test.shape)
print('shape of y_train as label:',y_train.shape)
print('shape of y_test as validation label:',y_test.shape)

"""Logistic Regression"""

model1 = LogisticRegression(solver = 'newton-cg' )

"""different itteration"""

train_accuracy = []
test_accuracy = []

for i in range(5):
  model1.max_iter = i
  model1.fit(x_train,y_train)
  train_accuracy.append(model1.score(x_train,y_train))
  test_accuracy.append(model1.score(x_test,y_test))

max_train_acc_index = np.argmax(train_accuracy)
max_train_acc_value = np.max(train_accuracy)
print('maximum accuracy for train data is',max_train_acc_value*100,'% for',max_train_acc_index,'index')
max_test_acc_index = np.argmax(test_accuracy)
max_test_acc_value = np.max(test_accuracy)
print('maximum accuracy for test data is',max_test_acc_value*100,'% for',max_test_acc_index,'index')

plt.figure(figsize=(10, 6))
plt.plot(train_accuracy, color = 'k', marker = '.')
plt.plot(test_accuracy, color = 'g', marker = '.')
plt.xlabel('iteration')
plt.ylabel('accuracy')
plt.savefig('Logistic_different iteration.png')

"""different solvers"""

solvers = ['lbfgs', 'liblinear', 'newton-cg', 'newton-cholesky', 'sag', 'saga']
model1.max_iter = 5
for solver in range(len(solvers)):
  model1.solver = solvers[solver]
  model1.fit(x_train,y_train)
  score_train = model1.score(x_train,y_train)
  score_test = model1.score(x_test,y_test)
  print('solver:',solvers[solver],'\n','score_train=',score_train*100,'\n','score_test=',score_test*100,'\n')

"""SGD classifier"""

model2 = SGDClassifier()

"""different itteration"""

train_accuracy2 = []
test_accuracy2 = []

for i in range(10):
  model2.max_iter = i+1
  model2.fit(x_train,y_train)
  train_accuracy2.append(model2.score(x_train,y_train))
  test_accuracy2.append(model2.score(x_test,y_test))

max_train_acc_index2 = np.argmax(train_accuracy2)
max_train_acc_value2 = np.max(train_accuracy2)
print('maximum accuracy for train data is',max_train_acc_value2*100,'% for',max_train_acc_index2,'index')
max_test_acc_index2 = np.argmax(test_accuracy2)
max_test_acc_value2 = np.max(test_accuracy2)
print('maximum accuracy for test data is',max_test_acc_value2*100,'% for',max_test_acc_index2,'index')

plt.figure(figsize=(10, 6))
plt.plot(train_accuracy2, color = 'k', marker = '.')
plt.plot(test_accuracy2, color = 'g', marker = '.')
plt.xlabel('iteration')
plt.ylabel('accuracy')
plt.savefig('SGD_differnt iteration.png')

"""different learning rate"""

model2.learning_rate = 'constant'
learning_rates = np.linspace(0.05,0.5,100)
print(learning_rates)

train_accuracy3 = []
test_accuracy3 = []

for i in range(len(learning_rates)):
  model2.eta0 = learning_rates[i]
  model2.fit(x_train,y_train)
  train_accuracy3.append(model2.score(x_train,y_train))
  test_accuracy3.append(model2.score(x_test,y_test))
  print('eta0:',learning_rates[i],'\n','score_train=',train_accuracy3[i]*100,'\n','score_test=',test_accuracy3[i]*100,'\n')

plt.figure(figsize=(10, 6))
plt.plot(learning_rates,train_accuracy3, color = 'k', marker = '.')
plt.plot(learning_rates,test_accuracy3, color = 'g', marker = '.')
plt.xlabel('learning rate')
plt.ylabel('accuracy')
plt.savefig('accuracy differnt eta0.png')
plt.legend(['train data','test data'])
plt.savefig('SGD_differnt learning rate.png')

max_train_acc_index3 = np.argmax(train_accuracy3)
max_train_acc_value3 = np.max(train_accuracy3)
print('maximum accuracy for train data is',max_train_acc_value3*100,'% for',learning_rates[max_train_acc_index3],'learning rate')
max_test_acc_index3 = np.argmax(test_accuracy3)
max_test_acc_value3 = np.max(test_accuracy3)
print('maximum accuracy for test data is',max_test_acc_value3*100,'% for',learning_rates[max_test_acc_index3],'learning rate')

"""different alpha"""

model2.learning_rate = 'optimal'

alphas = np.linspace(0.00001,1,100)

train_accuracy4 = []
test_accuracy4 = []

for i in range(len(alphas)):
  model2.alpha = alphas[i]
  model2.fit(x_train,y_train)
  train_accuracy4.append(model2.score(x_train,y_train))
  test_accuracy4.append(model2.score(x_test,y_test))
  print('alpha:',alphas[i],'\n','score_train=',train_accuracy4[i]*100,'\n','score_test=',test_accuracy4[i]*100,'\n')

plt.figure(figsize=(10, 6))
plt.plot(alphas,train_accuracy4, color = 'k', marker = '.')
plt.plot(alphas,test_accuracy4, color = 'g', marker = '.')
plt.xlabel('alpha')
plt.ylabel('accuracy')
plt.savefig('accuracy differnt alpha.png')
plt.legend(['train data','test data'])
plt.savefig('SGD_differnt alpha.png')

max_train_acc_index4 = np.argmax(train_accuracy4)
max_train_acc_value4 = np.max(train_accuracy4)
print('maximum accuracy for train data is',max_train_acc_value4*100,'% for',alphas[max_train_acc_index4],'alpha quantity')
max_test_acc_index4 = np.argmax(test_accuracy4)
max_test_acc_value4 = np.max(test_accuracy4)
print('maximum accuracy for test data is',max_test_acc_value4*100,'% for',alphas[max_test_acc_index4],'alpha quantity')

"""Perceptron classifier"""

model3 = Perceptron()

"""different itteration"""

train_accuracy5 = []
test_accuracy5 = []

for i in range(10):
  model3.max_iter = i+1
  model3.fit(x_train,y_train)
  train_accuracy5.append(model3.score(x_train,y_train))
  test_accuracy5.append(model3.score(x_test,y_test))

max_train_acc_index5 = np.argmax(train_accuracy5)
max_train_acc_value5 = np.max(train_accuracy5)
print('maximum accuracy for train data is',max_train_acc_value5*100,'% for',max_train_acc_index5,'index')
max_test_acc_index5 = np.argmax(test_accuracy5)
max_test_acc_value5 = np.max(test_accuracy5)
print('maximum accuracy for test data is',max_test_acc_value5*100,'% for',max_test_acc_index5,'index')

plt.figure(figsize=(10, 6))
plt.plot(train_accuracy5, color = 'k', marker = '.')
plt.plot(test_accuracy5, color = 'g', marker = '.')
plt.xlabel('iteration')
plt.ylabel('accuracy')
plt.legend(['train_data','test_data'])
plt.savefig('Perceptron_differnt iteration.png')

"""different learning rate"""

model3.learning_rate = 'constant'
learning_rates = np.linspace(0.05,0.5,100)
print(learning_rates)

train_accuracy6 = []
test_accuracy6 = []

for i in range(len(learning_rates)):
  model3.eta0 = learning_rates[i]
  model3.fit(x_train,y_train)
  train_accuracy6.append(model3.score(x_train,y_train))
  test_accuracy6.append(model3.score(x_test,y_test))
  print('eta0:',learning_rates[i],'\n','score_train=',train_accuracy6[i]*100,'\n','score_test=',test_accuracy6[i]*100,'\n')

plt.figure(figsize=(10, 6))
plt.plot(learning_rates,train_accuracy6, color = 'k', marker = '.')
plt.plot(learning_rates,test_accuracy6, color = 'g', marker = '.')
plt.xlabel('learning rate')
plt.ylabel('accuracy')
plt.legend(['train data','test data'])
plt.savefig('Perceptron_different eta0.png')

max_train_acc_index6 = np.argmax(train_accuracy6)
max_train_acc_value6 = np.max(train_accuracy6)
print('maximum accuracy for train data is',max_train_acc_value6*100,'% for',learning_rates[max_train_acc_index6],'learning rate')
max_test_acc_index6 = np.argmax(test_accuracy6)
max_test_acc_value6 = np.max(test_accuracy6)
print('maximum accuracy for test data is',max_test_acc_value6*100,'% for',learning_rates[max_test_acc_index6],'learning rate')

"""different alpha"""

model3.learning_rate = 'optimal'

alphas = np.linspace(0.00001,1,100)

train_accuracy7 = []
test_accuracy7 = []

for i in range(len(alphas)):
  model3.alpha = alphas[i]
  model3.fit(x_train,y_train)
  train_accuracy7.append(model3.score(x_train,y_train))
  test_accuracy7.append(model3.score(x_test,y_test))
  print('alpha:',alphas[i],'\n','score_train=',train_accuracy7[i]*100,'\n','score_test=',test_accuracy7[i]*100,'\n')

plt.figure(figsize=(10, 6))
plt.plot(alphas,train_accuracy7, color = 'k', marker = '.')
plt.plot(alphas,test_accuracy7, color = 'g', marker = '.')
plt.xlabel('alpha')
plt.ylabel('accuracy')
plt.savefig('Perceptron_different alpha.png')
plt.legend(['train data','test data'])

max_train_acc_index7 = np.argmax(train_accuracy7)
max_train_acc_value7 = np.max(train_accuracy7)
print('maximum accuracy for train data is',max_train_acc_value7*100,'% for',alphas[max_train_acc_index7],'alpha quantity')
max_test_acc_index7 = np.argmax(test_accuracy7)
max_test_acc_value7 = np.max(test_accuracy7)
print('maximum accuracy for test data is',max_test_acc_value7*100,'% for',alphas[max_test_acc_index7],'alpha quantity')

"""#Q1_4

importing libraries
"""

from mlxtend.plotting import plot_decision_regions
from sklearn.manifold import TSNE
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression,SGDClassifier,Perceptron

def plot_region(x,y,model,name='Train data'):

    def miss_class():

        hat = model.predict(x)
        miss = np.where(y != hat)
        miss = x[miss]
        return miss

    scatter_highlight_kwargs = {'s': 60, 'label': 'Missclassified', 'alpha': 0.7, 'linewidth':2}
    ax = plot_decision_regions(x,y,clf=model,zoom_factor = 1.,legend = 0,X_highlight = miss_class(),scatter_highlight_kwargs =  scatter_highlight_kwargs)
    ax.legend(loc='upper right')
    ax.set_title(f'Decision region for {name}')
    ax.set_xlabel('Latent feature 1')
    ax.set_ylabel('Latent feature 2')

"""https://scikit-learn.org/stable/modules/generated/sklearn.manifold.TSNE.html#sklearn.manifold.TSNE

t-SNE is a tool to visualize high-dimensional data.
"""

t = TSNE(n_components = 2,random_state = 44)

X_embedded = t.fit_transform(X1,y1)

x_tr, x_te, y_tr, y_te = train_test_split( X_embedded, y1, test_size = 0.2)

# scaling
scaler = StandardScaler().fit(x_tr)
x_train_r_s  = scaler.transform(x_tr)
x_val_r_s  = scaler.transform(x_te)

model_1= LogisticRegression(solver = 'sag',max_iter = 5,random_state = 44)

model_2 = SGDClassifier(max_iter =5,learning_rate = 'constant',eta0 = 0.3227272727272727,alpha = 0.02021181818181818,random_state = 44)

model_3 = Perceptron(max_iter = 5,eta0 =  0.07727272727272727,alpha = 0.02021181818181818,random_state = 44)

models = [model_1,model_2,model_3]
model_names = ['model_1', 'model_2', 'model_3']
for i, m in enumerate(models):
    m.fit(x_train_r_s,y_train)
    plt.figure(figsize=(12,5))
    plt.subplot(1,2,1)
    plot_region(x_train_r_s,y_tr,m,'Train Data')
    plt.subplot(1,2,2)
    plot_region(x_val_r_s,y_te,m,'validation Data')
    image_name = model_names[i]+'.png'
    plt.savefig(image_name)

"""#Q1_5"""

!pip install drawdata
from drawdata import ScatterWidget

widget = ScatterWidget()
widget

widget.data

import pandas as pd
w = widget.data_as_pandas

#https://drive.google.com/file/d/1qGQVoBFBQnDqTvojv0mwZ8rLSG8_Jrde/view?usp=sharing
!gdown 1qGQVoBFBQnDqTvojv0mwZ8rLSG8_Jrde

w.to_csv('/content/drawed_data1.csv')

df = pd.read_csv('/content/drawed_data1.csv')

X1 = df[['x','y']].values
y1 = df[['label']].values
#print(X.shape)
#print(y.shape)
for i in range(len(y1)):
  if y1[i] == 'a':
    y1[i]=0
  elif y1[i] =='b':
    y1[i]=1
  elif y1[i] =='c':
    y1[i]=2
  elif y1[i] =='d':
    y1[i]=3
y_new = y1
yn = np.concatenate(y_new).astype(None)
yn

from sklearn.model_selection import train_test_split

x1_train,x1_test,y1_train,y1_test = train_test_split(X1,yn,test_size= 0.2)
print('shape of x_train as input:',x1_train.shape)
print('shape of x_test as validation input:',x1_test.shape)
print('shape of y_train as label:',y1_train.shape)
print('shape of y_test as validation label:',y1_test.shape)

from sklearn.linear_model import LogisticRegression,SGDClassifier

model_1 = LogisticRegression(solver = 'newton-cg' )

train_accuracy_1 = []
test_accuracy_1 = []

for i in range(5):
  model_1.max_iter = i
  model_1.fit(x1_train,y1_train)
  train_accuracy_1.append(model_1.score(x1_train,y1_train))
  test_accuracy_1.append(model_1.score(x1_test,y1_test))

max_train_acc_index_1 = np.argmax(train_accuracy_1)
max_train_acc_value_1 = np.max(train_accuracy_1)
print('maximum accuracy for train data is',max_train_acc_value_1*100,'% for',max_train_acc_index_1,'index')
max_test_acc_index_1 = np.argmax(test_accuracy_1)
max_test_acc_value_1 = np.max(test_accuracy_1)
print('maximum accuracy for test data is',max_test_acc_value_1*100,'% for',max_test_acc_index_1,'index')

plt.figure(figsize=(10, 6))
plt.plot(train_accuracy_1, color = 'k', marker = '.')
plt.plot(test_accuracy_1, color = 'g', marker = '.')
plt.xlabel('iteration')
plt.ylabel('accuracy')
plt.savefig('dLogistic_different iteration.png')

solvers = ['lbfgs', 'liblinear', 'newton-cg', 'newton-cholesky', 'sag', 'saga']
model_1.max_iter = 5
for solver in range(len(solvers)):
  model_1.solver = solvers[solver]
  model_1.fit(x1_train,y1_train)
  score_train_1 = model_1.score(x1_train,y1_train)
  score_test_1 = model_1.score(x1_test,y1_test)
  print('solver:',solvers[solver],'\n','score_train=',score_train_1*100,'\n','score_test=',score_test_1*100,'\n')

"""SGD classifier"""

model_2 = SGDClassifier()

train_accuracy_2 = []
test_accuracy_2 = []

for i in range(5):
  model_2.max_iter = i+1
  model_2.fit(x1_train,y1_train)
  train_accuracy_2.append(model_2.score(x1_train,y1_train))
  test_accuracy_2.append(model_2.score(x1_test,y1_test))

max_train_acc_index_2 = np.argmax(train_accuracy_2)
max_train_acc_value_2 = np.max(train_accuracy_2)
print('maximum accuracy for train data is',max_train_acc_value_2*100,'% for',max_train_acc_index_2,'index')
max_test_acc_index_2 = np.argmax(test_accuracy_2)
max_test_acc_value_2 = np.max(test_accuracy_2)
print('maximum accuracy for test data is',max_test_acc_value_2*100,'% for',max_test_acc_index_2,'index')

plt.figure(figsize=(10, 6))
plt.plot(train_accuracy_2, color = 'k', marker = '.')
plt.plot(test_accuracy_2, color = 'g', marker = '.')
plt.xlabel('iteration')
plt.ylabel('accuracy')
plt.savefig('d SGD iteration.png')

model_2.learning_rate = 'constant'
learning_rates = np.linspace(0.05,0.5,100)
print(learning_rates)

train_accuracy_3 = []
test_accuracy_3 = []

for i in range(len(learning_rates)):
  model_2.eta0 = learning_rates[i]
  model_2.fit(x1_train,y1_train)
  train_accuracy_3.append(model_2.score(x1_train,y1_train))
  test_accuracy_3.append(model_2.score(x1_test,y1_test))
  print('eta0:',learning_rates[i],'\n','score_train=',train_accuracy_3[i]*100,'\n','score_test=',test_accuracy_3[i]*100,'\n')

plt.figure(figsize=(10, 6))
plt.plot(learning_rates,train_accuracy_3, color = 'k', marker = '.')
plt.plot(learning_rates,test_accuracy_3, color = 'g', marker = '.')
plt.xlabel('learning rate')
plt.ylabel('accuracy')
plt.savefig('accuracy different eta0.png')
plt.legend(['train data','test data'])
plt.savefig('d SGD_differnt learning rate.png')

max_train_acc_index_3 = np.argmax(train_accuracy_3)
max_train_acc_value_3 = np.max(train_accuracy_3)
print('maximum accuracy for train data is',max_train_acc_value_3*100,'% for',learning_rates[max_train_acc_index_3],'learning rate')
max_test_acc_index_3 = np.argmax(test_accuracy_3)
max_test_acc_value_3 = np.max(test_accuracy_3)
print('maximum accuracy for test data is',max_test_acc_value_3*100,'% for',learning_rates[max_test_acc_index_3],'learning rate')

model_2.learning_rate = 'optimal'

alphas = np.linspace(0.00001,1,100)

train_accuracy_4 = []
test_accuracy_4 = []

for i in range(len(alphas)):
  model_2.alpha = alphas[i]
  model_2.fit(x1_train,y1_train)
  train_accuracy_4.append(model_2.score(x1_train,y1_train))
  test_accuracy_4.append(model_2.score(x1_test,y1_test))
  print('alpha:',alphas[i],'\n','score_train=',train_accuracy_4[i]*100,'\n','score_test=',test_accuracy_4[i]*100,'\n')

plt.figure(figsize=(10, 6))
plt.plot(alphas,train_accuracy_4, color = 'k', marker = '.')
plt.plot(alphas,test_accuracy_4, color = 'g', marker = '.')
plt.xlabel('alpha')
plt.ylabel('accuracy')
plt.savefig('accuracy differnt alpha.png')
plt.legend(['train data','test data'])
plt.savefig('dSGD_differnt alpha.png')

max_train_acc_index_4 = np.argmax(train_accuracy_4)
max_train_acc_value_4 = np.max(train_accuracy_4)
print('maximum accuracy for train data is',max_train_acc_value_4*100,'% for',alphas[max_train_acc_index_4],'alpha quantity')
max_test_acc_index_4 = np.argmax(test_accuracy_4)
max_test_acc_value_4 = np.max(test_accuracy_4)
print('maximum accuracy for test data is',max_test_acc_value_4*100,'% for',alphas[max_test_acc_index_4],'alpha quantity')

from mlxtend.plotting import plot_decision_regions
from sklearn.manifold import TSNE
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

def plot_region(x,y,model,name='Train data'):

    def miss_class():

        hat = model.predict(x)
        miss = np.where(y != hat)
        miss = x[miss]
        return miss

    scatter_highlight_kwargs = {'s': 60, 'label': 'Missclassified', 'alpha': 0.7, 'linewidth':2}
    ax = plot_decision_regions(x,y,clf=model,zoom_factor = 1.,legend = 0,X_highlight = miss_class(),scatter_highlight_kwargs =  scatter_highlight_kwargs)
    ax.legend(loc='upper right')
    ax.set_title(f'Decision region for {name}')
    ax.set_xlabel('Latent feature 1')
    ax.set_ylabel('Latent feature 2')

t1 = TSNE(n_components = 2,random_state = 44)

X1_embedded = t1.fit_transform(X1,yn)

x_tr, x_te, y_tr, y_te = train_test_split( X1_embedded, yn, test_size = 0.2)

# scaling
scaler = StandardScaler().fit(x_tr)
x_train_r_s  = scaler.transform(x_tr)
x_val_r_s  = scaler.transform(x_te)

y_tr

model_1= LogisticRegression(solver = 'sag',max_iter = 8,random_state = 44)

model_2 = SGDClassifier(max_iter =3,learning_rate = 'constant',eta0 = 0.109,alpha = 0.767679,random_state = 44)

models = [model_1,model_2]
model_names_drawed = ['model_1', 'model_2']
for i, m in enumerate(models):
    m.fit(x_train_r_s,y_tr.astype(int))
    plt.figure(figsize=(12,5))
    plt.subplot(1,2,1)
    plot_region(x_train_r_s,y_tr.astype(int),m,'Train Data')
    plt.subplot(1,2,2)
    plot_region(x_val_r_s,y_te.astype(int),m,'validation Data')
    image_name = model_names_drawed[i]+'.png'
    plt.savefig(image_name)