import re

names=[line.strip() for line in open('input.txt')]
nums = {"one":1, "two":2, "three":3, "four":4, "five":5, "six":6, "seven":7, "eight":8, "nine":9}
ns = list(nums.keys())

def getWords(a):
    s = []
    for i in ns:
        s+= [ (i,m.start()) for m in re.finditer(i, a)]
    s = sorted(s, key=lambda x:x[1])
    if not s:
        return []
    else:
        return s

def getNumbers(a):
    ltr = a 
    num = []
    for j,i in enumerate(ltr):
        if i.isdigit():
            num.append((i, j))
    return num

s = 0

def determineType(i):
    if i.isdigit():
        return i 
    else:
        return nums[i]

for i in names:
    a = list(getWords(i)) + list(getNumbers(i))
    sort = sorted(a, key=lambda x: x[1])
    if len(sort) != 1:
        b = determineType(sort[0][0])
        j = determineType(sort[-1][0])
        s += int(str(b) + str(j))
        print(i,int(str(b) + str(j)))
    else:
        print(i,sort)

   

print(s)
