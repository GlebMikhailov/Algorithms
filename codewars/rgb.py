"""
The rgb function is incomplete. Complete it so that passing in RGB decimal values will result in a hexadecimal representation being returned. Valid decimal values for RGB are 0 - 255. Any values that fall out of that range must be rounded to the closest valid value.

Note: Your answer should always be 6 characters long, the shorthand with 3 will not work here.
The following are examples of expected output values:

rgb(255, 255, 255) # returns FFFFFF
rgb(255, 255, 300) # returns FFFFFF
rgb(0,0,0) # returns 000000
rgb(148, 0, 211) # returns 9400D3

https://www.codewars.com/kata/513e08acc600c94f01000001/train/python
"""


def rgb(r, g, b):
    return (zero_or_hex(r) + zero_or_hex(g) + zero_or_hex(b)).upper()


def zero_or_hex(n):
    print(n, hex(n))

    if n < 0:
        return "00"

    if n == 0:
        return "00"

    if n > 255:
        return "FF"

    if n < 10:
        return f"0{n}"
    else:
        result = str(hex(n))[2:]
        if len(result) == 1:
            return f"0{result}"
        return result


if __name__ == '__main__':
    print(rgb(46, -147, 13))
