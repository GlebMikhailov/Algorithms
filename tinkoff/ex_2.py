n, m, k = map(lambda x: int(x), input().split())


def res(n, k, m):
    return (n * k / m).__ceil__()


print(res(n, k, m))
