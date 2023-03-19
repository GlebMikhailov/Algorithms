"""
 https://www.codewars.com/kata/546d15cebed2e10334000ed9/train/python
 To give credit where credit is due: This problem was taken from the ACMICPC-Northwest Regional Programming Contest. Thank you problem writers.

You are helping an archaeologist decipher some runes. He knows that this ancient society used a Base 10 system, and that they never start a number with a leading zero. He's figured out most of the digits as well as a few operators, but he needs your help to figure out the rest.

The professor will give you a simple math expression, of the form

[number][op][number]=[number]
He has converted all of the runes he knows into digits. The only operators he knows are addition (+),subtraction(-), and multiplication (*), so those are the only ones that will appear. Each number will be in the range from -1000000 to 1000000, and will consist of only the digits 0-9, possibly a leading -, and maybe a few ?s. If there are ?s in an expression, they represent a digit rune that the professor doesn't know (never an operator, and never a leading -). All of the ?s in an expression will represent the same digit (0-9), and it won't be one of the other given digits in the expression. No number will begin with a 0 unless the number itself is 0, therefore 00 would not be a valid number.

Given an expression, figure out the value of the rune represented by the question mark. If more than one digit works, give the lowest one. If no digit works, well, that's bad news for the professor - it means that he's got some of his runes wrong. output -1 in that case.

Complete the method to solve the expression to find the value of the unknown rune. The method takes a string as a paramater repressenting the expression and will return an int value representing the unknown rune or -1 if no such rune exists.
"""
import re


def solve_runes(runes):
    s = 0
    print(runes)
    starts_with_zero = False
    example = str(runes).split("=")[0]
    answer = str(runes).split("=")[1]
    example_without_sings = [x for x in re.split('[+-]|\*', example) if x]
    print(example_without_sings)
    for paths_indexes in range(0, len(example_without_sings)):
        contains_questions = example_without_sings[paths_indexes] == len(example_without_sings[paths_indexes]) * '?'
        if example_without_sings[paths_indexes].startswith("?") and any(char.isdigit() for char in example_without_sings[paths_indexes]) and not contains_questions:
            starts_with_zero = True
        if len(example_without_sings[paths_indexes]) > 0 and contains_questions:
            s += 1
            # compare for [? * number=??] or  [number * ?=??], when 1 is not valid, but 2 is valid (for computer
            # checker)
            if eval(example.replace("?", str(s + 1))) == int(answer.replace("?", str(s + 1))):
                return s + 1
        if paths_indexes == len(example_without_sings) - 1 and starts_with_zero:
            s = 1
        else:
            s = 0

    for i in range(0, 10):
        if eval(example.replace("?", str(s))) == int(answer.replace("?", str(s))):
            break
        s += 1
    return -1


if __name__ == '__main__':
    #  bad test
    print(solve_runes("-?56373--9216=-?47157")) # 8
    print(-356373--9216==-347157)  # 8
    # print(solve_runes("??+??=??"))  # -1