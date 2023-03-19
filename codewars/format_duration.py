"""
https://www.codewars.com/kata/52742f58faf5485cae000b9a/train/python
"""


def format_duration(seconds: int):
    if seconds == 0:
        return 'now'
    formats = {'year': 365 * 24 * 60 * 60, 'day': 24 * 60 * 60, 'hour': 60 * 60, 'minute': 60, 'second': 1}
    res = []
    s = seconds
    for k, v in formats.items():
        if s - v < 0:
            continue
        c = 0
        while s >= v:
            s -= v
            c += 1
        new_key = k
        if c > 1:
            new_key = new_key + 's'
        if (list(formats).index(k) == len(formats) - 1 and len(res) > 0) or (s == 0 and len(res) > 0):
            res.append(' and ')
        elif len(res) > 0:
            res.append(', ')
        res.append(f'{c} {new_key}')
    return ''.join(s for s in res)


if __name__ == '__main__':
    print(format_duration(132030240)) # -> 4 years, 68 days, 3 hours and 4 minutes
