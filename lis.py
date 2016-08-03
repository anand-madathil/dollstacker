import numpy as np

def lischeck(list1):
	comparer = [0]*len(list1)
	listelements = {}
	listi = []
	listcounter = 1
	biggestinchain = 0
	for i in range(0,len(list1)):
		listi.append(i)
		for j in range(i + 1,len(list1)):
			if listcounter == 0:
				if list1[i] < list1[j]:
					biggestinchain = list1[j]
					listcounter = listcounter + 1
					listi.append(j)
			else:
				if biggestinchain < list1[j]:
					biggestinchain = list1[j]
					listcounter = listcounter + 1
					comparer[i] = listcounter
					listi.append(j)
		listelements[i] = listi
		listi = []
		listcounter = 1
					
	print max(comparer)
	print listelements[np.argmax(comparer)]

if __name__ == "__main__":
	a = [10, 22, 9, 33, 21, 50, 41, 60, 80]
	lischeck(a)
