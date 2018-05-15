def sensor_analysis(sensor_data):
    import math
    mean_sum = sum([data[1] for data in sensor_data])
    mean = mean_sum / len(sensor_data)
    std_dev_tot = sum([math.pow(data[1] - mean, 2) for data in sensor_data])

    return round(mean, 4), round(math.sqrt(std_dev_tot / (len(sensor_data) - 1)), 4)
# https://www.codewars.com/kata/ad2070-help-lorimar-troubleshoot-his-robots-ultrasonic-distance-analysis/train/python

import functools

def multi(l_st):
    return functools.reduce(lambda a, b: a * b, l_st)

def add(l_st):
    return functools.reduce(lambda a, b: a + b, l_st)

def reverse(string):
    return string[::-1]
# https://www.codewars.com/kata/debug-the-functions-easy/train/python/5adf67b7e7dbc45d1e000010

def driver(data):
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
              "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    char_1_6 = data[2][:5].ljust(5, "9").upper() + data[3].split("-")[2][2]
    char_7_8 = months.index(data[3][3:6]) + 1
    if char_7_8 > 9:
        if data[-1] == "F":
            char_7_8 = "6" + str(char_7_8 % 10)
    else:
        if data[-1] == "F":
            char_7_8 = "5" + str(char_7_8)
        else:
            char_7_8 = "0" + str(char_7_8)
    char_9_10 = data[3][0:2]
    char_11 = str(data[3].split("-")[-1])[-1]
    char_12_13 = data[0][0] + data[1][0] if data[1] else data[0][0] + "9"

    return char_1_6 + str(char_7_8) + char_9_10 + char_11 + char_12_13 + "9AA"
# https://www.codewars.com/kata/driving-license/train/python/5ae0a929c5a452323000016a


def xo(s):
    return s.lower().count("x") == s.lower().count("o")
# https://www.codewars.com/kata/exes-and-ohs/train/python

def longest_word(words):
    return sorted(words.split(" "), key = len)[-1]
# https://www.codewars.com/kata/inspiring-strings/train/python

def toJadenCase(string):
    string_copy = string[0].upper()
    for idx, letter in enumerate(string, 1):
        if idx < len(string) and string[idx - 1] == ' ':
            string_copy += string[idx].upper()
        elif idx < len(string) and string[idx - 1] != ' ':
            string_copy += string[idx]

    return string_copy
# https://www.codewars.com/kata/jaden-casing-strings/

def arithmetic(a, b, operator):
    return{"add": a + b, "subtract": a - b, "multiply": a * b, "divide": a / b}[operator]
# https://www.codewars.com/kata/make-a-function-that-does-arithmetic/train/javascript/5adb484e02db6199f60000bc

def box(n):
    return [n * "-"] + (n - 2) * ["-" + (n - 2) * " " + "-"] + [n * "-"]
# https://www.codewars.com/kata/make-a-square-box/train/python/5adf446402db6120dc0000d9


def accum(s):
    ns = ""
    for idx, el in enumerate(s):
        ns += "-" + el.upper() + idx * (el.lower())
    return ns[1:]
# https://www.codewars.com/kata/mumbling/train/python


# return the subtraction of the two polynomials p1 and p2.
import itertools


def poly_subtract(p1, p2):
    return [(a - b) for (a, b) in itertools.zip_longest(p1, p2, fillvalue=0)]
# https://www.codewars.com/kata/nova-polynomial-3-subtract/train/python/5adb6b1836257f3a9600006e


def replace_nth(text, n, old, new):
    if n < 1 or n > text.count(old):
        return text
    nt = ""
    p = 0
    for idx, letter in enumerate(text):
        if letter == old:
            p += 1
            if p % n == 0:
                nt += new
            else:
                nt += letter
        else:
            nt += letter
    return n
# https://www.codewars.com/kata/replace-every-nth/train/python/5ae0c8640913a1ed5c0000bd


def spot_diff(s1, s2):
    return [i for i in range(len(s1)) if s1[i] != s2[i]]
# https://www.codewars.com/kata/spot-the-differences/train/python/


def reverse_slice(s):
    return [s[::-1][i:] for i in range(len(s))]
# https://www.codewars.com/kata/string-reverse-slicing-101/train/python/5adf46970774db0c01000049


def sequence_sum(begin, end, step):
    return sum(range(begin, end + 1, step))
# https://www.codewars.com/kata/sum-of-a-sequence/train/python/5adf6d77e7dbc4de9800003b


def area_code(text):
    return text[text.index("(") + 1:text.index(")")]
# https://www.codewars.com/kata/thinkful-string-drills-areacode-extractor/train/python/5adf3d1a88a0b72369000122
