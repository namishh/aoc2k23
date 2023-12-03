def valid(i, j, n, m):
    return 0 <= i < n and 0 <= j < m 

def getAdjacent(matrix, i, j):
    n = len(matrix)
    m = len(matrix[0])
    v = []

    directions = [
        (di, dj) for di in range(-1, 2) for dj in range(-1, 2) if (di != 0 or dj != 0)
    ]

    for di, dj in directions:
        ni, nj = i + di, j + dj
        if 0 <= ni < n and 0 <= nj < m and matrix[ni][nj] != ".":
            v.append((matrix[ni][nj], ni,nj))

    return v

def getStars(matrix): 
    a = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == "*":
                a.append((i,j))
    return a

def removeAdjacentDuplicates(lst):
    return [current for current, prev in zip(lst, [None] + lst) if current != prev]

def calc(engine):
    matrix = [list(line.strip()) for line in open(engine)]
    stars = getStars(matrix)
    adjacents = []
    for i in stars:
        x,y = i 
        adj = getAdjacent(matrix, x,y)
        adjacents.append(adj)
    finals = []
    print(adjacents)
    for h in adjacents:
        z = []
        for i in h:
            n = str(i[0])
            xcor,ycor = i[2] ,i[1]
            l,r = xcor,xcor
            a,b = "",""
            while valid(ycor, l + 1, len(matrix), len(matrix[0])) and matrix[ycor][l + 1].isdigit():
                l += 1
                a += str(matrix[ycor][l])
            while valid(ycor, r - 1, len(matrix), len(matrix[0])) and matrix[ycor][r - 1].isdigit():
                r -= 1
                b = str(matrix[ycor][r]) + b
            final = b + n + a 
            z.append(final)
        finals.append(z)
    n = []
    for i in finals:
        n.append(removeAdjacentDuplicates(i))
    a = 0
    for i in n:
        if len(i) != 1:
            a += int(i[0]) * int(i[1])
    return a

def main():
    result = calc("inputs.txt")
    print(result)

main()
