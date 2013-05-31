#!/usr/bin/env python
import urllib2
newPart = '8022';
lastLastPart = '';
while newPart.isdigit():
  fc = urllib2.urlopen('http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=' + newPart).read()
  lastLastPart = newPart;
  newPart = fc.split()[-1]
  
print fc, lastLastPart
