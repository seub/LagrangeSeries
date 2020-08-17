from numpy import *
import matplotlib.pyplot as plt

		
def vietaTop(triple) :
	return [triple[0], triple[2], 3*triple[0]*triple[2]-triple[1]]
	
def vietaBottom(triple) :
	return [triple[1],triple[2],3*triple[1]*triple[2]-triple[0]]

def generateMarkovRec(triple, prevList, upperBound) :
	
	if triple[2] < upperBound :
		prevList.append(triple[2])
		generateMarkovRec(vietaTop(triple), prevList, upperBound)
		generateMarkovRec(vietaBottom(triple), prevList, upperBound)
	else:
		return triple
	
def generateMarkov(upperBound):
	res = []
	generateMarkovRec([1,1,1], res, upperBound)
	return sorted(set(res))
	
def printMarkovList(upperBound):
	markovList = generateMarkov(upperBound)
	L = len(markovList)
	print(L)
	filename = 'data/Markov'+str(L)+'.txt'
	with open(filename, mode='wt', encoding='utf-8') as f:
    		f.write('\n'.join(str(m) for m in markovList))

	
upperBound = 10**415
printMarkovList(upperBound)


