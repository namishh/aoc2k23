def contains(cells):
    con = False 
    for i in cells:
        if i in "!@#$%^&*()_+=-|\\{}[]:;'\"?/>,<~`":
            con = True 
            break 
    return con

def valid(i, j, n, m):
    return 0 <= i < n and 0 <= j < m 

def getAdjacent(arr, i, j):
    n = len(arr)
    m = len(arr[0])
    v = []
    directions = [(h, k) for h in range(-1, 2) for k in range(-1, 2) if h != 0 or k != 0]
    for h, k in directions:
        ni, nj = i + h, j + k
        if valid(ni, nj, n, m):
            v.append(arr[ni][nj])
    return v

def removeAdjacentDuplicates(lst):
    return [current for current, prev in zip(lst, [None] + lst) if current != prev]

def calc(engine):
    matrix = [list(line.strip()) for line in open(engine)]
    new = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j].isdigit():
                adjacent_cells = getAdjacent(matrix, i, j)
                if contains(adjacent_cells):
                    new.append((matrix[i][j],i,j))
    finals = []
    for i in new:
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
        finals.append(int(final))
    finals = removeAdjacentDuplicates(finals)
    return sum(finals)


def main():
    result = calc("inputs.txt")
    print(f"The sum of part numbers is: {result}")

main()
