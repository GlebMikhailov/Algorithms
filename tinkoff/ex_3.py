import re
import itertools


def find_substrings(n, s):
    substrings = []
    for j in map(lambda x: x[0] + x[2::], ["+".join(i) for i in itertools.permutations('abcd', 4)]):
        substrings += re.findall(rf"{j}", s)
    substrings_lengths = list(map(lambda x: len(x), substrings))
    return min(substrings_lengths) if len(substrings_lengths) != 0 else -1


print(find_substrings(int(input()), input()))
