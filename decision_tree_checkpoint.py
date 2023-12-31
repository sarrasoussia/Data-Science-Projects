# -*- coding: utf-8 -*-
"""decision tree checkpoint.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1xXCtWz7v9_PmrQuht64buG_zbg1x0ryT
"""

#Importing our dataset from csv file
import pandas as pd
dataset=pd.read_csv("titanic-passengers.csv", sep=";")

#Preprocessing our data
def preprocess_data(new_data):
    new_data['Age'].fillna(new_data['Age'].mean(),inplace=True)
    new_data.replace({'Sex':{'male': 1,'female':0}},inplace=True)
    new_data['Cabin']=new_data.Cabin.fillna('G6')
    new_data.replace({'Survived':{'Yes': 1,'No':0}},inplace=True)
    return new_data
data=preprocess_data(dataset)

"""Decision Tree Prediction"""

#importing relevant libraries
from sklearn.model_selection import train_test_split
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

#features extraction
x=data.drop(["Survived", "Name", "Cabin", "Ticket", "Embarked"], axis=1)
y= data["Survived"]

#splitting data
x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=0.20,random_state=10)

#applying tree algorithm
trees = tree.DecisionTreeClassifier()
trees.fit(x_train, y_train)   #fitting our model
y_pred=trees.predict(x_test)   # evaluating our model
print("score:{}".format(accuracy_score(y_test, y_pred)))

import graphviz
from sklearn.tree import export_graphviz

dot_data= tree.export_graphviz(trees,out_file=None)
graph= graphviz.Source(dot_data)
graph.render("data")
graph

"""Decision Tree Pruning Code"""

dtree= tree.DecisionTreeClassifier(criterion="gini", splitter='random', max_leaf_nodes= 10, min_samples_leaf=5,
                                   max_depth=5)
dtree

"""**Decision Tree Pros**
Easy to understand and interpret. At each node, we are able to see exactly what decision our model is making.

Can handle numerical and categorical data.

Doesn't require a lot of preprocessing.

**Decision Tree Cons**
Calculations can become challenging when there are many target labels and Features.

Decision-tree learners can create over-complex trees that do not generalize the data well which means they suffer from Overfitting.

Decision trees are sensitive to overfitting and robust to outliers.
A tree is composed of Internal Nodes, branches and leaf nodes.

Random Forest Code
"""

clf=RandomForestClassifier(n_estimators=10)  #Creating a random forest with 100 decision trees
clf.fit(x_train, y_train)  #Training our model
y_pred=clf.predict(x_test)  #testing our model
print("Accuracy:", metrics.accuracy_score(y_test, y_pred))  #Measuring the accuracy of our model

clf=RandomForestClassifier(n_estimators=20)
clf.fit(x_train, y_train)
y_pred=clf.predict(x_test)
print("Accuracy:", metrics.accuracy_score(y_test, y_pred))

from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score

iris= datasets.load_iris()

clf=RandomForestClassifier(n_estimators=100)

scores = cross_val_score(clf, iris.data, iris.target, cv=5)
print("Accuracy on each subset/fold:", scores)
print("the average accuracy is", sum(scores)/5)

"""In supervised learning we use training to fit our model then we test it using the testing set.

In supervised we have two problems:

Regression: Linear, multilinear and Polynomial Regression.
Classification: Decision Tree , Random Forest , Logistic Regression , K-NN .
To test our model's performance we can use cross-validation.
"""

