def dollsort(height):
	leftmark = 0
	rightmark = len(height) - 1
	s = 0
	if len(height) != 1:
		while rightmark > leftmark:
			for i in range(len(height) - 1):
				if height[i] > height[i + 1]:
					leftmark = leftmark + 1
					break
				else:
					leftmark = leftmark + 1
			for i in range(len(height) - 1, 1, -1):
				if height[i] < height[i - 1]:
					rightmark = rightmark - 1
					break
				else:
					rightmark = rightmark - 1
			s = height[rightmark]
			print s
			height[rightmark] = height[leftmark]
			height[leftmark] = s
		s = height[rightmark]
		height[rightmark] = height[0]
		height[0] = s
		print height
		return dollsort(height[0:rightmark]) + [height[rightmark]] + dollsort(height[rightmark + 1:len(height)])
	else:
		print height
		return height
			
if __name__ == "__main__":
	a = [1,23,45,67,6]
	print dollsort(a)
	
