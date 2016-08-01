import numpy as np
dollno = {}
lengths = []

def dollArrange(height, width):
	global dollno
	checkalltaken = 1
	smallcount = [0]*len(height)
	for i in range(len(height)):
		if height[i] != "taken":
			for a in range(i) + range(i + 1,len(height)):
				if height[i] < height[a] and width[i] < width[a]:
					print i					
					smallcount[i] = smallcount[i] + 1
			checkalltaken = 0
		else:
			smallcount[i] = -99
			print i
	if checkalltaken == 1:
		return 0
	else:
		lengths.append(dollno[tuple(np.append(height[np.argmax(smallcount)], width[np.argmax(smallcount)]))])
		height[np.argmax(smallcount)] = "taken" 
		width[np.argmax(smallcount)] = "taken" 
		dollArrange(height, width)
def dollsArrange(height, width):
	for i in range(len(height)):
		dollno[tuple(np.append(height[i], width[i]))] = "doll number", i
	print dollArrange(height, width)			
if __name__ == "__main__":
	dollsArrange([11,34,33],[11,72,63])
	print lengths
