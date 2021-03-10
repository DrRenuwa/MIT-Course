s = 'azcbobobegghakl'
string = "bob"
count = 0
i = 0

for char in s:
    if char == 'b':
        if s[i:i+3] == string:
            count += 1
    i += 1
    
print("Number of times bob occurs is: " + str(count))