class Rectangle:

    def __init__(self, id, x_coord, y_coord, width, height):
        self.id = id
        self.left = x_coord
        self.right = x_coord + width
        self.up = y_coord
        self.down = y_coord + height

class FabricSquare:

    def __init__(self):
        self.claims = set()
        self.counter = 0

    def add_claim(self, rec_id):
        self.claims.add(rec_id)
        self.counter += 1

def parser(line):

    # 0  1  2   3    4  5
    # #1 @ 817,273: 26x26

    xs = line.replace(',', ' ').replace(':', ' ').replace('x', ' ').replace('#',' ').split()
    return Rectangle(int(xs[0]) ,int(xs[2]), int(xs[3]), int(xs[4]), int(xs[5]))

def main():
    filename = "input.txt"
    file = open(filename, "r")
    raw = file.readlines()
    parsed = [parser(l) for l in raw]

    fabric = [[FabricSquare() for x in range(1000)] for y in range(1000)]
    s = set()

    for rec in parsed:
        s.add(rec.id)
        for i in range(rec.left, rec.right):
            for j in range(rec.up, rec.down):
                fabric[i][j].add_claim(rec.id)

    counter = 0
    for row in fabric:
        for i in row:
            counter += 1 if i.counter >= 2 else 0
            if i.counter >= 2:
                s -= i.claims

    print(s)
    print(counter)


if __name__ == "__main__":
    main()
