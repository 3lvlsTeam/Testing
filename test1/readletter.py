# -*- coding: utf-8 -*-
"""
Created on Fri Jan 22 22:46:24 2021

@author: abdelrahman maged
"""

count_a = 0
count_A = 0
count_1 = 0
count_ = 0

word_list = 'Words_list.txt'
file = open('rockyou.txt', 'r', errors='ignore')

for x in file:

    count_a = 0
    count_A = 0
    count_1 = 0
    count_ = 0

    if len(x) > 11:
        for char in x:
            asa = ord(char)
            if asa >= 97 and asa <= 122:
                count_a = count_a + 1
            if asa >= 65 and asa <= 90:
                count_A = count_A + 1
            if asa >= 48 and asa <= 57:
                count_1 += count_1 + 1
            if asa >= 33 and asa <= 47:
                count_ = count_+1
            if asa >= 58 and asa <= 64:
                count_ = count_+1
            if asa >= 91 and asa <= 96:
                count_ = count_ + 1
            if asa >= 123 and asa <= 126:
                count_ = count_+1
            # print(count_,char1,)

    counttotal = count_A+count_a

    if count_ >= 1 and count_1 >= 2 and count_A >= 1 and count_a >= 1 and counttotal >= 8:
        # print(x)
        with open(word_list, 'a') as f:
            f.writelines(x)
            # f.writelines('\n')

file.close()
