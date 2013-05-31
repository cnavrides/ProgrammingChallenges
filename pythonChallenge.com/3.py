#!/usr/bin/env python

huge_string = ''
output = ''
with open('3.input') as in_file:
  for line in in_file:
    huge_string += line.strip()
for i in range(0, len(huge_string)-7):
  isLeftUpper = huge_string[i:i+3].isupper()
  isRightUpper = huge_string[i+4:i+7].isupper()

  if isLeftUpper and isRightUpper and huge_string[i-1].islower() and huge_string[i+7].islower() and huge_string[i+3].islower():
    output += huge_string[i+3]

print output
 
