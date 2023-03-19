"""
https://www.codewars.com/kata/55f89832ac9a66518f000118/train/python
"""
import re

alphabet = 'abcdefghijklmnopqrstuvwxyz'
signs = '*/+-'
numbers = '0123456789'


def simplify(poly):
    print(poly)

    paths = []
    path = ""
    if poly[:1] in signs:
        sign = poly[:1]
    else:
        sign = '+'

    # get signs and paths
    # 1st char is sign, we get it in previous condition
    start = 0
    if poly[:1] in signs:
        start = 1
    for i in range(start, len(poly)):
        if poly[i] in signs or i == len(poly) - 1:
            if i == len(poly) - 1:
                paths.append(sign + path + poly[-1])
            else:
                paths.append(sign + path)
            path = ""
            sign = poly[i]
        else:
            path += poly[i]

    # sort
    for i in range(0, len(paths)):
        paths[i] = ''.join(sorted(paths[i]))
    result = paths.copy()
    print('paths', paths)

    # find sample
    all_samples_indices = []
    all_samples = [[]]
    for i in range(0, len(paths)):
        sample = []
        for j in range(i, len(paths)):
            if get_only_alphabet(paths[i]) == get_only_alphabet(paths[j]) and (j not in all_samples_indices):
                sample.append(paths[j])
                all_samples_indices.append(j)
            if j == len(paths) - 1:
                all_samples.append(sample)
    for array_numbers in all_samples:
        if len(array_numbers) < 2:
            continue
        coefficient = '0'
        for k in range(0, len(array_numbers)):

            result.remove(array_numbers[k])
            coefficient = str(eval(coefficient + get_signs_and_coefficients(array_numbers[k])))
        if coefficient == '0':
            continue
        if coefficient[0] not in signs:
            coefficient = '+' + coefficient
        result.append(coefficient + get_only_alphabet(array_numbers[0]))

    for i in range(0, len(result)):
        if re.match('\+[1]|-[1][a-z]', result[i]):
            result[i] = result[i][:1] + result[i][(1 + 1):]
        elif re.match('[1][a-z]', result[i]):
            result[i] = result[i][1:]

    print(sort_by_length(result))
    print(sort_by_alphabet(result))

    r = ''.join([add_sign(letter) for letter in result])

    if r[0] == "+":
        r = r[1:]
    return r


def add_sign(monomial: str):
    if re.match('[a-z]', monomial):
        monomial = '+' + monomial
    return monomial


def sort_by_length(ls):
    for i1 in range(len(sorted(ls, reverse=True)) - 1):
        replaced = False
        for i2 in range(len(ls) - i1 - 1):
            if len(get_only_alphabet(ls[i2])) > len(get_only_alphabet(ls[i2 + 1])):
                replaced = True
                ls[i2], ls[i2 + 1] = ls[i2 + 1], ls[i2]
        if not replaced:
            break
    return ls


def sort_by_alphabet(ls):
    # example ['a', '+ac', '-ab']
    for i in range(len(ls) - 1):
        # example '+ac'
        replaced = False
        for j in range(len(ls) - i - 1):
            # example '+ac'
            if len(get_only_alphabet(ls[j])) == len(get_only_alphabet(ls[j + 1])):
                for k in range(0, len(get_only_alphabet(ls[j]))):
                    if alphabet.index(get_only_alphabet(ls[j])[k]) > alphabet.index(get_only_alphabet(ls[j + 1])[k]):
                        ls[j], ls[j + 1] = ls[j + 1], ls[j]
                        replaced = True
        if not replaced:
            break
    return ls


def get_only_alphabet(s):
    return ''.join([letter for letter in s if letter in alphabet])


def get_signs_and_coefficients(s):
    result = ''.join([letter for letter in s if letter not in alphabet])
    if not any(char.isdigit() for char in result):
        return result + '1'
    return result


if __name__ == '__main__':
    # 'abcde [f] ghij [k] lmnop [q] rstuvwxyz'
    print(simplify('4e-2y-12r-23h')) # 4a+b-ab+4ac
    print(simplify('-8fk+5kv-4yk+7kf-qk+yqv-3vqy+4ky+4kf+yvqkf'))  # 3fk-kq+5kv-2qvy+fkqvy
