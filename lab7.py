import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn import datasets
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix

from sklearn.cluster import KMeans

iris = datasets.load_iris()

x = pd.DataFrame(iris.data)
x.columns = ['Sepal_length','Sepal_width','Petal_length','Petal_width']

y = pd.DataFrame(iris.target)
y.columns = ['Target']



model = KMeans(n_clusters=3)
model.fit(x)

plt.Figure(figsize=(14,7))
plt.subplot(1,2,1)
colormap = np.array(['red','lime','black'])
plt.scatter(x.Petal_length, x.Petal_width, c=colormap[y.Target])

plt.subplot(1,2,2)
colormap = np.array(['red','lime','black'])
plt.scatter(x.Petal_length, x.Petal_width, c=colormap[model.labels_])
print(accuracy_score(y.Target, model.labels_))
print(confusion_matrix(y.Target,model.labels_))