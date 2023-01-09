import math #to get square root and power of 2 for distance
import operator #as parameter in sort and sorted
import pandas as pd
import numpy as np

def euclideanDistance(instance1, instance2, length):
	distance=0
    
	for x in range(length):
		distance += math.pow((instance1[x]-instance2[x]),2)
	return math.sqrt(distance)

def getNeighbours(testInstance, trainingSet, k):
	distance = []
	length = len(testInstance)-1
	for i in range(len(trainingSet)):
		dist = euclideanDistance(testInstance, trainingSet[i], length)
		distance.append((trainingSet[i], dist))
	distance.sort(key=operator.itemgetter(1)) #sort based on first column value in distance
	neighbours = []
	for x in range(k):
		neighbours.append(distance[x][0])
	return neighbours

def getResponse(neighbours):
	classVotes = {}
	for x in range(len(neighbours)):
		response = neighbours[x][-1]
		if response in classVotes:
			classVotes[response] += 1
		else:
			classVotes[response] = 1
    
	sortedClassVotes = sorted(classVotes.items(), key=operator.itemgetter(1), reverse=True) #sort the items based on descending order
	return sortedClassVotes[0][0]

def getAccuracy(testSet, predictions):
	correct = 0
	for x in range(len(predictions)):
		if predictions[x] == testSet[x][-1]:
			correct += 1
	return (correct/float(len(predictions))*100)



trainingSet = []
testSet = []
split = 0.67
data = pd.read_csv('KNN-input.csv')
trainingSet = data.sample(frac=0.67)
testSet = pd.concat([data,trainingSet]).drop_duplicates(keep=False)

trainingSet = np.array(trainingSet)
testSet = np.array(testSet)



print("Number of training data =", len(trainingSet))
print("Number of test data =", len(testSet))

predictions = []
k = 3
for x in range(len(testSet)):
	neighbours = getNeighbours(testSet[x], trainingSet, k)
	response = getResponse(neighbours)
	predictions.append(response)
	print("Predicted =",response,"Actual =",testSet[x][-1])
print("Accuracy =", getAccuracy(testSet, predictions))



