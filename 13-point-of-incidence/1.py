def split(li):
    result = []
    sublist = []
    for item in li:
        if item == "":
            if sublist:
                result.append(sublist)
                sublist = []
        else:
            sublist.append(list(item))
    if sublist:
        result.append(sublist)
    return result

def findAdjacentDduplicates(input_list):
    duplicates = []
    for i in range(len(input_list) - 1):
        if input_list[i] == input_list[i + 1]:
            duplicates.append(i)
            break
    return duplicates

def countd(m):
    dup = []
    c = 0
    for a in m:
        if m.count(a)>1 and a not in dup:
            c += 1 
            dup.append(a)
    return c

def verticalize(m):
    new = []
    for i in range(len(m[0])):
        l = []
        for j in m:
            l.append(j[i])
        new.append(l)
    return new

def check(m):
    c1,c2 = countd(m),countd(verticalize(m))
    print(c1,c2)
    contains = 0
    if c1>c2:
        if findAdjacentDduplicates(m) == []:
            contains = (findAdjacentDduplicates(verticalize(m))[0] + 1)*100
        else:
            contains = (findAdjacentDduplicates(m)[0] + 1)*100
    else:
        if findAdjacentDduplicates(verticalize(m)) == []:
            contains = findAdjacentDduplicates(m)[0] + 1
        else:
            contains = findAdjacentDduplicates(verticalize(m))[0] + 1
    return contains


def calc(mirrors):
    mirs = [line.strip() for line in open(mirrors)]
    m = split(mirs)
    s = 0
    for i in m:
        s += check(i)
    return s
def main():
    a = calc("inputs.txt")
    print(a)
main()

