import numpy as np

lis1 = []
donkey = {}

def dollsort(height, width):
	leftmark = 1
	rightmark = len(height) - 1
	s = 0
	if len(height) > 2:
		while rightmark > leftmark:
			for i in range(leftmark, len(height)):
				if height[i] < height[0] or (height[i] == height[0] and width[0] < width[i]):
					leftmark = leftmark + 1
				else:
					break
					
			for i in range(rightmark, 0, -1):
				if height[i] > height[0] or (height[i] == height[0] and width[0] > width[i]):
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
			print [height[rightmark]], [width[leftmark]]
			return [height[rightmark]], [width[rightmark]]
	elif len(height) == 1:
		return height, width
	elif len(height) == 2:
		if height[1] < height[0] or ((height[1] == height[0]) and (width[1] > width[0])):
			s = height[1]
			s1 = width[1]
			height[1] = height[0]
			width[1] = width[0]
			height[0] = s
			width[0] = s1
			return height, width
		else:
			return height, width


def lis(list1):
	global lis1
	global donkey
	donkey = {}
	lis1 = [1]*len(list1)
	for i in range(len(list1)):
		donkey[i] = [i]
		for j in range(i):
			if list1[i] > list1[j] and lis1[i] < lis1[j] + 1:
				lis1[i] = lis1[j] + 1
				donkey[i].append(j)
	for i in range(len(list1)):
		del donkey[i][0]
		donkey[i].append(i)
	max1 = 0
	maxlen = []
	for i in range(len(list1)):
		max1 = max(max1, lis1[i])
		maxlen.append(len(donkey[i]))
	return donkey[np.argmax(maxlen)]



def dollno(height, width): #works with the example case and this case. disprove this method of solving the problem, if it is wrong.
	tup = dollsort(height, width)
	inliers = lis(tup[1])
	dollstackh = []
	dollstackw = []
	for i in inliers:
		dollstackh.append(tup[0][i])
		dollstackw.append(tup[1][i])
		height[i] = -21
		width[i] = -21
	i = 0
	#print dollstackh, dollstackw, height, width
	while i < len(height):
		if height[i] == -21:
			del height[i]
			del width[i]
		else:
			i = i + 1
	print dollstackh, dollstackw
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
	#h = [10,10,10,10,20]
	#w = [10,20,30,40,50]
	dollno(h, w)
	h = []
	w  = []
