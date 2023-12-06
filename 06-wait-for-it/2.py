def analyze(n, d):
    splitted = [(i, n-i) for i in range(1, n)]
    count = 0
    for j in splitted:
        if j[0] * j[1] > d:
            count+=1
    return count

def calc(file):
    data = [line.strip() for line in open(file) if line.strip()]
    time = int(''.join([i for i in data[0].split(":")[1].strip() if i != " "]))
    distance = int(''.join([i for i in data[1].split(":")[1].strip() if i != " "]))
    a = analyze(time, distance)
    return a

def main():
    a = calc('inputs.txt')
    print(a)  
main()

