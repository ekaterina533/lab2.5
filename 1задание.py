# !/usr/bin/env python3
# -*- coding: utf-8 -*-


def srgeom(*args):
    if args:
        n = len(args)
        c = 1
        for i in args:
            c*=i
        c=c**(1/n)
        return c
    else:
        return None


if __name__ == "__main__":
    k = list(map(int, input('Введите числа:').split()))
    print('Среднее геометрическое чисел', srgeom(*k))