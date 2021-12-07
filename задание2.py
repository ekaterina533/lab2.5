#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def harmonic(*args):
    if args:
        values = [float(arg) for arg in args]
        n = len(values)
        i = 0
        c = 0
        for i in values:
            c += 1 / i
        return n/c
    else:
        return None


if __name__ == "__main__":
    k = input('Введите числа: ').split()
    print('Среднее гармоническое чисел', harmonic(*k))

