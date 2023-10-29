#!/usr/bin/python3
"""Factorizing as many numbers as possible into a product of two smaller numbers."""

from sys import argv


def factorize(nu):
    n = 2

    if nu < 2:
        return
    print()
    print(nu, "<- prev-value")
    while nu % n:
        n += 1
    print("{:.0f}={:.0f}*{:.0f}".format(nu, nu / n, n))
    print(nu, "<- next-value")
    print()

if len(argv) != 2:
    exit()

try:
    with open(argv[1]) as file:
        line = file.readline()

        while line != "":
            nu = int(line.split('\n')[0])
            factorize(nu)
            line = file.readline()
except:
    pass
