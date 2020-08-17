from numpy import *
import matplotlib.pyplot as plt
import sys


		
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
	
def printMarkovList(markovList):
	L = len(markovList)
	filename = 'data/Markov'+str(L)+'.txt'
	with open(filename, mode='wt', encoding='utf-8') as f:
    		f.write('\n'.join(str(m) for m in markovList))
	print ('File '+filename+' was successfully generated.')

def generateMarkovTriplesRec(triple, prevList, upperBound) :	
	if triple[2] < upperBound :
		prevList.append(triple)
		generateMarkovTriplesRec(vietaTop(triple), prevList, upperBound)
		generateMarkovTriplesRec(vietaBottom(triple), prevList, upperBound)
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

def generateMarkovTriples(upperBound):
	res = []
	generateMarkovTriplesRec([1,1,1], res, upperBound)
	res = sorted(res, key=lambda x: x[2])
	return removeDuplicates(res)
	
def printMarkovTriplesList(markovTriplesList):
	L = len(markovTriplesList)
	filename = 'data/MarkovTriples'+str(L)+'.txt'
	with open(filename, mode='wt', encoding='utf-8') as f:
    		f.write('\n'.join('{'+str(m[0])+', '+str(m[1])+', '+str(m[2])+'}' for m in markovTriplesList))
	print ('File '+filename+' was successfully generated.')
    		
def checkMUC(markovTriplesList):
	L = len(markovTriplesList)
	res = True;
	i=0;
	last = [0,0,0]
	while (res and i<L):
		triple = markovTriplesList[i];
		res = (triple[2] != last[2])
		last = triple
		i += 1
	print('MUC check: '+str(res))
	return res


def Fast(upperBound):
	markovList = generateMarkov(upperBound)
	markovTriplesList = generateMarkovTriples(upperBound)
	checkMUC(markovTriplesList)
	printMarkovList(markovList)
	printMarkovTriplesList(markovTriplesList)


#sys.setrecursionlimit(3000)
#upperBound = 10**1000
upperBound = 10**400

Fast(upperBound)


