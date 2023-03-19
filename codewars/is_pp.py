
"""
https://www.codewars.com/kata/54d4c8b08776e4ad92000835/train/python
"""
def isPP(n):
    print(n ** 0.5)
    for i in range(2, int((n + 1) ** 0.5) + 1):
        for j in range(2, int((n + 1) ** 0.5) + 1):
            if i ** j == n:
                return [i, j]
            if i ** j > n:
                break
    return None

if __name__ == '__main__':
    print(isPP(37636))
