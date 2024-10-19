from sklearn import datasets
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree
import matplotlib.pyplot as plt
iris=datasets.load_iris()
data=iris.data
labels=iris.target

clf=DecisionTreeClassifier(criterion='entropy')
clf.fit(data,labels)
plt.figure(figsize=(12,8))
tree.plot_tree(clf,class_names=iris.target_names)
plt.title("Decision Tree")
plt.show()
