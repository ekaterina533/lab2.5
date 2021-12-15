#!/usr/bin/env python3
# -*- coding: utf-8 -*-


#Найти минимальное значение аргумета

def min_values(**kwargs):
    min_val = min(kwargs.values())
    for k, v in kwargs.items():
        if v == min_val:
            print(f"Переменная минимального значения: {k}, минимальное значение: {v}")


min_values(
    min_1="1",
    min_2="2",
    min_3="9",
    min_4="-1",
    min_5="2",
    min_6="0"
)