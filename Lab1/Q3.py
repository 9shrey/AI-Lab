import numpy as np

import numpy as np
def list(list1,list2):
	dist =[]
	for i in range(len(list1)):
		dist.append((list1[i]-list2[i]) **2)
	vec = np.array(dist)
	return np.sum(vec)

def calc_dist(list1, list2):
	dist = []
	for i in range(len(list1)):
		dist.append(np.sqrt(list(list1[i],list2[i])))
	return dist

def bub_sort(dist):
	n = len(dist)
	for i in range(n):
		for j in range(0, n-i-1):
			if dist[j] > dist[j+1]:
				dist[j], dist[j+1] = dist[j+1], dist[j]
	return dist

def main():
	list1 = [[1,2],[2,3]]
	list2 = [[2,4],[9,4]]

	l3 = calc_dist(list1,list2)
	l4 = bub_sort(l3)
	for i in range(len(l4)):
		print(l4[i])

if __name__ == "__main__":
	main()