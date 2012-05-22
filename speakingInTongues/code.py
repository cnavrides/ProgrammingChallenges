#!/usr/bin/env python

#the given values, plus the assumption for the one not given
mapping = {'y':'a', 'e':'o', 'q':'z', ' ':' ', 'z':'q'}

encodedStrings = [ "ejp mysljylc kd kxveddknmc re jsicpdrysi",
		   "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
		   "de kr kd eoya kw aej tysr re ujdr lkgc jv"]
decodedStrings = [ "our language is impossible to understand",
		   "there are twenty six factorial possibilities",
		   "so it is okay if you want to just give up"]

#fill in the mapping
for x in range(len(encodedStrings)):
	#get each line
	a = encodedStrings[x]
	b = decodedStrings[x]
	#go through each character
	for l in range(len(a)):
		eLetter = a[l]
		
		#if the encoded letter hasn't been found yet
		if not eLetter in mapping:
			dLetter = b[l]
			mapping[eLetter] = dLetter

#get number of lines	 
numLines = int(raw_input())

#go through input lines
for i in range(numLines):
	line = raw_input().rstrip('\n')
	outLine = ""
	for c in line:
		outLine += mapping[c]
	print "Case #" + str(i+1) + ":", outLine



