#!/usr/bin/env python3
# -*- coding: utf-8 -*-


#Найти минимальное значение аргумета

def min_values(**kwargs):
    min_val = min(kwargs.values())
    for k, v in kwargs.items():
        if v == min_val:
            print("Переменная", k, "минимальное значение", v)


min_values(a=100, b=95, c=88, d=92, e=99)
