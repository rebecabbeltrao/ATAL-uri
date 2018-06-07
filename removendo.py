#coding: utf-8


sequence = []

def remove(word1, word2):
	sequence.append(word1)
	aux = []
	for i in xrange(len(word2)):
		if (word2[i] not in aux):
			aux.append(word2[i])
			remove(word1 + word2[i], word2[i+1:])
			
while True:
	try:
		sequence = []
		input = raw_input()
		remove(input[0], input[1:])
		
		for i in xrange(len(sequence)):
			if(len(sequence[i]) >1):
				sequence.append(sequence[i][1:])
				
		sequence = list(set(sequence))
		sequence.sort()
		
		for j in xrange(len(sequence)):
			print sequence[j]

		print
	
	except EOFError:
		break
	
