import re


# "sssssaaaabcc" -> "5s4ab2c"
def encode(string):
    current_size = 1
    res = ''
    for i in range(len(string) - 1):
        if string[i] == string[i + 1]:
            current_size += 1
        if (string[i] != string[i + 1]) or (i == len(string) - 2):
            if current_size > 1:
                res += str(current_size) + string[i]
            else:
                res += string[i]
            if i == len(string) - 2 and string[i] != string[i + 1]:
                res += string[i + 1]
            current_size = 1
    return res


def decode(string):
    for i in re.findall('\d+\w', string):
        string = string.replace(i, int(i[:-1]) * i[-1])
    return string


if __name__ == '__main__':
    print(encode('sssssaaaabccca'))
    print(encode('sssssaaaabcz'))
    print(decode('5s4abcz5s'))
