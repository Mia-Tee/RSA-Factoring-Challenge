#!/usr/bin/python3
"""Factorizing as many numbers as possible into a product of two smaller numbers"""

import sys


def fact():

    try:
        rfile = sys.argv[1]
        with open(rfile) as f:
            for revnum in f:
                revnum = int(revnum)
                if revnum % 2 == 0:
                        print("{}={}*{}".format(revnum, revnum// 2, 2))
                        continue
                i = 3
                while i < revnum // 2:
                    if revnum % i == 0:
                        print("{}={}*{}".format(revnum, revnum // i, i))
                        break
                    i = i + 2
                if i == (revnum // 2) + 1:
                    print("{}={}*{}".format(revnum, revnum, 1))
    except (IndexError):
        pass


# autostart
fact()
