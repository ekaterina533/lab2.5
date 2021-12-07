#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#18. Сумму положительных аргументов, расположенных до максимального аргумента.

def maxsum(*args):
    if args:
        summ = 0
        max_idx = max(args)
        for i in args:
            if args.index(i) < args.index(max_idx) and i > 0:
                summ += i
        return summ
    else:
        return None


if __name__ == "__main__":
    k = list(map(int, input('Введите числа:').split()))
    print("Сумма чисел до максимального значения", maxsum(*k))