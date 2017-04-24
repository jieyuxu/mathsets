A = [1,2,3,1,1,1,1,1,1,1,1,1,2,2,2,2,3,3,3,3,3]
B = [4,3,2,8,1]
C = [5,3,7,8,10]

def isRepeat(L):
	for x in L:
		if L.count(x) > 1:
			return True
	return False

def removeRepeats(L):
	c = True
	while c == isRepeat(L):
		for x in L:
			if L.count(x) > 1:
				L.remove(x)
	return sorted(L)

def union(L1,L2):
	return removeRepeats([x for x in L1] + [y for y in L2])

def intersection(A, B):
	return removeRepeats([x for x in A if x in B])

def setDiff(L1,L2):
	return sorted([x for x in L1 if x not in L2])

def symDiff(L1,L2):
	return setDiff(union(L1,L2), intersection(L1,L2))

def cartesianProd(L1,L2):
	print "no repeats version: " + str([[x,y] for x in L1 for y in L2])
	return removeRepeats([[x,y] for x in L1 for y in L2]) 

#LET THE HUNGER TESTS BEGIN.
print "Testing Union..."
print "================\n"
print "Unioning lists: " + str(A) + " and " + str(B)
print "Result:" + str(union(A,B)) + "\n"

print "Unioning lists: " + str(B) + " and " + str(C)
print "Result:" + str(union(C,B))
print 

print "Testing Intersection..."
print "=======================\n"
print "Intersecting lists: " + str(A) + " and " + str(B)
print "Result:" + str(intersection(A,B)) + "\n"

print "Intersecting lists: " + str(C) + " and " + str(B)
print "Result:" + str(intersection(C,B))
print 

print "Testing Set Difference..."
print "================\n"
print "Testing lists: " + str(A) + " and " + str(B)
print "Result:" + str(setDiff(A,B)) + "\n"

print "Testing lists: " + str(B) + " and " + str(C)
print "Result:" + str(setDiff(B,C))
print 

A = [1,2,3]
B = [2,3,4]

print "Testing Sym Difference..."
print "================\n"
print "Testing lists: " + str(A) + " and " + str(B)
print "Result:" + str(symDiff(A,B)) + "\n"

print "Testing lists: " + str(B) + " and " + str(C)
print "Result:" + str(symDiff(B,C))
print 

A = [1,2]
B = ["red", "white"]

C = [2,3,4,5,2,3]

print "Testing lists: " + str(A) + " and " + str(B)
print "Result:" + str(cartesianProd(A,B)) + "\n"

print "Testing lists: " + str(B) + " and " + str(C)
print "Result:" + str(cartesianProd(C,B))


