#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def maxsum(*args):
    if args:
        summ = 0
        max_arg = args[0]
        max_ind = 0
        for i, item in enumerate(args):
            if item > max_arg and item > 0:
                max_arg = item
                max_ind = i
                summ += i
        return summ
    else:
        return None


if __name__ == "__main__":
    k = list(map(int, input('Введите числа:').split()))
    print("Сумма чисел до максимального значения", maxsum(*k))

