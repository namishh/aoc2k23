def analyze(n, d):
    splitted = [(i, n-i) for i in range(1, n)]
    count = 0
    for j in splitted:
        if j[0] * j[1] > d:
            count+=1
    return count

def calc(file):
    data = [line.strip() for line in open(file) if line.strip()]
    times = [int(i) for i in data[0].split(":")[1].strip().split(" ") if i != ""]
    distances = [int(i) for i in data[1].split(":")[1].strip().split(" ") if i != ""]
    a =  1
    for i in range(len(times)):
       a = a * analyze(times[i], distances[i])
    return a

def main():
    a = calc('inputs.txt')
    print(a)  
main()
