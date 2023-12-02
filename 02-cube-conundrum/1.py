def is_possible(cubes, rev):
    for subset in rev:
        count = {}
        for item in subset:
            c, col = item.split()
            count[col] = count.get(col, 0) + int(c)
        for col, c in count.items():
            if cubes[col] < c:
                return False
    return True

def possibleForAll(cubes, games):
    return [id for id, rev in games if is_possible(cubes, rev)]

def calculate():
    cubes = {'red': 12, 'green': 13, 'blue': 14}
    names=[(int(parts[0].split()[1]), [part.strip().split(', ') for part in parts[1].split(';')])  for parts in (line.strip().split(':') for line in open('./inputs.txt'))]
    possible = sum(possibleForAll(cubes, names))
    pass 

calculate()
