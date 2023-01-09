from sklearn.model_selection import train_test_split
from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix

iris = datasets.load_iris()

x_train,x_test,y_train,y_test  = train_test_split(iris.data,iris.target,train_size=0.1)

model = KNeighborsClassifier()
model.fit(x_train, y_train)

y_predict = model.predict(x_test)
acc = 0;
for i in range(len(y_predict)):
    print(y_predict[i] , y_test)
    if y_predict[i] == y_test[i]:
        acc += 1
        
print("Accuracy : ",acc/len(y_predict))
print("Accuracy : ",model.score(x_test, y_test))