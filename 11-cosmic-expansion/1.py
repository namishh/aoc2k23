def getEmpty(matrix):
    vc,hc = [],[]
    num_rows = len(matrix)
    num_cols = len(matrix[0])

    for col in range(num_cols):
        is_vertical_line = all(matrix[row][col] == '.' for row in range(num_rows))
        if is_vertical_line:
            vc.append(col)

    for row in range(num_rows):
        is_horizontal_line = all(char == '.' for char in matrix[row])
        if is_horizontal_line:
            hc.append(row)

    return (vc,hc)

def findGalaxies(matrix):
    coordinates = []
    for rindex, row in enumerate(matrix):
        if "#" in row:
            coordinates.extend((rindex, cindex) for cindex, element in enumerate(row) if element == "#")

    return coordinates

def manhattan(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return abs(x1 - x2) + abs(y1 - y2)

def getdistances(coords):
    distances = []

    for i in range(len(coords)):
        for j in range(i + 1, len(coords)):
            distance = manhattan(coords[i], coords[j])
            distances.append(distance)

    return distances

def calc(file):
    univ = [[char for char in line.strip()] for line in open(file)]
    flatverts,flathortz = getEmpty(univ)
    for i in flathortz:
        univ.insert(i+1,['.']*len(univ[0]))
    for i in flatverts:
        for j in univ:
            j.insert(i+1, ".")
    galaxies = findGalaxies(univ)
    distances = getdistances(galaxies)
    return sum(distances)

def main():
    a = calc("inputs.txt")
    print(a)

main()
