# https://www.youtube.com/watch?v=vyJUW8wW1XE
def doors(n):
    # O(n*2)
    all_doors = {}
    counter = 0
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i == 1:
                all_doors[j] = True
            else:
                if j % i == 0:
                    all_doors[j] = not all_doors[j]
                if i == n:
                    counter += all_doors[j]
    return counter


if __name__ == '__main__':
    print(doors(100))
