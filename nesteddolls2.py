#each doll has a capacity for height, width, and individual height and width as well.
#For each doll, if its height and width is less than the height capacity and width capacity of another, change the capacities of the latter doll to the measurements of the former, and delete the former doll entirely.
#Base case is when the capacities of each doll are less than the measurements of every other doll. In this case, return the length of one of the lists
#find the minimum of these lengths
import numpy as np
globalcomparer = []
def Nestedcheck(height, width, heightcap, widthcap):
	global globalcomparer
	for i in range (len(height)):
		for a in range(i) + range(i + 1, len(height)):
			#if len(height) == 3:
			#print "i =",i,"a =",a,height,width,np.delete(height, a),np.delete(width, a)
			if heightcap[i] > height[a] and widthcap[i] > width[a]: #to find if recursion can continue. I don't believe you can store dolls with height x inside another doll with heightcap x
				heightstore = height
				widthstore = width
				heightcstore = heightcap
				widthcstore = widthcap
				heightcstore[i] = height[a]
				widthcstore[i] = width[a]
				Nestedcheck(np.delete(heightstore, a), np.delete(widthstore, a), np.delete(heightcstore, a), np.delete(widthcstore, a))
				#here you would try to place it inside, and continue the check, so call the function again with the changed vars
			else:
				globalcomparer.append(len(height))

def Nestedcompare(height, width, heightcap, widthcap):
	global globalcomparer
	Nestedcheck(height, width, heightcap, widthcap)
	return min(globalcomparer)

if __name__ == "__main__":
	w = [20,40,30]
	h = [30,50,40]
	print Nestedcompare(h,w,h,w)
			
