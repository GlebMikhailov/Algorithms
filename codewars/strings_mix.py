"""
https://www.codewars.com/kata/5629db57620258aa9d000014/train/python
"""
import re

alphabet = 'abcdefghijklmnopqrstuvwxyz'
numbers = '0123456789'


def mix(s1, s2):
    if s1 == s2:
        return ""
    res = []

    for i in sorted(merge(count_map(s1), count_map(s2)).values()):
        res.append(i)
    sort_by_alphabet(res)
    return ''.join(items + "/" for items in res)[:-1]


def count_map(word: str):
    res = {}
    for s in set(word):
        if not re.match('[a-z]', s):
            continue
        c = word.count(s)
        if c < 2:
            continue
        res[s] = c
    return res


def merge(m1, m2):
    res = {}
    for s in m1:
        if s in m2:
            if (len(s * m1[s]) < 2) and (len(s * m2[s]) < 2):
                continue
            if m1[s] < m2[s]:
                res[s] = f'2:{s * m2[s]}'
            elif m1[s] > m2[s]:
                res[s] = f'1:{s * m1[s]}'
            else:
                res[s] = f'=:{s * m1[s]}'
            del m2[s]
        else:
            res[s] = f'1:{s * m1[s]}'
    for s in m2:
        if s in m1:
            if (len(s * m2[s]) < 2) and (len(s * m1[s]) < 2):
                continue
            if m2[s] < m1[s]:
                res[s] = f'1:{s * m1[s]}'
            elif m2[s] > m1[s]:
                res[s] = f'2:{s * m2[s]}'
            else:
                res[s] = f'=:{s * m2[s]}'
        else:
            res[s] = f'2:{s * m2[s]}'
    return res


def sort(arr):
    for i in range(len(arr) - 1):
        for k in range(len(arr) - i - 1):
            if get_numbers(arr[i]) < get_numbers(arr[j]):
                pass


def get_only_alphabet(s: str):
    return ''.join(i for i in s if i in alphabet)


def sort_by_alphabet(ls):
    for i in range(len(ls) - 1):
        replaced = False
        for j in range(len(ls) - i - 1):
            if len(get_only_alphabet(ls[j])) < len(get_only_alphabet(ls[j + 1])):
                ls[j], ls[j + 1] = ls[j + 1], ls[j]
                replaced = True
            elif len(get_only_alphabet(ls[j])) == len(get_only_alphabet(ls[j + 1])):
                for k in range(0, len(get_only_alphabet(ls[j]))):
                    if alphabet.index(get_only_alphabet(ls[j])[k]) > alphabet.index(
                            get_only_alphabet(ls[j + 1])[k]) and get_numbers(ls[j]) < get_numbers(ls[j + 1]):
                        ls[j], ls[j + 1] = ls[j + 1], ls[j]
                        replaced = True
        if not replaced:
            break
    return ls


def get_numbers(s):
    return len(''.join(i for i in s if i in numbers))


if __name__ == '__main__':
    print(mix("Are they here", "yes, they are here")) # 2:eeeee/2:yy/=:hh/=:rr
    print(mix("In many languages", " there's a pair of functions")) # -> "1:aaa/1:nnn/1:gg/2:ee/2:ff/2:ii/2:oo/2:rr/2:ss/2:tt"
    print(mix("Sadus:cpms>orqn3zecwGvnznSgacs", "MynwdKizfd$lvse+gnbaGydxyXzayp"))  # -> 2:yyyy/1:ccc/1:nnn/1:sss/2:ddd/=:aa/=:zz
