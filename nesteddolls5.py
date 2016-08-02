import numpy as np

def dollsort(height, width):
	problematicheight = []
	problematicwidth = []
	leftmark = 1
	rightmark = len(height) - 1
	s = 0
	if len(height) > 2:
		while rightmark > leftmark:
			for i in range(leftmark, len(height)):
				if height[i] != "problematic":
					if height[i] < height[0] and width[i] < width[0]:
						leftmark = leftmark + 1
					elif height[i] >= height[0] and width[i] >= width[0]:
						break
					else:
						problematicheight.append(height[i])
						problematicwidth.append(width[i])
						height[i] = "problematic"
						width[i] = "problematic"				

			for i in range(rightmark, 0, -1):
				if height[i] != "problematic":
					if height[i] < height[0] and width[i] < width[0]:
						break
					elif height[i] >= height[0] and width[i] >= width[0]:
						rightmark = rightmark - 1
					else:
						problematicheight.append(height[i])
						problematicwidth.append(width[i])
						height[i] = "problematic"
						width[i] = "problematic"
			if rightmark > leftmark:
				s = height[rightmark]
				s1 = width[rightmark]
				height[rightmark] = height[leftmark]
				width[rightmark] = width[leftmark]
				height[leftmark] = s	
				height[leftmark] = s1
		s = height[rightmark]
		s1 = width[rightmark]
		height[rightmark] = height[0]
		width[rightmark] = width[0]
		height[0] = s	
		height[0] = s1
		for i in range(0, len(height)):
			if height[i] == "problematic":
				height = np.delete(height, i)
				width = np.delete(width,i)
		if len(height[0:rightmark]) == 0 and len(height[rightmark + 1:len(height)]) != 0:
			return 
		elif len(height[0:rightmark]) != 0 and len(height[rightmark + 1:len(height)]) == 0:
			return 
		elif len(height[0:rightmark]) != 0 and len(height[rightmark + 1:len(height)]) != 0:	
			return 
		else:
			return 
		if problematicheight != 0:
			print dollsort(problematicheight, problematicwidth)
	elif len(height) == 1:
		return height, width
	elif len(height) == 2:
		if height[1] < height[0]:
			s = height[1]
			height[1] = height[0]
			height[0] = s
			return height, width
		else:
			return height, width

			
if __name__ == "__main__":
	#a = [1,3,4,5,9,8,6,7,2]
	h = [30,50,40]
	w = [20,40,30]
	print dollsort(h,w)
