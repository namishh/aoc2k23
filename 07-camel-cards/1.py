from itertools import groupby
def analyzebet(bet):
    hand = bet[0]
    cardlist = list(hand)
    count = {}
    for card in cardlist:
        count[card] = count.get(card, 0) + 1
    unique = len(count.values())
    value = 0
    if unique == 1:
        value = 6
    elif unique == 2:
        if 3 in count.values() and 2 in count.values():
            value = 4
        elif 2 in count.values():
            value = 1
        elif 3 in count.values():
            value = 3
        elif 4 in count.values():
            value = 5
    elif unique == 3:
        if list(count.values()).count(2) > 1:
            value = 2
        elif 3 in count.values():
            value = 3
        else:
            value = 1
    elif unique == 4:
        value = 1
    else:
        value = 0
    return bet + [value]


def sort(li):
    key = "AKQJT98765432"[::-1]
    return sorted(li, key=lambda word: [key.index(c) for c in word[0]])

def calc(bets):
    bets = [line.strip().split() for line in open(bets)]
    final = [analyzebet(bet) for bet in bets]
    grouped_data = [list(g) for _, g in groupby(sorted(final, key=lambda x: x[2]), key=lambda x: x[2])]
    final2 = [sort(i) for i in grouped_data]
    flat = [item for sublist in final2 for item in sublist]
    vals = [int(item[1]) * (index + 1) for index,item in enumerate(flat)]
    return sum(vals)
def main():
    a = calc('inputs.txt')
    print(a)

main()
