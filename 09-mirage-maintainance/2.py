
def parseHistory(history): 
    lines = [history]
    curr = history
    while True:
        differences = [curr[i+1] - curr[i] for i in range(len(curr)-1)]
        lines.append(differences)
        curr = differences
        if all(elem == 0 for elem in differences):
            break 
    sum = 0 
    for i in lines[::-1]:
        sum = i[0] - sum
    return sum

def calc(reports):
    histories = [[int(i) for i in line.strip().split(" ")] for line in open(reports)]
    sum = 0
    for i in histories:
        sum += parseHistory(i)
    return sum

def main():
    a = calc("inputs.txt")
    print(a)

main()
