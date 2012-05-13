#!/usr/bin/env python
import string
num = int(raw_input())

#all the letters and their T9 code
letters = {'a':'2', 'b':'22', 'c':'222', 'd':'3', 'e':'33','f':'333', 'g':'4', 'h':'44', 'i':'444', 'j':'5', 'k':'55', 'l':'555', 'm':'6', 'n':'66', 'o':'666', 'p':'7', 'q':'77', 'r':'777', 's':'7777', 't':'8', 'u':'88', 'v':'888', 'w':'9', 'x':'99', 'y':'999', 'z':'9999', ' ':'0'} 

for i in range(num):
	text = raw_input()
	previousNum = '1'
	outputString = ""
	#go through each letter of text
	for x in text:
		#if it has the same number put a  space for pause
		if previousNum == letters[x][0]:
			outputString += ' '
		outputString += letters[x]
		previousNum = letters[x][0]
	print "Case #" + str(i+1) +":", outputString


