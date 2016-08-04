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
			a = [height[rightmark]] 
			b = dollsort(height[rightmark + 1:len(height)], width[rightmark + 1:len(height)])[0]
			c = [width[rightmark]] 
			d = dollsort(height[rightmark + 1:len(height)], width[rightmark + 1:len(height)])[1]
			a += b
			c += d
			return a, c
		elif len(height[0:rightmark]) != 0 and len(height[rightmark + 1:len(height)]) == 0:
			a = dollsort(height[0:rightmark], width[0:rightmark])[0]
			b = [height[rightmark]] 
			c = dollsort(height[0:rightmark], width[0:rightmark])[1]
			d = [width[rightmark]]
			a += b
			c += d
			return a, c
		elif len(height[0:rightmark]) != 0 and len(height[rightmark + 1:len(height)]) != 0:	
			a = dollsort(height[0:rightmark], width[0:rightmark])[0]
			b = [height[rightmark]]
			c = dollsort(height[rightmark + 1:len(height)], width[rightmark + 1:len(height)])[0]
			d = dollsort(height[0:rightmark], width[0:rightmark])[1]
			e = [width[rightmark]]
			f = dollsort(height[rightmark + 1:len(height)], width[rightmark + 1:len(height)])[1]
			a += b
			a += c
			d += e
			d += f
			return a, d
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
	listlongelements = {}
	listi = []
	listcounter = 1
	biggestinchainw = 0
	biggestinchainh = 0
	for i in range(0,len(width)): #[10, 20, 30],[20, 20, 30]
		listi.append(i)
		for j in range(i + 1,len(width)):
			if listcounter == 1:
				if width[i] < width[j] and height[i] < height[j]:
					biggestinchainw = width[j]
					biggestinchainh = height[j]
					listcounter = listcounter + 1
					comparer[i] = listcounter
					listi.append(j)
			else:
				if biggestinchainw < width[j] and biggestinchainh < height[j]:
					biggestinchainw = width[j]
					biggestinchainh = height[j]
					listcounter = listcounter + 1
					comparer[i] = listcounter
					listi.append(j)
		listelements[i] = listi
		listi = []
		listcounter = 1
	for i in range(0, len(width)):
		if len(listelements[i]) == comparer[np.argmax(comparer)]:
			listlongelements[i] = listelements[i]
	return listlongelements

def dollno(height, width): #works with the example case and this case. disprove this method of solving the problem, if it is wrong.
	tup = dollsort(height, width)
	inliers = lischeck(tup[0], tup[1])
	print inliers
	j = 0
	dollstackh = []
	dollstackw = []
	dshdict = {}
	dswdict = {}
	hremaindict = {}
	wremaindict = {}
	hstore = height
	wstore = width
	global nest
	for i in range(0,len(height)):
		if i in inliers:
			for i in inliers[i]:	
				dollstackh.append(tup[0][i])
				dollstackw.append(tup[1][i])
				height[i] = -21
				width[i] = -21
			dshdict[j] = dollstackh
			dswdict[j] = dollstackw
			dollstackh = []
			dollstackw = []
			hremaindict[j] = height
			wremaindict[j] = width
			height = hstore
			width = wstore
			j = j + 1
	for s in range(0,j):
		i = 0
		while i < len(hremaindict[s]):
			if hremaindict[s][i] == -21:
				del hremaindict[s][i]
				del wremaindict[s][i]
			else:
				i = i + 1
		print dshdict, dswdict
		if len(hremaindict[s]) != 0:
			dollno(hremaindict[s], wremaindict[s])

			
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
