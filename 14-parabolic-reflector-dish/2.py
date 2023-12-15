def verticalize(m):
    new = []
    for i in range(len(m[0])):
        l = []
        for j in m:
            l.append(j[i])
        new.append(l[::-1])
    return new

def indices(line):
    inds = []
    for i,j in enumerate(line):
        if j == "O":
            inds.append(i)
    return inds

def moveballs(lst):
    balls = [i for i, char in enumerate(lst) if char == 'O']
    for ball in sorted(balls, reverse=True):
        index = ball
        while index < len(lst) - 1 and lst[index + 1] == '.':
            lst[index], lst[index + 1] = lst[index + 1], lst[index]
            index += 1
    
    return lst

def cycle(n):
    arr = n
    for i in range(3):
        temp = verticalize(arr)
        t = []
        for line in temp:
            t.append(moveballs(line))
        arr = t
    return verticalize(arr)

def calc(ref):
    ref = [list(line.strip()) for line in open(ref)]
    new = verticalize(ref)
    v = []
    for i in range(1000):
        t = new 
        v = cycle(t)
        t = v
    sum = 0 
    for i in v:
        for j,k in enumerate(i):
            if k == 'O':
                sum= sum + j+1

    print(sum)
        
def main():
    calc('inputs.txt')
main()
