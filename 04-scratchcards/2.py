# Cons - takes a lot of time to be processed

def seperate(li):
    a = li[0].split(" ")
    b = li[1].split(" ")
    return [[int(i) for i in a if i], [int(i) for i in b if i]]

def getDuplicates(your, winners):
    return [i for i in winners if i in your]

def computeCard(card, position, b):
    winners = card[0]
    your = card[1]
    dupes = getDuplicates(your, winners) 
    b[position] = b[position] + 1
    for _ in range(b[position]):
        for i in range(len(dupes)):
            n = position + i + 1
            b[n] = b[n] + 1
    return dupes

def calc(cards): 
    matrix = [seperate(line.strip().split(":")[1].split("|")) for line in open(cards)]
    b = [0] * len(matrix)
    for i,card in enumerate(matrix):
        computeCard(card, i, b)
    return sum(b) 

def main():
    c = calc("inputs.txt") 
    print(c)

main()
