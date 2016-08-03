import numpy as np

def dollsort(height, width):
	leftmark = 1
	rightmark = len(height) - 1
	s = 0
	if len(height) > 2:
		while rightmark > leftmark:
			for i in range(leftmark, len(height)):
				if height[i] <= height[0]:
					leftmark = leftmark + 1
				else:
					break
					
			for i in range(rightmark, 0, -1):
				if height[0] <= height[i]:
					rightmark = rightmark - 1
				else:
					break
			if rightmark > leftmark:
				s = height[rightmark]
				s1 = width[rightmark]
				height[rightmark] = height[leftmark]
				width[rightmark] = width[leftmark]
				width[leftmark] = s1
				height[leftmark] = s
		s = height[rightmark]
		s1 = width[rightmark]
		height[rightmark] = height[0]
		width[rightmark] = width[0]
		width[0] = s1
		height[0] = s
		if len(height[0:rightmark]) == 0 and len(height[rightmark + 1:len(height)]) != 0:
			return [height[rightmark]] + dollsort(height[rightmark + 1:len(height)], width[rightmark + 1:len(height)])[0], [width[rightmark]] + dollsort(height[rightmark + 1:len(height)], width[rightmark + 1:len(height)])[1]
		elif len(height[0:rightmark]) != 0 and len(height[rightmark + 1:len(height)]) == 0:
			return dollsort(height[0:rightmark], width[0:rightmark])[0] + [height[rightmark]], dollsort(height[0:rightmark], width[0:rightmark])[1] + [width[rightmark]]
		elif len(height[0:rightmark]) != 0 and len(height[rightmark + 1:len(height)]) != 0:	
			return dollsort(height[0:rightmark], width[0:rightmark])[0] + [height[rightmark]] + dollsort(height[rightmark + 1:len(height)], width[rightmark + 1:len(height)])[0], dollsort(height[0:rightmark], width[0:rightmark])[1] + [width[rightmark]] + dollsort(height[rightmark + 1:len(height)], width[rightmark + 1:len(height)])[1]
		else:
			return [height[rightmark]], [width[rightmark]]
	elif len(height) == 1:
		return height, width
	elif len(height) == 2:
		if height[1] < height[0]:
			s = height[1]
			s1 = width[1]
			height[1] = height[0]
			width[1] = width[0]
			height[0] = s
			width[0] = s1
			return height, width
		else:
			return height, width

def lischeck(height, width):
	comparer = [0]*len(width)
	listelements = {}
	listi = []
	listcounter = 1
	biggestinchain = 0
	for i in range(0,len(width)):
		listi.append(i)
		for j in range(i + 1,len(width)):
			if listcounter == 0:
				if width[i] < width[j] and height[i] < height[j]:
					biggestinchain = width[j]
					listcounter = listcounter + 1
					listi.append(j)
			else:
				if biggestinchain < width[j] and height[i] < height[j]:
					biggestinchain = width[j]
					listcounter = listcounter + 1
					comparer[i] = listcounter
					listi.append(j)
		listelements[i] = listi
		listi = []
		listcounter = 1			
	return listelements[np.argmax(comparer)]

def dollno(height, width): #works with the example case and this case. disprove this method of solving the problem, if it is wrong.
	tup = dollsort(height, width)
	inliers = lischeck(tup[0], tup[1])
	dollstackh = []
	dollstackw = []
	for i in inliers:
		dollstackh.append(tup[0][i])
		dollstackw.append(tup[1][i])
		height[i] = -21
		width[i] = -21
	i = 0
	while i < len(height):
		if height[i] == -21:
			height = np.delete(height, i)
			width = np.delete(width, i)
		else:
			i = i + 1
	print dollstackh, dollstackw, height, width
	if len(height) != 0:
		dollno(height, width)

			
if __name__ == "__main__":
	#a = [1,3,4,5,9,8,6,7,2]
	#10 30 20 20 30 10
	#h = [10, 20, 30, 30, 40, 20]
	#w = [10, 20, 20, 30, 30, 10]
	#for i in range(0,10):
	#	for i in range(0,3):
	#		h.append(np.random.randint(1,100))	
	#		w.append(np.random.randint(1,100))
	#print "unsorted- ", h
	#print "unsorted- ", w	
	#print "sorted- ", dollsort(h, w)
	h = [10, 20, 20, 30, 30, 10]
	w = [10, 20, 30, 30, 40, 20]
	dollno(h, w)
	h = []
	w  = []
