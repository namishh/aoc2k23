## DISCLAIMER THIS CODE WILL CRASH YOUR SYSTEM. I DID THIS BY MANUALLY GETTING THE VALUES OF 2 RANGES AT A TIME AND THEN GETTING THEM MINIMUM AT THE END
import numpy as np

def seedy(seed, dick):
    n = seed
    v = ['seed-to-soil', 'soil-to-fertilizer', 'fertilizer-to-water', 'water-to-light', 'light-to-temperature', 'temperature-to-humidity', 'humidity-to-location']
    for d in v:
        value = 0
        for i in dick[d]:
            if i[1] <= n <= i[1] + i[2]:
                value = n - i[1] + i[0]
                n = value
                break
    return n

def calcSeeds(seeds):
    return np.concatenate([np.arange(i[0], i[0] + i[1]) for i in zip(seeds[::2], seeds[1::2])])

def calc(file):
    maps = [line.strip() for line in open(file) if line.strip()]
    seeds = np.array([int(i) for i in maps[0].split(": ")[1].split(" ")])
    seeds = calcSeeds(seeds)
    thedata = maps[1:]
    dick = {}
    curr = ""
    for i in thedata:
        if ":" in i:
            curr = i.split(" ")[0]
            dick[curr] = []
        else:
            dick[curr].append(np.array([int(x) for x in i.split()]))

    b = np.array([seedy(seed, dick) for seed in seeds])
    return np.min(b)

def main():
    ans = calc('inputs.txt')
    print(ans)

main()
