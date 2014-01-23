import sys

def convertTeensDigit(digit):
  singles = ['', 'One', 'Two', 'Three', 'Four',
    'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten',
    'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen',
    'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']
  return str(singles[int(digit)])

def convertTensDigit(digit):
  tens = ['', 'Ten', 'Twenty', 'Thirty', 'Forty',
    'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']
  return str(tens[int(digit)])

# Handle each three digit set, returns the string associated
def convertThreeDigits(digits):
  digitLength = len(digits)
  if digitLength == 0:
    return ''
  tmpString = ''

  if digitLength == 3:
    if int(digits[0]) > 0:
      tmpString += convertTeensDigit(digits[0])
      tmpString += 'Hundred'
    if int(digits[1:3]) < 20:
      tmpString += convertTeensDigit(digits[1:3])
    else:
      tmpString += convertTensDigit(digits[1])
      tmpString += convertTeensDigit(digits[2])
  elif digitLength == 2:
    if int(digits) < 20:
      tmpString += convertTeensDigit(digits)
    else:
      tmpString += convertTensDigit(digits[0])
      tmpString += convertTeensDigit(digits[1])
  else:
    tmpString += convertTeensDigit(digits)

  return tmpString

# Takes the string of the number, returning human readable string
def convertNumber(num):
  # What to append to the end
  sizes = ['', 'Thousand', 'Million']

  # String value of the number
  strVal = str(num)

  # Current number of threes
  currentSize = len(strVal)/3

  # Where to break the string
  startPoint = 0
  endPoint = len(strVal) % 3
  # If it is just 3 digits shrink by 1.
  if endPoint == 0:
    endPoint = 3
    currentSize -= 1

  # String to build and ultimately return
  tmpString = ''
  while currentSize > -1:
    digits = convertThreeDigits(strVal[startPoint:endPoint])
    if len(digits) > 0:
      tmpString += digits
      tmpString += sizes[currentSize]
    currentSize -= 1
    startPoint = endPoint
    endPoint += 3
  return tmpString


test_cases = open(sys.argv[1], 'r')
for test in test_cases:
  intVal = int(test.strip())
  if intVal == 0:
    print "ZeroDollars"
    continue
  """ Though gramatically correct, wrong as it wants plurals
  if intVal == 1:
    print "OneDollar"
    continue
  """
  text = ''
  text = ['','negative'] [intVal < 0]
  text += convertNumber(intVal)
  text += 'Dollars'
  print text

test_cases.close()
