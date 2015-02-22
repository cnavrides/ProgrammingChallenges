import sys, re
test_cases = open(sys.argv[1], 'r')

for test in test_cases:
    test_string = test.split(',')[0]
    test_regex = test.split(',')[1].strip()
    test_regex = test_regex.replace('\*', '_')
    test_regex = test_regex.replace('*', '.*')
    test_regex = test_regex.replace('_', '\*')
    if re.search(test_regex, test_string):
        print 'true'
    else:
        print 'false'
test_cases.close()
