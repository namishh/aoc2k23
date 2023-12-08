import math

def calc(maps):
    maps = [line.strip().split(" = ") for line in open(maps)]
    algorithm = list([0 if i == "L" else 1 for i in maps[0][0]]) * len(maps)
    curr = algorithm[0]
    nodes = {item[0]: item[1] for item in [[i[0], i[1][1:-1].split(", ")] for i in maps[2:]]}
    aas = [item[0] for item in [[i[0], i[1][1:-1].split(", ")] for i in maps[2:]] if item[0][-1] == 'A']
    def traverse(currnode, curr):
        steps = 0
        while True:
            if nodes[currnode][curr][-1] == 'Z':
                break 
            else:
                currnode = nodes[currnode][curr]
                steps+=1
                curr = algorithm[steps]
        return steps + 1
    step = 1
    for i in aas:
        step = math.lcm(step, traverse(i, curr))
    return step
def main():
    a = calc("inputs.txt")
    print(a)

main()
