def minsets(lines):
    min = []
    for _, revsets in lines:
        count = {}
        for subset in revsets:
            for item in subset:
                c, color = item.split(' ')
                count[color] = max(count.get(color, 0), int(c))
        min.append(count)
    return min

def calc():
    names=[line.strip() for line in open('inputs.txt')]
    lines = []
    for i in names:
        c = i.split(":")
        revset = [part.strip().split(", ") for part in c[1].split(';')]
        lines.append((int(c[0].split()[1]), revset))
    minset =  minsets(lines)
    powset = [cubes['red'] * cubes['green'] * cubes['blue'] for cubes in minset]
    print(sum(powset))
calc()
