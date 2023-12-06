def analyze(n, d):
    return len([j for j in [(i, n-i) for i in range(1, n)] if j[0] * j[1] > d])

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

