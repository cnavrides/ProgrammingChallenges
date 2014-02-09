import sys

inFileName = sys.argv[1]

with open(inFileName) as inFile:
  lines = inFile.readlines()
  for l in lines:
    parts = l.strip().split(' ')
    num = int(parts[-1:][0])
    letters = parts[0:-1]
    letters.reverse()
    if num > len(letters):
      continue

    print letters[num-1]
