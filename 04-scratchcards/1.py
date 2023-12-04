def seperate(li):
    a = li[0].split(" ")
    b = li[1].split(" ")
    return [[int(i) for i in a if i], [int(i) for i in b if i]]

def getDuplicates(your, winners):
    a = []
    for i in winners:
        if i in your:
            a.append(i)
    return a

def computeCard(card):
    winners = card[0]
    your = card[1]
    dupes = getDuplicates(your, winners)
    d = len(dupes) - 1
    if not d < 0:
        return 2 ** d
    else:
        return 0

def calc(cards): 
    matrix = [seperate(line.strip().split(":")[1].split("|")) for line in open(cards)]
    a = 0
    for card in matrix:
        a += computeCard(card)
    return a

def main():
    c = calc("inputs.txt") 
    print(c)

main()
