def calc(maps):
    maps = [line.strip().split(" = ") for line in open(maps)]
    algorithm = [0 if i == "L" else 1 for i in maps[0][0]] * len(maps) # this is not a pretty way to do this but works :p
    curr = algorithm[0]
    nodes = {item[0]: item[1] for item in [[i[0], i[1][1:-1].split(", ")] for i in maps[2:]]}
    currnode = 'AAA'
    steps = 0
    while True:
        if nodes[currnode][curr] == 'ZZZ':
            break 
        else:
            currnode = nodes[currnode][curr]
            steps+=1
            curr = algorithm[steps]
    return steps + 1
def main():
    a = calc("inputs.txt")
    print(a)

main()
