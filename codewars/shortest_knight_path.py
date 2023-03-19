"""
https://www.codewars.com/kata/549ee8b47111a81214000941/train/python
"""


def knight(p1, p2):
    moves = []
    c = 0
    while get_coordinates(p2) not in moves:
        if len(moves) == 0:
            x, y = get_coordinates(p1)
            moves += move(x, y)
        else:
            for i in range(len(moves)):
                x, y = moves[i]
                moves += move(x, y)
            moves = list(set(moves))
        c += 1
    return c


def move(x, y):
    variants = []
    for i in range(4):
        if i < 2:
            if i % 2 == 0:
                new_x = x + 2
            else:
                new_x = x - 2
        else:
            if i % 2 == 0:
                new_x = x - 1
            else:
                new_x = x + 1
        for i2 in range(4):
            new_y = -1
            if i2 < 2:
                if i < 2:
                    if i2 % 2 == 0:
                        new_y = y + 1
                    else:
                        new_y = y - 1
            else:
                if not (i < 2):
                    if i2 % 2 == 0:
                        new_y = y + 2
                    else:
                        new_y = y - 2

            if 0 < new_x < 9 and 0 < new_y < 9:
                variants.append((new_x, new_y))

    return list(set(variants))


def get_coordinates(p):
    alphabet = 'abcdefgh'
    if type(p) is tuple:
        return f'{alphabet[int(p[0]) - 1]}{p[1]}'

    return alphabet.index(p[0]) + 1, int(p[1])


if __name__ == '__main__':
    arr = [['a1', 'c1', 2], ['a1', 'f1', 3], ['a1', 'f3', 3], ['a1', 'f4', 4], ['a1', 'f7', 5]]
    for x in arr:
        z = knight(x[0], x[1])
        print(z == x[2], "{} to {}: expected {}, got {}".format(x[0], x[1], x[2], z))
