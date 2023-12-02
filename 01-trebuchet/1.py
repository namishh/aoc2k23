names=[line.strip() for line in open('inputs.txt')]
sum = 0
def getNumbers(a):
    ltr = a 
    rtl = a[::-1]
    num = ""
    for i in ltr:
        if i.isdigit():
            num+=i 
            break
    for i in rtl:
        if i.isdigit():
            num+=i 
            break
    return int(num)

for i in names:
    sum += getNumbers(i)

print(sum)
