## DISCLAIMER THIS CODE WILL CRASH YOUR SYSTEM. I DID THIS BY MANUALLY GETTING THE VALUES OF 2 RANGES AT A TIME AND THEN GETTING THEM MINIMUM AT THE END
def seedy(seed, dick):
    n = seed
    v = ['seed-to-soil', 'soil-to-fertilizer', 'fertilizer-to-water', 'water-to-light', 'light-to-temperature', 'temperature-to-humidity', 'humidity-to-location']
    for d in v:
        value = 0
        for i in dick[d]:
            if n >= i[1] and n <= i[1] + i[2]:
                value = n - i[1] + i[0]
                n = value
                break
    return n


def calcSeeds(seeds):
    return [num for start, length in zip(seeds[::2], seeds[1::2]) for num in range(start, start + length)]

def calc(file):
    maps = [line.strip() for line in open(file) if line.strip()]
    seeds = [int(i) for i in maps[0].split(": ")[1].split(" ")]
    seeds = calcSeeds(seeds)
    thedata = maps[1:]
    dick = {}
    curr = ""
    for i in thedata:
        if ":" in i:
            curr = i.split(" ")[0]
            dick[curr] = []
        else:
            dick[curr].append([int(i) for i in i.split()])
    b = []
    for seed in seeds:
        b.append(seedy(seed, dick))
    b.sort()
    return b[0]

def main():
    ans = calc('inputs.txt')
    print(ans)

main()
