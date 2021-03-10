s = 'azcbobobegghakl'

letter = s[0]
testString = ""
longestString = ""

for i in range(len(s)):
    if letter <= s[i]:
        letter = s[i]
        testString += letter
        if len(testString) > len(longestString):
            longestString = testString
    else:
        letter = s[i]
        testString = ""
        testString += letter
                
print("Longest substring in alphabetical order is: " + longestString)