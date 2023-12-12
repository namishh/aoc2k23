from functools import cache

@cache
def mybeautifulrecurstionfunction(config, pairing):
    if (len(pairing) == 0):
        a = int(sum(c == 1 for c in config) == 0)
        return a
    if sum(pairing) > len(config):
        return 0

    if config[0] == 0:
        a = mybeautifulrecurstionfunction(config[1:], pairing)
        return a
    one,two =0,0
     
    if config[0] == 2:
        two = mybeautifulrecurstionfunction(config[1:], pairing) 

    firstgroup = config[:pairing[0]]
    remaining = config[pairing[0] + 1:] if len(config) > pairing[0] else []

    if all(c != 0 for c in firstgroup) and (config[pairing[0]] if remaining else 0) != 1:
        one = mybeautifulrecurstionfunction(tuple(remaining), tuple(pairing[1:]))
    return one + two

def calc(records):
    lines = [line.strip() for line in open(records)] 
    dic ={'.' : 0, '#':1,'?':2}
    configs = [[dic[x] for x in line.split(' ')[0]] for line in lines]
    pairings = [[int(x) for x in line.split(' ')[1].split(',')] for line in lines]
    total = 0
    for i in range(len(configs)):
        total += mybeautifulrecurstionfunction(tuple(((configs[i] + [2])*5)[:-1]), tuple(pairings[i]*5))
    return total

def main():
    print(calc("inputs.txt"))

main()

