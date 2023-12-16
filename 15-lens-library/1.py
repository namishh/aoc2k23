def calc(lenses):
    lenses = [line.strip().split(",") for line in open(lenses)][0]
    values = []
    for lens in lenses:
        val = 0
        for char in lens:
            a = ord(char)
            val = val+a
            val = val * 17 
            val = val % 256
        values.append(val)
    print(sum(values))

def main():
    calc("inputs.txt")

main()
