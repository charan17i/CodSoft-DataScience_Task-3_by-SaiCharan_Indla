# -*- coding: utf-8 -*-
"""Task-03_CodSoft_IRIS_Flower_Classification.ipynb.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1n40r-sFEOwDyCfwISbHo896CTVp42FXW

**Task-3**: IRIS FLOWER CLASSIFICATION

**Author**: Sai Charan Indla

**Batch**: November - December

**Domain**: Data Science

**Aim**: To develop a model that can classify iris
'''
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.metrics import classification_report

df=pd.read_csv('/content/SaiCharanIndlaIRIS.csv')
df.head(5)

df.info()

"""'''***Data Visualization***'''"""

plt.figure(figsize=(5,3))
df["species"].value_counts().plot(kind='pie',autopct='%.2f',labels=None)
plt.legend(df["species"].value_counts().index, title="species", loc="center left", bbox_to_anchor=(1, 0.5))
plt.title("Distribution of Species")

l=['sepal_length','sepal_width','petal_length','petal_width']
plt.figure(figsize=(6,5))
for i in l:
    plt.subplot(2, 2, l.index(i) + 1)   # 2 rows , 2 columns
    sns.boxplot(df[i])
    plt.title(f"Boxplot of {i}")
plt.tight_layout()

sns.FacetGrid(df, hue ="species", height=4, aspect=1).map(plt.scatter, 'petal_length','petal_width').add_legend()

sns.FacetGrid(df, hue ="species", height=4, aspect=1).map(plt.scatter, 'sepal_length','sepal_width').add_legend()

sns.pairplot(df,hue='species')

df.isnull().sum()

"""'''**Encoding**'''"""

df["species"].value_counts()

df["species"]=df["species"].replace({"Iris-setosa":0,"Iris-versicolor":1,"Iris-virginica":2})

"""'''Checking Correlation'''"""

df.corr()

plt.figure(figsize=(5, 2))
cor=df.corr()
sns.heatmap(cor,annot=True)

"""'''**Splitting variables**'''"""

x=df.iloc[:,:4]
y=df.iloc[:,-1]
x.info()
y.info()

"""'''Train_split'''

"""

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=32)

print(x_train.shape)
print(x_test.shape)

"""'''Knn'''"""

model1=KNeighborsClassifier(n_neighbors=3)
model1

model1.fit(x_train, y_train)
y_pred1 = model1.predict(x_test)
print(classification_report(y_test, y_pred1))
print(confusion_matrix(y_test,y_pred1))

"""'''LOgistic'''"""

model2=LogisticRegression(max_iter=1000) # Increase the max_iter value
model2

model2.fit(x_train, y_train)
y_pred2 = model2.predict(x_test)
print(classification_report(y_test, y_pred2))
print(confusion_matrix(y_test,y_pred2))

"""'''Decision'''

"""

model3=DecisionTreeClassifier() # Increase the max_iter value
model3

model3.fit(x_train, y_train)
y_pred3 = model3.predict(x_test)
print(classification_report(y_test, y_pred3))
print(confusion_matrix(y_test,y_pred3))

"""'''Printing'''"""

print("KNN Classifier Accuracy:", accuracy_score(y_test, y_pred1)*100)
print("Logistic Regression Accuracy:", accuracy_score(y_test, y_pred2)*100)
print("Decision Tree Accuracy:", accuracy_score(y_test, y_pred3)*100)

"""'''Predicting'''"""

sample_check=[[5.8,2.7,3.9,1.2],
              [7.7,2.8,6.7,2],
              [7.9,3.8,6.4,2],
              [5,3.4,1.5,0.2],
              [4.8,3.4,1.9,0.2]
             ]
for i in sample_check:
    x=model3.predict([i])
    if(x==0):
        print("Iris-setosa")
    elif(x==1):
        print("Iris-versicolor")
    elif(x==2):
        print("Iris-virginica")