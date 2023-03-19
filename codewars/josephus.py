"""
https://www.codewars.com/kata/5550d638a99ddb113e0000a2/train/python
"""


def josephus(items, k):
    res = []
    index = 1
    while len(items) > 0:
        indices = []
        deletes = 0
        for i in range(len(items)):
            if i + 1 % k == 0 or (index > 0 and index % k == 0):
                index = 1
                indices.append(i)
                res.append(items[i])
            else:
                index += 1
        for element in indices:
            print(element)
            items.pop(element - deletes)
            deletes += 1
    return res


if __name__ == '__main__':
    print(josephus(["C", "o", "d", "e", "W", "a", "r", "s"], 4))  # -> ,['e', 's', 'W', 'o', 'C', 'd', 'r', 'a']
    print(josephus([1, 2, 3, 4, 5], 7))  # -> [2, 5, 1, 3, 4]
    print(josephus([True, False, True, False, True, False, True, False, True], 9)) # -> [True, True, True, False, False, True, False, True, False]
