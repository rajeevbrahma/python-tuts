from turtle import distance
import numpy as np
import matplotlib.pyplot as plt
from math import sqrt
# from sklearn import neighbors, datasets
from collections import Counter


# # import some data to play with
# iris = datasets.load_iris()
# x = iris.data[:, :2]  # we only take the first two features. We could
#                       # avoid this ugly slicing by using a two-dim dataset
# y = iris.target


# print x, y


# x = np.array([[1.4,2.1],[2,3],[5,7],[8,9]]).reshape(-1,2)
# y = np.array([0,0,0,1,1,1]).reshape(-1,1)

test_features = np.array([1.1,2.3]).reshape(-1,2)

dataset = {
			'Male':[[1.2,2.1],[2.8,3.4],[1.6,2.2],[1,2],[2,3],[1.4,2.4]],
			'Female':[[5.5,7.9],[6.3,5.2],[8.1,9.5],[5,7],[6,5],[8,9]]}
color = {"Male":"b","Female":"c"}


for group in dataset:
	for features in dataset[group]:
		plt.scatter(features[0],features[1],s=100,color=color[group])


print (test_features)
plt.scatter(test_features[0][0],test_features[0][1],s=100,color='y')


distances = []
def k_nn(data,predict,k=2):

	for group in dataset:
		for features in dataset[group]:
			euclidean_distance = np.linalg.norm(np.array(features)-np.array(predict))
			distances.append([euclidean_distance,group])


	votes = [val[1] for val in sorted(distances)[:k]] # since 1 is the group
	print (Counter(votes).most_common(1))
	print ("Test feature belongs to group",Counter(votes).most_common(1)[0][0])

k_nn(dataset,test_features,k=2)


plt.show()	