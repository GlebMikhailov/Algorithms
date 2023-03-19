def find_boring(numbers):
    length = 0
    numbers_dict = {}
    for i in range(len(numbers)):
        if numbers[i] not in numbers_dict:
            numbers_dict[numbers[i]] = 1
        else:
            numbers_dict[numbers[i]] += 1
        if i > 0:
            new_len = count_sample_elements(numbers_dict)
            if length < new_len:
                length = new_len
    return length


def count_sample_elements(dictionary: dict):
    min_element = 0
    mid_element = 0
    max_element = 0
    i = 0
    length = 0
    changed = False
    print(dictionary)
    for k in sorted(dictionary, key=dictionary.get, reverse=True):
        key, count = k, dictionary[k]
        if i == 0:
            max_element = count
        elif i == len(dictionary) - 1:
            min_element = count
        else:
            if not changed:
                changed = True
                mid_element = count
        length += count
        i += 1
    if i == 2 and (max_element - 1 == min_element or min_element - 1 == 0):
        return length
    elif i > 2:
        if (max_element - 1 == min_element) and len({k: v for k, v in dictionary.items() if v == max_element}) == 1:
            return length

        if min_element - 1 == 0 and max_element == mid_element and len({k: v for k, v in dictionary.items() if v == min_element}) == 1:
            return length
    return -1


print(find_boring([1, 2, 3, 1, 2, 2, 3, 3, 3, 1, 4, 4, 5]))
print(find_boring(list(map(lambda x: int(x), '1 2 4 2 3 1 3 9 15 23'.split()))))
