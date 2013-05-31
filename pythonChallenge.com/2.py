#!/usr/bin/env python

letters = {}
with open('2.input') as in_file:
  for line in in_file:
    for char in line:
      if char in letters:
        letters[char] += 1
      else:
        letters[char] = 1

print letters
