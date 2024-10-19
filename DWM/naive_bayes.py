import numpy as np
import pandas as pd
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score,classification_report
iris=datasets.load_iris()
data=iris.data
labels=iris.target
X_train,X_test,y_train,y_test=train_test_split(data,labels,test_size=0.2,random_state=42)
model=GaussianNB()
model.fit(X_train,y_train)
y_preds=model.predict(X_test)
accuracy=accuracy_score(y_test,y_preds)
report=classification_report(y_test,y_preds,target_names=iris.target_names)
print(f"Accuracy:{accuracy}\n Report;{report}")