from collections import defaultdict, deque

def calc(maze):
    maze = [line.strip() for line in open("inputs.txt")]

    width = len(maze[0])
    height = len(maze)

    horiset = set()
    vertset = set()
    fset = set()
    lset = set()
    sevenset = set()
    jset = set()
    invalidset = set()
    startspace = ()

    for y, h in enumerate(maze):
        for x, c in enumerate(h):
            if c == "-":
                horiset.add((x,y))
            elif c == "|":
                vertset.add((x,y))
            elif c == "F":
                fset.add((x,y))
            elif c == "L":
                lset.add((x,y))
            elif c == "7":
                sevenset.add((x,y))
            elif c == "J":
                jset.add((x,y))
            elif c == "S":
                startspace = (x,y)
            else:
                invalidset.add((x,y))

    neighbordict = defaultdict()
    for x, y in horiset:
        nx1, nx2 = x+1, x-1
        neighbordict[(x,y)] = ((nx1, y),(nx2, y))
    for x, y in vertset:
        ny1, ny2 = y+1, y-1
        neighbordict[(x,y)] = ((x, ny1),(x, ny2))
    for x, y in fset:
        nx1, ny1 = x+1, y+1
        neighbordict[(x,y)] = ((x, ny1),(nx1, y))
    for x, y in lset:
        nx1, ny1 = x+1, y-1
        neighbordict[(x,y)] = ((x, ny1),(nx1, y))
    for x, y in sevenset:
        nx1, ny1 = x-1, y+1
        neighbordict[(x,y)] = ((x, ny1),(nx1, y))
    for x, y in jset:
        nx1, ny1 = x-1, y-1
        neighbordict[(x,y)] = ((x, ny1),(nx1, y))
    x, y = startspace
    neighbordict[startspace] = ((x+1, y),(x-1, y),(x, y+1),(x, y-1))

    core = set()
    frontier = deque()
    core.add(startspace)
    frontier.append((0,startspace))

    while frontier:
        distance, coords = frontier.popleft()
        neighbors = neighbordict[coords]

        for nx, ny in neighbors:
            if nx < 0 or ny < 0 or nx >= width or ny >= height:
                continue
            if (nx, ny) in core or (nx,ny) in invalidset:
                continue
            newneighbors = neighbordict[(nx, ny)]
            if coords not in newneighbors:
                continue
            newdistance = distance+1
            frontier.append((newdistance, (nx,ny)))
            core.add((nx,ny))
        a = distance
    frontier2 = deque()
    core2 = set()
    frontier2.append((-0.5,-0.5))

    while frontier2:
        coords = frontier2.popleft()
        x, y = coords
        if coords in core2:
            continue
        core2.add(coords)

        directions = [(0,1,0.5,0.5,-0.5,0.5),(0,-1,0.5,-0.5,-0.5,-0.5),(1,0,0.5,0.5,0.5,-0.5),(-1,0,-0.5,0.5,-0.5,-0.5)]
        for dx, dy, mx1, my1, mx2, my2 in directions:
            nx, ny, hx1, hy1, hx2, hy2 = x+dx, y+dy, int(x+mx1), int(y+my1), int(x+mx2), int(y+my2)
            if nx < -1 or nx > width or ny < -1 or ny > height:
                continue
            half1, half2 = (hx1, hy1), (hx2, hy2)
            newlocation = (nx, ny)
            if half1 not in core or half2 not in core:
                frontier2.append(newlocation)
                continue
            neighbors1 = set(neighbordict[half1])
            neighbors2 = set(neighbordict[half2])
            if half1 in neighbors2 and half2 in neighbors1:
                continue
            frontier2.append(newlocation)

    part2answer = 0
    for x in range(width):
        for y in range(height):
            if (x, y) in core:
                continue
            tempset = set()
            for dx, dy in [(0.5,0.5),(0.5,-0.5),(-0.5,0.5),(-0.5,-0.5)]:
                nx,ny = x+dx,y+dy
                tempset.add((nx,ny))
            rea = tempset & core2
            if len(rea) == 0:
                part2answer += 1

    return (a, part2answer)
def main():
    a = calc("inputs.txt")
    print(a)

main()
