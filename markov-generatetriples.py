from numpy import *
import matplotlib.pyplot as plt

		
def vietaTop(triple) :
	return [triple[0], triple[2], 3*triple[0]*triple[2]-triple[1]]
	
def vietaBottom(triple) :
	return [triple[1],triple[2],3*triple[1]*triple[2]-triple[0]]

def generateMarkovRec(triple, prevList, upperBound) :
	
	if triple[2] < upperBound :
		prevList.append(triple)
		generateMarkovRec(vietaTop(triple), prevList, upperBound)
		generateMarkovRec(vietaBottom(triple), prevList, upperBound)
	else:
		return triple
		
def removeDuplicates(inputList):
	res = []
	last = object()
	for x in inputList :
		if x == last:
			continue
		res.append(x)
		last = x
	return res
		
def generateMarkov(upperBound):
	res = []
	generateMarkovRec([1,1,1], res, upperBound)
	res = sorted(res, key=lambda x: x[2])
	return removeDuplicates(res)
	
def printMarkovList(upperBound):
	markovList = generateMarkov(upperBound)
	L = len(markovList)
	print(L)
	filename = 'data/MarkovTriples'+str(L)+'.txt'
	with open(filename, mode='wt', encoding='utf-8') as f:
    		f.write('\n'.join(str(m) for m in markovList))
    		
def checkMUC(upperBound):
	markovList = generateMarkov(upperBound)
	L = len(markovList)
	res = True;
	i=0;
	last = [0,0,0]
	while (res and i<L):
		triple = markovList[i];
		res = (triple[2] != last[2])
		last = triple
		i += 1
	return res

	
upperBound = 10**400
print(checkMUC(upperBound))
printMarkovList(upperBound)
