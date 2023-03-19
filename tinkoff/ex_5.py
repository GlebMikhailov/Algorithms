def f(arr):
    c = 0
    second_iterations = 0
    for i in range(0, len(arr)):
        for j in range(i + 1, len(arr)):
            second_iterations += 1
            if is_normal(arr, i, j):
                c += len(arr) - i - second_iterations
                break
        second_iterations = 0
    return c


# a - origin list
# i - 1st index
# j - last index
def is_normal(a: list, i: int, j: int):
    s = 0
    for k in range(i, j + 1):
        if a[k] == 0:
            continue
        s += a[k]
        if s == 0:
            return True
    return False


s1, s2 = input(), list(map(lambda x: int(x), input().split()))
print(f(s2))

if __name__ == '__main__':
    print(f([-1, 1, 2, -3, 6]) == 6)
    print(f([42, -42, 42]) == 3)
    print(f([1, 2, 3, -6]))
    #         0  1  2   3  4
