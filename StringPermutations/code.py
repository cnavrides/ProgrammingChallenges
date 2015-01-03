import sys

def recursiveWords(letters, currentWord=''):
    copyLetters = list(letters)
    allWords = []
    if len(letters) == 0:
        return [currentWord]
    for i in range(len(letters)):
        tmp = letters[i]
        currentWord += tmp
        del copyLetters[i]
        allWords.extend(recursiveWords(copyLetters, currentWord))
        copyLetters.insert(i, tmp)
        currentWord = currentWord[:-1]
    return allWords
        

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    letters = []
    for letter in test.strip():
      letters.append(letter)
    words = recursiveWords(letters)
    output = ''
    for word in sorted(words):
        output += word + ','
    print output[:-1]



test_cases.close()
